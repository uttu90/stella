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
display_configuration = {
    'I_RFlowdata_mmday': {
        'color': 'r',
        'position': 1,
        'pad': True,
    },
    'L_InFlowtoLake': {
        'color': 'b',
        'position': 0.85,
        'pad': False
    },
    'O_RainAcc': {
        'color': 'r',
        'position': 1,
        'pad': True
    },
    'O_IntercAcc': {
        'color': 'g',
        'position': 0.85,
        'pad': False
    },
    'O_EvapoTransAcc': {
        'color': 'b',
        'position': 0.7,
        'pad': False
    },

    'O_SurfQFlowAcc': {
        'color': 'y',
        'position': 0.55,
        'pad': False
    },
    'O_InfAcc': {
        'color': 'k',
        'position': 0.4,
        'pad': False
    },

    'O_DeepInfAcc': {
        'color': 'g',
        'position': 0.85,
        'pad': False
    },

    'O_PercAcc': 'k',

    'O_BaseFlowAcc': 'b',
    'O_SoilQFlowAcc': 'y',

    'O_CumRain': 'r',
    'O_CumIntercepEvap': 'g',
    'O_CumEvapotrans': 'b',
    'O_CumSurfQFlow': 'k',
    'O_CumInfiltration': 'y',

    'O_CumPercolation': 'g',
    'O_CumDeepInfilt': 'b',
    'O_CumBaseFlow': 'k',
    'O_CumSoilQFlow': 'y',

    'L_HEPPWatUseFlow': 'r',
    'L_LakeVol': 'g',
    'L_HEPP_Kwh': 'b',
    'L_LakeLevel': 'k',
}

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

    def _clear_waterBalance_page(self):
        for page in pages:
            for timeseries in self.waterBalanceData[page].keys():
                self.waterBalanceAxes[timeseries].clear()

    def _select_page_1(self):
        self.selected_page = 'Page 1'
        self._clear_waterBalance_page()

    def _select_page_2(self):
        self.selected_page = 'Page 2'
        self._clear_waterBalance_page()

    def _select_page_3(self):
        self.selected_page = 'Page 3'
        self._clear_waterBalance_page()

    def _select_page_4(self):
        self.selected_page = 'Page 4'
        self._clear_waterBalance_page()

    def _select_page_5(self):
        self.selected_page = 'Page 5'
        self._clear_waterBalance_page()

    # def _exportData(self):
    #     print('Start saving')
    #     outputWb = xlwt.Workbook()
    #     outputWs = outputWb.add_sheet('outputData')
    #     time, lastData = self.dataQueue[self.currentTime]
    #     excel_utils.write_dict(lastData, outputWs, 0)
    #     outputWb.save(self.outputFile)
    #     # outputWb.save('test.xls')
    #     print('End saving')

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
        self.waterBalanceAxes = {
            'I_RFlowdata_mmday': self.ax1.twinx(),
            'L_InFlowtoLake': self.ax1.twinx(),

            'O_RainAcc': self.ax1.twinx(),
            'O_IntercAcc': self.ax1.twinx(),
            'O_SurfQFlowAcc': self.ax1.twinx(),
            'O_InfAcc': self.ax1.twinx(),

            'O_DeepInfAcc': self.ax1.twinx(),
            'O_PercAcc': self.ax1.twinx(),
            'O_EvapoTransAcc': self.ax1.twinx(),
            'O_BaseFlowAcc': self.ax1.twinx(),
            'O_SoilQFlowAcc': self.ax1.twinx(),

            'O_CumRain': self.ax1.twinx(),
            'O_CumIntercepEvap': self.ax1.twinx(),
            'O_CumEvapotrans': self.ax1.twinx(),
            'O_CumSurfQFlow': self.ax1.twinx(),
            'O_CumInfiltration': self.ax1.twinx(),

            'O_CumPercolation': self.ax1.twinx(),
            'O_CumDeepInfilt': self.ax1.twinx(),
            'O_CumBaseFlow': self.ax1.twinx(),
            'O_CumSoilQFlow': self.ax1.twinx(),
        }
        self.ax2 = self.fig.add_subplot(212)
        self.ax2.yaxis.set_ticks([])
        self.heppAxes = {
            'L_HEPPWatUseFlow': self.ax2.twinx(),
            'L_LakeVol': self.ax2.twinx(),
            'L_HEPP_Kwh': self.ax2.twinx(),
            'L_LakeLevel': self.ax2.twinx(),
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

    def display_selected_maps(self, i):
        if self.isActiveWindow():
            self.lock = True
            self.clear_axes()
            ax1 = self.fig.add_subplot(211)
            ax1.clear()
            lines = []
            for index, timeseries in enumerate(self.waterBalanceData[self.selected_page].keys()):
                try:
                    axes = self.wbAxes[timeseries]
                except KeyError:
                    self.wbAxes[timeseries] = ax1.twinx()
                    axes = self.wbAxes[timeseries]
                axeplot, = axes.plot(self.waterBalanceData[self.selected_page][timeseries], color=colors[index], label=timeseries)
                lines.append(axeplot)
                axes.yaxis.set_ticks([])
                # axes.set_frame_on(True)
                axes.set_visible(True)
                # axes.set_title(timeseries)
                # axes.patch.set_visible(False)
                # for sp in axes.spines.values():
                #     sp.set_visible(False)
                axes.yaxis.tick_left()
                ax1.yaxis.set_ticks([])
                self.min[timeseries], y_max = axes.get_ylim()
                # self.max[timeseries] = math.ceil(y_max/100) * 100
                axes.set_yticks([self.min[timeseries], y_max * postions[index]])
                axes.set_yticklabels(['0', '%0.4f' %(y_max)])

                axes.tick_params('y', colors=colors[index], length=pads[index])
                ax1.legend(lines, [l.get_label() for l in lines])
                # print timeseries, axes.get_ylim()
                # self.waterBalanceAxes[timeseries].spines['right'].set_position(('outward', display_spines[timeseries]))
                # self.waterBalanceAxes[timeseries].yaxis.set_ticks([max(self.waterBalanceData[self.selected_page][timeseries]) or [0]])
            self.ax2.clear()
            for timeseries in self.heppData.keys():
                self.heppAxes[timeseries].clear()
                # self.heppAxes[timeseries].plot(self.heppData[timeseries], color=display_colors[timeseries])
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