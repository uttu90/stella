from PyQt4 import QtCore


class Stella_Output(object):
    def __init__(self):
        self.updateQueue = []
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.display_selected_maps)
        timer.start(3000)

    def display_selected_maps(self):
        None

    def update_display(self):
        None