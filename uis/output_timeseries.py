import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import output_timeseries_ui
import constants

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
    def __init__(self, parent=None):
        super(OutputTimeseries, self).__init__(parent)
        self.setupUi(self)
        self.resultBox.addItems(constants.ouputTimeSeries)
        self.resultBox_2.addItems(constants.ouputTimeSeries)
        self.resultBox_3.addItems(constants.ouputTimeSeries)
        self.resultBox_4.addItems(constants.ouputTimeSeries)
        self.resultBox.setCurrentIndex(
            constants.ouputTimeSeries.index('L_HEPPWatUseFlow')
        )
        self.resultBox_2.setCurrentIndex(
            constants.ouputTimeSeries.index('L_HEPP_Kwh')
        )
        self.resultBox_3.setCurrentIndex(
            constants.ouputTimeSeries.index('L_LakeVol')
        )
        self.resultBox_4.setCurrentIndex(
            constants.ouputTimeSeries.index('L_LakeLevel')
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
        self._prepare_display()
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

    def display_selected_maps(self):
        screen_position = [221, 222, 223, 224]
        if self.isVisible() and len(self.updateQueue) > 0:
            time, output = self.updateQueue.pop(0)
            self.dayProgress.display(time)
            self.yearProgress.display(time / 365 + 1)
            if self.isVisible():
                self.fig.clear()
                for index, timeseries in enumerate(self.selected_maps):
                    array = output[timeseries]
                    display_array = array[-10:] if len(array) >0 else array
                    self.axes = self.fig.add_subplot(screen_position[index])
                    self.axes.set_ylim(0, max(display_array) * 1.1)
                    self.axes.set_autoscale_on(True)
                    self.axes.plot(display_array, linestyle='steps-post')
                    self.axes.set_xlabel('day')
                    self.canvas.draw()

    def update_display(self, output, time):
        self.updateQueue.append((time, output))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = OutputTimeseries()
    form.show()
    app.exec_()