import sys
from PyQt4 import QtGui
import uis
app = QtGui.QApplication(sys.argv)
form = uis.Stella_Main_Window()
form.show()
app.exec_()