import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import output_timeseries_ui
import constants
from os import path as file_path
from utils import excel_utils
import xlwt

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

class OutputTimeseries(
    QtGui.QDialog,
    output_timeseries_ui.Ui_Dialog,
    Stella_Output):
    def __init__(self, parent=None, outputFolder=''):
        super(OutputTimeseries, self).__init__(parent)
        self.setupUi(self)
        self.selected_maps = ["Water Balance", "HEPP"]
        self.exportData.clicked.connect(self._exportData)
        self.outputFile = (file_path.join(outputFolder, 'output.xls') if
                           outputFolder
                           else file_path.join(file_path.dirname(__file__), 'output.xls'))
        self._prepare_display()
        self.autoUpdate = self.checkBox.isChecked()
        self.checkBox.toggled.connect(self._trigger_timer)
        self.nextBtn.clicked.connect(self._next)
        self.backBtn.clicked.connect(self._back)
        self.currentTime = 0
        self.dataQueue = []
        if not hasattr(self, 'updateQueue'):
            self.updateQueue = []
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self._timer_timeout)
        self.selectedTimeseries = []
        if self.autoUpdate:
            self.timer.start(3000)
        for widget in self.children():
            if isinstance(widget, QtGui.QGroupBox):
                for subWidget in widget.children():
                    subWidget.toggled.connect(self.selectTimeseries)
                    if subWidget.isChecked():
                        self.selectedTimeseries.append(str(subWidget.text()))

    def selectTimeseries(self):
        self.selectedTimeseries = []
        for widget in self.children():
            if isinstance(widget, QtGui.QGroupBox):
                for subWidget in widget.children():
                    subWidget.toggled.connect(self.selectTimeseries)
                    if subWidget.isChecked():
                        self.selectedTimeseries.append(str(subWidget.text()))

    def _timer_timeout(self):
        self.currentTime = self.currentTime + 1
        self.display_selected_maps()

    def _next(self):
        self.currentTime = (self.currentTime + 1
                            if self.currentTime < len(self.updateQueue) - 1
                            else self.currentTime)
        self.display_selected_maps()

    def _back(self):
        self.currentTime = self.currentTime - 1 if self.currentTime > 0 else 0
        self.display_selected_maps()

    def _trigger_timer(self):
        if self.autoUpdate:
            self.autoUpdate = not self.autoUpdate
            self.timer.stop()
        else:
            self.autoUpdate = True
            self.timer.start(3000)

    def _exportData(self):
        print('Start saving')
        outputWb = xlwt.Workbook()
        outputWs = outputWb.add_sheet('outputData')
        time, lastData = self.dataQueue[self.currentTime]
        excel_utils.write_dict(lastData, outputWs, 0)
        outputWb.save(self.outputFile)
        # outputWb.save('test.xls')
        print('End saving')

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
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)

    def display_selected_maps(self):
        screen_position = [211, 212]
        if self.isVisible() and len(self.updateQueue) > self.currentTime:
            time, output = self.updateQueue[self.currentTime]
            self.dayProgress.display(time)
            self.yearProgress.display(time / 365 + 1)
            self.fig.clear()
            for index, timeseries in enumerate(self.selected_maps):
                dict = output[timeseries]
                self.axes = self.fig.add_subplot(screen_position[index])
                for key in self.selectedTimeseries:
                    if key in dict:
                        array = dict[key]
                        display_array = array[-100:] if len(array) > 0 else array
                        self.axes.plot(display_array, label=key)
                self.axes.legend()
                self.axes.set_title(timeseries)
                self.canvas.draw()

    def update_display(self, output, time, playingState):
        self.playingState = playingState
        self.updateQueue.append((time, output['display']))
        self.dataQueue.append((time, output['data']))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputTimeseries()
    form.show()
    app.exec_()