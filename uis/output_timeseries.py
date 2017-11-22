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

from stella_output import Stella_Output

pages = ['Page 1', 'Page 2', 'Page 3', 'Page 4', 'Page 5']
display_sections = ['Water Balance', 'HEPP']
display_colors = {
    'I_RFlowdata_mmday': 'r',
    'L_InFlowtoLake': 'b',

    'O_RainAcc': 'g',
    'O_IntercAcc': 'r',
    'O_SurfQFlowAcc': 'k',
    'O_InfAcc': 'b',

    'O_DeepInfAcc': 'r',
    'O_PercAcc': 'k',
    'O_EvapoTransAcc': 'grey',
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

display_spines = {
    'I_RFlowdata_mmday': 20,
    'L_InFlowtoLake': 40,

    'O_RainAcc': 20,
    'O_IntercAcc': 40,
    'O_SurfQFlowAcc': 60,
    'O_InfAcc': 80,
    'O_EvapoTransAcc': 100,

    'O_DeepInfAcc': 15,
    'O_PercAcc': 30,
    'O_BaseFlowAcc': 45,
    'O_SoilQFlowAcc': 60,

    'O_CumRain': 20,
    'O_CumIntercepEvap': 15,
    'O_CumEvapotrans': 30,
    'O_CumSurfQFlow': 45,
    'O_CumInfiltration': 60,

    'O_CumPercolation': 15,
    'O_CumDeepInfilt': 30,
    'O_CumBaseFlow': 45,
    'O_CumSoilQFlow': 60,

    'L_HEPPWatUseFlow': 0,
    'L_LakeVol': 15,
    'L_HEPP_Kwh': 30,
    'L_LakeLevel': 45,
}

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

    def display_selected_maps(self, i):
        if self.isActiveWindow():
            self.lock = True
            self.ax1.clear()
            for timeseries in self.waterBalanceData[self.selected_page].keys():
                self.waterBalanceAxes[timeseries].clear()
                self.waterBalanceAxes[timeseries].plot(self.waterBalanceData[self.selected_page][timeseries], color=display_colors[timeseries])
                self.waterBalanceAxes[timeseries].spines['right'].set_position(('outward', display_spines[timeseries]))
                # self.waterBalanceAxes[timeseries].yaxis.set_ticks([max(self.waterBalanceData[self.selected_page][timeseries]) or [0]])
            self.ax2.clear()
            for timeseries in self.heppData.keys():
                self.heppAxes[timeseries].clear()
                self.heppAxes[timeseries].plot(self.heppData[timeseries], color=display_colors[timeseries])
            self.lock = False

    def update_display(self, output, time):
        self.dayProgress.display(time)
        self.yearProgress.display(time / 365 + 1)
        if not self.lock:
            self.waterBalanceData = output['display']['Water Balance']
            self.heppData = output['display']['HEPP']


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputTimeseries()
    form.show()
    app.exec_()