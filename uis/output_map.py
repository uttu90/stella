import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import output_map_ui
import constants
from osgeo import gdal
import numpy
import os.path as file_path

from utils import np_utils
from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning

from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat
from stella_output import Stella_Output
import landcover_info


class OutputMap(
    QtGui.QDialog,
    output_map_ui.Ui_Dialog,
    Stella_Output):
    def __init__(self, parent=None, subcatchment='', landcover='', period=[]):
        super(OutputMap, self).__init__(parent)
        self.setupUi(self)
        self.resultBox.addItems(constants.outputMapsSubcatchment)
        self.resultBox_2.addItems(constants.outputMapsSubcatchment)
        self.resultBox_3.addItems(constants.outputMapsSubcatchment)
        self.resultBox_4.addItems(constants.outputMapsSubcatchment)
        self.resultBox.setCurrentIndex(
            constants.outputMapsSubcatchment.index('L_InFlowtoLake')
        )
        self.resultBox_2.setCurrentIndex(
            constants.outputMapsSubcatchment.index('O_EvapoTransAcc')
        )
        self.resultBox_3.setCurrentIndex(
            constants.outputMapsSubcatchment.index('O_PercAcc')
        )
        self.resultBox_4.setCurrentIndex(
            constants.outputMapsSubcatchment.index('O_RainAcc')
        )
        self.selected_maps = [
            str(self.resultBox.currentText()),
            str(self.resultBox_2.currentText()),
            str(self.resultBox_3.currentText()),
            str(self.resultBox_4.currentText()),
        ]
        self.resultBox.currentIndexChanged.connect(self._selectionchange)
        self.resultBox_2.currentIndexChanged.connect(self._selectionchange_2)
        self.resultBox_3.currentIndexChanged.connect(self._selectionchange_3)
        self.resultBox_4.currentIndexChanged.connect(self._selectionchange_4)
        self.subcatchmentFile = subcatchment
        self.landcoverFiles = landcover
        self.autoUpdate = self.checkBox.isChecked()
        self.checkBox.toggled.connect(self._trigger_timer)
        if file_path.isfile(self.subcatchmentFile):
            ds = gdal.Open(self.subcatchmentFile)
            band = ds.GetRasterBand(1)
            subcachmentArray = band.ReadAsArray()
            self.subcachmentArray = numpy.ma.masked_where(
                subcachmentArray <= 0,
                subcachmentArray
            )
        self.landcoverArrays = []
        for landcoverFile in landcover:
            if file_path.isfile(landcoverFile):
                ds = gdal.Open(landcoverFile)
                band = ds.GetRasterBand(1)
                DataArray = band.ReadAsArray()
                landcoverArray = numpy.ma.masked_where(
                    DataArray <= 0,
                    DataArray
                )
                self.landcoverArrays.append(landcoverArray)
        self.nextBtn.clicked.connect(self._next)
        self.backBtn.clicked.connect(self._back)
        self.period = period
        self._prepare_display()
        self.subcachmentId = [_ for _ in range(1, 21)]
        self.updateQueue = []
        self.currentTime = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._timer_timeout)
        if self.autoUpdate:
            self.timer.start(3000)
        self.pausingTime = 0
        self.landcoverDialog = landcover_info.LandcoverInfo()
        self.landcoverColors = self.landcoverDialog.colorResult
        self.landcoverCMaps = colorsmap.ListedColormap(self.landcoverColors)
        print(self.landcoverCMaps)
        self.landcoverInfo.clicked.connect(self.openLandcoverInfo)

    def openLandcoverInfo(self):
        self.landcoverDialog.exec_()
        self.landcoverColors = self.landcoverDialog.colorResult
        self.landcoverCMaps = colorsmap.ListedColormap(self.landcoverColors)

    def _timer_timeout(self):
        self.currentTime = self.currentTime + 1
        self.display_selected_maps()

    def _next(self):
        self.currentTime = (self.currentTime + 1
                            if self.currentTime < len(self.updateQueue) - 1
                            else self.currentTime)
        nextTime, data = self.updateQueue[self.currentTime]
        if not self.playingState and not nextTime < self.pausingTime:
            self.nextBtn.setEnabled(False)
        self.display_selected_maps()

    def _back(self):
        self.currentTime = self.currentTime - 1 if self.currentTime > 0 else 0
        self.nextBtn.setEnabled(True)
        self.display_selected_maps()

    def _trigger_timer(self):
        if self.autoUpdate:
            self.autoUpdate = not self.autoUpdate
            self.timer.stop()
        else:
            self.autoUpdate = True
            self.timer.start(3000)

    def _get_landcover(self, time):
        if time/365 < self.period[0]:
            return self.landcoverArrays[0]
        if time/365 > self.period[0] and time/365 < self.period[1]:
            return self.landcoverArrays[1]
        if time/365 > self.period[1] and time/365 < self.period[2]:
            return self.landcoverArrays[2]
        if time/365 > self.period[2]:
            return self.landcoverArrays[3]

    def _selectionchange(self):
        selection = str(self.resultBox.currentText())
        self.selected_maps[0] = selection

    def _selectionchange_2(self):
        selection = str(self.resultBox_2.currentText())
        self.selected_maps[1] = selection

    def _selectionchange_3(self):
        selection = str(self.resultBox_3.currentText())
        self.selected_maps[2] = selection

    def _selectionchange_4(self):
        selection = str(self.resultBox_4.currentText())
        self.selected_maps[3] = selection

    def display_selected_maps(self):
        screen_position = [221, 222, 223, 224]
        # self.currentTime = self.currentTime + 1
        if self.isVisible() and len(self.updateQueue) > self.currentTime:
            time, output = self.updateQueue[self.currentTime]
            self.dayProgress.display(time)
            self.yearProgress.display(time / 365 + 1)
            self.fig.clear()
            for index, map in enumerate(self.selected_maps):
                self.axes = self.fig.add_subplot(screen_position[index])
                if map == 'Landcover':
                    self.resul1_array = self._get_landcover(time)
                    plt = self.axes.imshow(self.resul1_array, cmap=self.landcoverCMaps)
                    self.fig.colorbar(plt)
                    self.axes.set_title(map)
                    self.canvas.draw()
                else:
                    self.resul1_array = np_utils.array_to_maps(
                        self.subcachmentId,
                        output[map][time],
                        self.subcachmentArray
                    )
                    cm = colorsmap.LinearSegmentedColormap.from_list('abc', [(0.4, 0.76, 1), (0, 0.12, 0.2)])
                    plt = self.axes.imshow(self.resul1_array, cmap=cm)
                    self.fig.colorbar(plt)
                    self.axes.set_title(map)
                    self.canvas.draw()

    def _prepare_display(self):
        self.main_frame = self.displayResult
        self.fig = Figure((1.0, 1.0), dpi=60)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.canvas.setSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        # self.canvas.mpl_connect('key_press_event', self.on_key_press)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)

    def update_display(self, output, time, playingState):
        self.playingState = playingState
        self.checkBox.setEnabled(playingState)
        # self.nextBtn.setEnabled(playingState)
        # self.autoUpdate = playingState
        # if not playingState:
        #     self.checkBox.setChecked(False)
        #
        #     self.pausingTime = time
        #     self.timer.stop()
        self.updateQueue.append((time, output))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputMap()
    form.show()
    app.exec_()