import sys
import gc
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from qtdesigners import output_timeseries_ui
import constants
from os import path as file_path
from utils import excel_utils
import xlwt
import numpy as np
from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
import matplotlib.animation as animation

from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat
import math

from stella_output import Stella_Output

pages = ['Page 1', 'Page 2', 'Page 3', 'Page 4', 'Page 5']
wbPages = {
    'Page 1': ['I_RFlowdata_mmday', 'L_InFlowtoLake'],
    'Page 2': [
        'O_RainAcc',
        'O_IntercAcc',
        'O_EvapoTransAcc',
        'O_SurfQFlowAcc',
        'O_InfAcc'],
    'Page 3': [
        'O_RainAcc',
        'O_DeepInfAcc',
        'O_PercAcc',
        'O_BaseFlowAcc',
        'O_SoilQFlowAcc'
    ],
    'Page 4': [
        'O_CumRain',
        'O_CumIntercepEvap',
        'O_CumEvapotrans',
        'O_CumSurfQFlow',
        'O_CumInfiltration'
    ],
    'Page 5': [
        'O_CumRain',
        'O_CumPercolation',
        'O_CumDeepInfilt',
        'O_CumBaseFlow',
        'O_CumSoilQFlow'
    ],
}

heppPages = [
    'L_LakeVol',
    'L_HEPPWatUseFlow',
    'L_HEPP_Kwh',
    'L_LakeLevel'
]
# display_sections = ['Water Balance', 'HEPP']

colors = ['r', 'g', 'b', 'y', 'k']
postions = [1, 0.9, 0.8, 0.7, 0.6]
pads = [3.0, 0.0, 0.0, 0.0, 0.0]


