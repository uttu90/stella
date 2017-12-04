import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import output_timeseries_ui
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
display_sections = ['Water Balance', 'HEPP']

colors = ['r', 'g', 'b', 'y', 'k']
postions = [1, 0.9, 0.8, 0.7, 0.6]
pads = [3.0, 0.0, 0.0, 0.0, 0.0]


class OutputTimeseries(
    QtGui.QDialog,
    output_timeseries_ui.Ui_Dialog,
    Stella_Output):
    def __init__(self, parent=None, outputFolder='', simulationTime=1000):
        super(OutputTimeseries, self).__init__(parent)
        self.setupUi(self)
        self.selected_maps = ["Water Balance", "HEPP"]

        self.simulationTime = simulationTime
        self.currentTime = 0
        self.selected_page = 'Page 1'
        self.waterBalanceData = {}
        self.heppData = {}
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
        # self._clear_waterBalance_page()

    def _select_page_2(self):
        self.selected_page = 'Page 2'
        # self._clear_waterBalance_page()

    def _select_page_3(self):
        self.selected_page = 'Page 3'
        # self._clear_waterBalance_page()

    def _select_page_4(self):
        self.selected_page = 'Page 4'
        # self._clear_waterBalance_page()

    def _select_page_5(self):
        self.selected_page = 'Page 5'
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
        canvas = FigureCanvas(self.fig)
        canvas.setParent(main_frame)
        canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        canvas.setFocus()
        canvas.setSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        main_frame.setLayout(vbox)
        ani = animation.FuncAnimation(self.fig, self.display_selected_maps, interval=1000)
        self.ax1 = self.fig.add_subplot(211)
        self.ax1.yaxis.set_ticks([])
        self.wbAxes = {

        }

        self.ax2 = self.fig.add_subplot(212)
        self.ax2.yaxis.set_ticks([])
        self.heppAxes = {
        }
        canvas.draw()

    def clear_axes(self):
        for page in pages:
            if not page == self.selected_page:
                for timeseries in self.waterBalanceData[page].keys():
                    try:
                        self.wbAxes[timeseries].set_visible(False)
                    except KeyError:
                        None

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
            mainAx.legend(lines, [l.get_label() for l in lines])


    def display_selected_maps(self, i):
        if self.isActiveWindow():
            self.lock = True
            self.display_map(self.waterBalanceData[self.selected_page], self.wbAxes, 211)
            self.display_map(self.heppData, self.heppAxes, 212)

            # self.clear_axes()
            # ax1 = self.fig.add_subplot(211)
            # ax1.clear()
            # lines = []
            # for index, timeseries in enumerate(self.waterBalanceData[self.selected_page].keys()):
            #     try:
            #         axes = self.wbAxes[timeseries]
            #     except KeyError:
            #         self.wbAxes[timeseries] = ax1.twinx()
            #         axes = self.wbAxes[timeseries]
            #     axeplot, = axes.plot(self.waterBalanceData[self.selected_page][timeseries], color=colors[index], label=timeseries)
            #     lines.append(axeplot)
            #     axes.yaxis.set_ticks([])
            #     # axes.set_frame_on(True)
            #     axes.set_visible(True)
            #     # axes.set_title(timeseries)
            #     # axes.patch.set_visible(False)
            #     # for sp in axes.spines.values():
            #     #     sp.set_visible(False)
            #     axes.yaxis.tick_left()
            #     ax1.yaxis.set_ticks([])
            #     y_min, y_max = axes.get_ylim()
            #     # self.max[timeseries] = math.ceil(y_max/100) * 100
            #     axes.set_yticks([y_min, y_max * postions[index]])
            #     axes.set_yticklabels(['0', '%0.4f' %(y_max)])
            #
            #     axes.tick_params('y', colors=colors[index], length=pads[index])
            #     ax1.legend(lines, [l.get_label() for l in lines])
            #     # print timeseries, axes.get_ylim()
            #     # self.waterBalanceAxes[timeseries].spines['right'].set_position(('outward', display_spines[timeseries]))
            #     # self.waterBalanceAxes[timeseries].yaxis.set_ticks([max(self.waterBalanceData[self.selected_page][timeseries]) or [0]])
            # # self.ax2.clear()
            # ax2 = self.fig.add_subplot(212)
            # ax2.clear()
            # hepplines = []
            # for heppIndex, heppName in enumerate(self.heppData.keys()):
            #     # print heppName
            #     try:
            #         heppAxes = self.heppAxes[heppName]
            #     except KeyError:
            #         self.heppAxes[heppName] = ax2.twinx()
            #         heppAxes = self.heppAxes[heppName]
            #
            #     heppAxes.clear()
                # axeplot, = heppAxes.plot(self.heppData[heppName], color=colors[heppIndex],
                #                      label=heppName)
                # hepplines.append(axeplot)
                # heppAxes.yaxis.set_ticks([])
                # heppAxes.yaxis.tick_left()
                # ax2.yaxis.set_ticks([])
                # y_min, y_max = heppAxes.get_ylim()
                # heppAxes.set_yticks([y_min, y_max * postions[heppIndex]])
                # heppAxes.set_yticklabels(['0', '%0.4f' % (y_max)])
                # heppAxes.tick_params('y', colors=colors[heppIndex], length=pads[heppIndex])
                # ax2.legend(lines, [_.get_label() for _ in hepplines])
            self.lock = False

    def update_display(self, output, time):
        self.dayProgress.display(time)
        self.yearProgress.display(time / 365 + 1)
        # self.currentTime = time
        if not self.lock:
            self.waterBalanceData = output['display']['Water Balance']
            self.heppData = output['display']['HEPP']


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputTimeseries()
    form.show()
    app.exec_()