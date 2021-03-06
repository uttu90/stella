import sys
import gc
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from qtdesigners import output_map_ui
import constants
from osgeo import gdal
import numpy as np
import os.path as file_path

from utils import np_utils
from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning

import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat
from stella_output import Stella_Output
import landcover_info_view
from functools import partial

mapDataToDisplay = {

}

screens = [
    'screen 1',
    'screen 2',
    'screen 3',
    'screen 4',
]

mapScreens = {
    'screen 1': ['subcatchment', 'landcover'],
    'screen 2': ['L_InFlowtoLake', 'O_PercAcc', 'O_EvapoTransAcc', 'O_RainAcc'],
    'screen 3': ['O_SurfQFlowAcc', 'O_DeepInfAcc', 'O_BaseFlowAcc', 'O_IntercAcc'],
    'screen 4': ['O_SoilQFlowAcc', 'D_GWaDisch', 'O_InfAcc', 'D_SoilDischarge'],
}

class OutputMap(
    QtGui.QDialog,
    output_map_ui.Ui_Dialog,
    Stella_Output):
    def __init__(self, parent=None, subcatchment='', landcover='', period=[], simulationTime=10000):
        super(OutputMap, self).__init__(parent)
        self.setupUi(self)

        self.landcoverArrays = []
        for landcoverFile in landcover:
            if file_path.isfile(landcoverFile):
                ds = gdal.Open(landcoverFile)
                band = ds.GetRasterBand(1)
                DataArray = band.ReadAsArray()
                landcoverArray = np.ma.masked_where(
                    DataArray <= 0,
                    DataArray
                )
                self.landcoverArrays.append(landcoverArray)
        self.nextBtn.clicked.connect(self._next)
        self.backBtn.clicked.connect(self._back)
        self.period = period
        self._prepare_display()
        self.subcachmentId = [2, 4, 12, 11, 13, 9, 1, 3, 7, 6, 5, 14, 18, 8, 19, 16, 15, 10, 17, 20]
        # self.landCoverId = [1, 2, 8, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 31, 32, 33, 34, 35]
        self.landCoverId = range(0, 20)
        if file_path.isfile(subcatchment):
            ds = gdal.Open(subcatchment)
            band = ds.GetRasterBand(1)
            subcachmentArray = band.ReadAsArray()
            self.subcachmentArray = np.ma.masked_where(
                subcachmentArray <= 0,
                subcachmentArray
            )

        self.landcoverDialog = landcover_info_view.LandcoverInfo()
        landcoverColors = self.landcoverDialog.colorResult
        landcoverSettings = [u'#ffffff' for _ in range(1, 22)]
        for i in range(len(self.landCoverId)):
            landcoverSettings[self.landCoverId[i]] = landcoverColors[i]
        self.subcatchmentDiaglog = landcover_info_view.LandcoverInfo(self, landcover=False)
        subcatchmentColors = self.subcatchmentDiaglog.colorResult
        # print landcoverColors
        self.landcoverCMaps = colorsmap.ListedColormap(landcoverSettings)
        self.subcatchmentCMaps = colorsmap.ListedColormap(subcatchmentColors)
        # print(self.landcoverCMaps)
        self.screens = {
            'screen 1': '',
            'screen 2': '',
            'screen 3': '',
            'screen 4': '',
        }
        self.displayData = {
            'screen 1': '',
            'screen 2': '',
            'screen 3': '',
            'screen 4': '',
        }

        self.data = {}
        for mapName in constants.outputMap:
            self.data[mapName] = np.empty(simulationTime, dtype=object)

        for index, screen in enumerate([self.screen1GroupBox, self.screen2GroupBox, self.screen3GroupBox, self.screen4GroupBox]):
            for radioBtn in screen.children():
                screenText = 'screen %d' % (index + 1)
                radioBtn.toggled.connect(partial(self.triggerRadioBtn, radioBtn, screenText))

        self.landcoverBtn.clicked.connect(self.openLandCover)
        self.subcatchBtn.clicked.connect(self.openSubcatch)
        self.goBtn.clicked.connect(self.gotoDay)

        self.currentTime = 0
        self.lock = False

    def triggerRadioBtn(self, radioBtn, screen):
        if radioBtn.isChecked():
            self.screens[screen] = str(radioBtn.text())
            self.display_selected_maps()

    def gotoDay(self):
        self.currentTime = int(self.goDayEdit.text()) or 0
        self.display_selected_maps()

    def openSubcatch(self):
        self.subcatchmentDiaglog.exec_()
        self.subcatchmentColors = self.subcatchmentDiaglog.colorResult
        self.subcatchmentCMaps = colorsmap.ListedColormap(self.subcatchmentColors)

    def openLandCover(self):
        self.landcoverDialog.exec_()
        self.landcoverColors = self.landcoverDialog.colorResult
        self.landcoverCMaps = colorsmap.ListedColormap(self.landcoverColors)

    def _timer_timeout(self):
        self.currentTime = self.currentTime + 1
        self.display_selected_maps()

    def _next(self):
        self.currentTime = self.currentTime + 1
        self.display_selected_maps()
        # self.currentTime = (self.currentTime + 1
        #                     if self.currentTime < len(self.updateQueue) - 1
        #                     else self.currentTime)
        # nextTime, data = self.updateQueue[self.currentTime]
        # self.display_selected_maps()

    def _back(self):
        self.currentTime = self.currentTime - 1 if self.currentTime > 0 else 0
        # self.nextBtn.setEnabled(True)
        self.display_selected_maps()

    def _trigger_timer(self):
        if self.autoUpdate:
            self.autoUpdate = not self.autoUpdate
            self.timer.stop()
        else:
            self.autoUpdate = True
            self.timer.start(3000)

    def _get_landcover(self, time):
        if time/365 <= self.period[0]:
            return self.landcoverArrays[0]
        if time/365 > self.period[0] and time/365 <= self.period[1]:
            return self.landcoverArrays[1]
        if time/365 > self.period[1] and time/365 <= self.period[2]:
            return self.landcoverArrays[2]
        if time/365 > self.period[2]:
            return self.landcoverArrays[3]

    def display_selected_maps(self):
        screen_position = [221, 222, 223, 224]
        if self.isVisible():
            for screen in screens:
                if screen != 'screen 1' and self.screens[screen] != '':
                    self.displayData[screen] = self.data[self.screens[screen]][self.currentTime]
            self.dayLCD.display(self.currentTime)
            self.fig.clear()
            self.lock = True
            for index, screen in enumerate(screens):
                if screen != 'screen 1' and self.screens[screen] != '':
                    displayMap = self.displayData[screen]
                    axes = self.fig.add_subplot(screen_position[index])
                    displayArray = np_utils.array_to_maps(self.subcachmentId, displayMap, self.subcachmentArray)
                    cm = colorsmap.LinearSegmentedColormap.from_list('abc', [(0.4, 0.76, 1), (0, 0.12, 0.2)])
                    plt = axes.imshow(displayArray, cmap=cm)
                    self.fig.colorbar(plt)
                    axes.set_title(self.screens[screen])
                    axes.xaxis.set_ticks([])
                    axes.yaxis.set_ticks([])
                    # axes.xaxis.set_ticks([])
                    # axes.yaxis.set_ticks([])
                else:
                    if screen == 'screen 1':
                        if self.screens['screen 1'] == 'Landcover map':
                            displayArray = self._get_landcover(self.currentTime)
                            axes = self.fig.add_subplot(221)
                            # cm = colorsmap.LinearSegmentedColormap.from_list('abc', [(0.4, 0.76, 1), (0, 0.12, 0.2)])
                            plt = axes.imshow(displayArray, cmap=self.landcoverCMaps)
                            self.fig.colorbar(plt, ticks=range(1, 22))
                            axes.set_title('landcover')
                            axes.xaxis.set_ticks([])
                            axes.yaxis.set_ticks([])
                        if self.screens['screen 1'] == 'Subcatchment map':
                            # displayArray = self.subcachmentArray
                            axes = self.fig.add_subplot(221)
                            plt = axes.imshow(self.subcachmentArray, cmap=self.subcatchmentCMaps)
                            self.fig.colorbar(plt, ticks=range(1, 21))
                            axes.set_title('subcatchment')
                            axes.xaxis.set_ticks([])
                            axes.yaxis.set_ticks([])
                self.canvas.draw()

            self.lock = False
            # for index, map in enumerate(self.screens.keys()):
            #     self.axes = self.fig.add_subplot(screen_position[index])
            #     if map == 'Landcover':
            #         self.resul1_array = self._get_landcover(self.currentTime)
            #         plt = self.axes.imshow(self.resul1_array, cmap=self.landcoverCMaps)
            #         self.fig.colorbar(plt)
            #         self.axes.set_title(map)
            #         self.canvas.draw()
            #     else:
            #         self.resul1_array = np_utils.array_to_maps(
            #             self.subcachmentId,
            #             output[map][self.currentTime],
            #             self.subcachmentArray
            #         )
            #         cm = colorsmap.LinearSegmentedColormap.from_list('abc', [(0.4, 0.76, 1), (0, 0.12, 0.2)])
            #         plt = self.axes.imshow(self.resul1_array, cmap=cm)
            #         self.fig.colorbar(plt)
            #         self.axes.set_title(map)
            #         self.canvas.draw()

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
        # ani = animation.FuncAnimation(self.fig, self.display_selected_maps, interval=1000)
        # self.canvas.draw()

    def update_display(self, output, time):
        for mapName in constants.outputMap:
            self.data[mapName] = output[mapName]
        del output
        # if time == 100:
        #     for var in output.keys():
        #         print var, output[var][time].shape
        # if time == 1:
        #     for var in output.keys():
        #         print var, output[var][time].shape
        # if not self.lock:
        #     self.data = output
        # for screen in self.screens.keys():
        #     self.displayData[screen] = output[self.screens[screen]][self.currentTime]
        # print self.isActiveWindow()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputMap()
    form.show()
    app.exec_()