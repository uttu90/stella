import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import output_map_ui
import constants
from osgeo import gdal
import numpy
import os.path as file_path

import utils
from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning

from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat


class OutputMap(
    QtGui.QDialog,
    output_map_ui.Ui_Dialog):
    def __init__(self, parent=None, subcatchment='', landcover=''):
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
        self.landcoverFile = landcover
        if file_path.isfile(self.subcatchmentFile):
            ds = gdal.Open(self.subcatchmentFile)
            band = ds.GetRasterBand(1)
            subcachmentArray = band.ReadAsArray()
            self.subcachmentArray = numpy.ma.masked_where(
                subcachmentArray <= 0,
                subcachmentArray
            )
        self._prepare_display()
        self.subcachmentId = [_ for _ in range(1, 21)]
        self.updateQueue = []
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.display_selected_maps)
        timer.start(3000)

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
        if self.isVisible() and len(self.updateQueue) > 0:
            time, output = self.updateQueue.pop(0)
            self.dayProgress.display(time)
            self.yearProgress.display(time / 365 + 1)
            self.fig.clear()
            for index, map in enumerate(self.selected_maps):
                if self.isVisible():
                    self.axes = self.fig.add_subplot(screen_position[index])
                    self.resul1_array = utils.array_to_maps(
                        self.subcachmentId,
                        output[map][time],
                        self.subcachmentArray
                    )
                    plt = self.axes.imshow(self.resul1_array)
                    self.fig.colorbar(plt)
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

    def update_display(self, output, time):
        self.updateQueue.append((time, output))
        # self.time = time
        # self.output = output
        # self.display_selected_maps()

    def timer_call(self):
        print ('abcdefghlakjdfladfja;dfkljad;fljkadf;lkadjf')

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputMap()
    form.show()
    app.exec_()