class OutputTimeseries(
    QtGui.QDialog,
    output_timeseries_ui.Ui_Dialog,
    Stella_Output):
    def __init__(self, parent=None, simulationTime=1000):
        super(OutputTimeseries, self).__init__(parent)
        self.setupUi(self)
        self.selected_maps = ["Water Balance", "HEPP"]

        self.simulationTime = simulationTime
        self.currentTime = 0
        self.selected_page = 'Page 1'
        self.timeseriesData = {}
        self.waterBalanceData = {}
        self.heppData = {}
        for timeseries in constants.outputTimeseries:
            self.timeseriesData[timeseries] = np.empty(simulationTime)
        # for mapName in constants.outputMaps:
        #     self.
        self._prepare_display()
        self.page1Btn.clicked.connect(self._select_page_1)
        self.page2Btn.clicked.connect(self._select_page_2)
        self.page3Btn.clicked.connect(self._select_page_3)
        self.page4Btn.clicked.connect(self._select_page_4)
        self.page5Btn.clicked.connect(self._select_page_5)
        self.lock = False
        self.min = {}
        self.max = {}

    # def _clear_waterBalance_page(self):
    #     for page in pages:
    #         for timeseries in self.waterBalanceData[page].keys():
    #             self.waterBalanceAxes[timeseries].clear()

    def _select_page_1(self):
        self.selected_page = 'Page 1'
        self.display_selected_maps()
        # self._clear_waterBalance_page()

    def _select_page_2(self):
        self.selected_page = 'Page 2'
        self.display_selected_maps()
        # self._clear_waterBalance_page()

    def _select_page_3(self):
        self.selected_page = 'Page 3'
        self.display_selected_maps()
        # self._clear_waterBalance_page()

    def _select_page_4(self):
        self.selected_page = 'Page 4'
        self.display_selected_maps()
        # self._clear_waterBalance_page()

    def _select_page_5(self):
        self.selected_page = 'Page 5'
        self.display_selected_maps()
        # self._clear_waterBalance_page()

    def displayTimeseries(self, i):
        axes = self.fig.add_subplot(1,1,1)
        axes.clear()
        axes.set_xlim(0, self.simulationTime)
        for timeseries in self.data.keys():
            ax = axes.twinx()
            ax.plot(self.data[timeseries])

    def _prepare_display(self):
        main_frame = self.displayResult
        self.fig = Figure((1.0, 1.0), dpi=60)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(main_frame)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.canvas.setSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        mpl_toolbar = NavigationToolbar(self.canvas, main_frame)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(mpl_toolbar)
        main_frame.setLayout(vbox)
        # ani = animation.FuncAnimation(self.fig, self.display_selected_maps, interval=1000)
        self.ax1 = self.fig.add_subplot(211)
        self.ax1.yaxis.set_ticks([])
        self.wbAxes = {

        }

        self.ax2 = self.fig.add_subplot(212)
        self.ax2.yaxis.set_ticks([])
        self.heppAxes = {
        }
        self.canvas.draw()

    def clear_axes(self):
        for page in pages:
            if not page == self.selected_page:
                for timeseries in wbPages[page]:
                    try:
                        self.wbAxes[timeseries].set_visible(False)
                    except KeyError:
                        None

    def display_waterbalance(self):
        ax = self.fig.add_subplot(211)
        ax.clear()
        lines = []
        self.clear_axes()
        for index, timeseries in enumerate(wbPages[self.selected_page]):
            try:
                axes = self.wbAxes[timeseries]
            except KeyError:
                self.wbAxes[timeseries] = ax.twinx()
                axes = self.wbAxes[timeseries]
            axeplot, = axes.plot(self.timeseriesData[timeseries], color=colors[index],
                                 label=timeseries)
            lines.append(axeplot)
            axes.yaxis.set_ticks([])
            axes.set_visible(True)
            axes.yaxis.tick_left()
            ax.yaxis.set_ticks([])
            y_min, y_max = axes.get_ylim()
            axes.set_yticks([y_min, y_max * postions[index]])
            axes.set_yticklabels(['0', '%0.4f' % (y_max)])
            axes.tick_params('y', colors=colors[index], length=pads[index])
        ax.legend(lines, [l.get_label() for l in lines], bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                      ncol=len(lines), mode="expand", borderaxespad=0.)

    def display_hepp(self):
        ax = self.fig.add_subplot(212)
        ax.clear()
        lines = []
        # self.clear_axes()
        for index, timeseries in enumerate(heppPages):
            try:
                axes = self.heppAxes[timeseries]
            except KeyError:
                self.heppAxes[timeseries] = ax.twinx()
                axes = self.heppAxes[timeseries]
            axeplot, = axes.plot(self.timeseriesData[timeseries], color=colors[index],
                                 label=timeseries)
            lines.append(axeplot)
            axes.yaxis.set_ticks([])
            axes.set_visible(True)
            axes.yaxis.tick_left()
            ax.yaxis.set_ticks([])
            y_min, y_max = axes.get_ylim()
            # print y_max, postions[index]
            axes.set_yticks([y_min, y_max * postions[index]])
            axes.set_yticklabels(['0', '%0.4f' % (y_max)])
            axes.tick_params('y', colors=colors[index], length=pads[index])
        ax.legend(lines, [l.get_label() for l in lines], bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                      ncol=len(lines), mode="expand", borderaxespad=0.)
        ax.set_xlabel('day')

    def display_map(self, data, dataAxes, pos):
        mainAx = self.fig.add_subplot(pos)
        mainAx.clear()
        lines = []
        if (pos == 211):
            self.clear_axes()
        for index, timeseries in enumerate(data.keys()):
            try:
                axes = dataAxes[timeseries]
            except KeyError:
                dataAxes[timeseries] = mainAx.twinx()
                axes = dataAxes[timeseries]
            axeplot, = axes.plot(data[timeseries], color=colors[index],
                                 label=timeseries)
            lines.append(axeplot)
            axes.yaxis.set_ticks([])
            axes.set_visible(True)
            axes.yaxis.tick_left()
            mainAx.yaxis.set_ticks([])
            y_min, y_max = axes.get_ylim()
            axes.set_yticks([y_min, y_max * postions[index]])
            axes.set_yticklabels(['0', '%0.4f' % (y_max)])
            axes.tick_params('y', colors=colors[index], length=pads[index])
            mainAx.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                            ncol=len(lines), mode="expand", borderaxespad=0.)
            # mainAx.legend(lines, [l.get_label() for l in lines])


    def showEvent(self, e):
        # print "show", e
        self.display_selected_maps()

    def display_selected_maps(self):
        self.lock = True
        self.display_waterbalance()
        self.display_hepp()
        self.canvas.draw()

    def update_display(self, output, time):
        self.dayProgress.display(time)
        self.yearProgress.display(time / 365 + 1)
        for timeseries in constants.outputTimeseries:
            self.timeseriesData[timeseries] = output[timeseries]
            # if time in [self.simulationTime/4, self.simulationTime/2, self.simulationTime-1]:
            #     self.display_selected_maps()
        del output
        # if not self.lock:
        #     self.waterBalanceData = output['display']['Water Balance']
        #     self.heppData = output['display']['HEPP']

        # print 'by by output timeseries'
        # print sys.getsizeof(self.timeseriesData)
        # self.timeseriesData = None
        # gc.collect()



if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputTimeseries()
    form.show()
    app.exec_()