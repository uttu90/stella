# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\stella.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(819, 594)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuREADME = QtGui.QMenu(self.menubar)
        self.menuREADME.setObjectName(_fromUtf8("menuREADME"))
        self.menuINPUT = QtGui.QMenu(self.menubar)
        self.menuINPUT.setObjectName(_fromUtf8("menuINPUT"))
        self.menuRUN_SPECS = QtGui.QMenu(self.menubar)
        self.menuRUN_SPECS.setObjectName(_fromUtf8("menuRUN_SPECS"))
        self.menuOUTPUT = QtGui.QMenu(self.menubar)
        self.menuOUTPUT.setObjectName(_fromUtf8("menuOUTPUT"))
        self.menuSIMULATION = QtGui.QMenu(self.menubar)
        self.menuSIMULATION.setObjectName(_fromUtf8("menuSIMULATION"))
        self.menuLANGUAGE = QtGui.QMenu(self.menubar)
        self.menuLANGUAGE.setObjectName(_fromUtf8("menuLANGUAGE"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionRainfall = QtGui.QAction(MainWindow)
        self.actionRainfall.setObjectName(_fromUtf8("actionRainfall"))
        self.actionRiver = QtGui.QAction(MainWindow)
        self.actionRiver.setObjectName(_fromUtf8("actionRiver"))
        self.actionSoil_and_Plant_Water = QtGui.QAction(MainWindow)
        self.actionSoil_and_Plant_Water.setObjectName(_fromUtf8("actionSoil_and_Plant_Water"))
        self.actionLake = QtGui.QAction(MainWindow)
        self.actionLake.setObjectName(_fromUtf8("actionLake"))
        self.actionLake_HEPP = QtGui.QAction(MainWindow)
        self.actionLake_HEPP.setObjectName(_fromUtf8("actionLake_HEPP"))
        self.actionGrass_and_Cattle = QtGui.QAction(MainWindow)
        self.actionGrass_and_Cattle.setObjectName(_fromUtf8("actionGrass_and_Cattle"))
        self.actionSoil_Structure_Dynamic = QtGui.QAction(MainWindow)
        self.actionSoil_Structure_Dynamic.setObjectName(_fromUtf8("actionSoil_Structure_Dynamic"))
        self.actionSubcatchment_Balance = QtGui.QAction(MainWindow)
        self.actionSubcatchment_Balance.setObjectName(_fromUtf8("actionSubcatchment_Balance"))
        self.actionTimeseries = QtGui.QAction(MainWindow)
        self.actionTimeseries.setObjectName(_fromUtf8("actionTimeseries"))
        self.actionMaps = QtGui.QAction(MainWindow)
        self.actionMaps.setObjectName(_fromUtf8("actionMaps"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionInitial_Run = QtGui.QAction(MainWindow)
        self.actionInitial_Run.setObjectName(_fromUtf8("actionInitial_Run"))
        self.actionRun_Specs = QtGui.QAction(MainWindow)
        self.actionRun_Specs.setObjectName(_fromUtf8("actionRun_Specs"))
        self.actionLandcover_maps = QtGui.QAction(MainWindow)
        self.actionLandcover_maps.setObjectName(_fromUtf8("actionLandcover_maps"))
        self.actionSubcatchment_maps = QtGui.QAction(MainWindow)
        self.actionSubcatchment_maps.setObjectName(_fromUtf8("actionSubcatchment_maps"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setObjectName(_fromUtf8("actionEnglish"))
        self.actionVietnamese = QtGui.QAction(MainWindow)
        self.actionVietnamese.setObjectName(_fromUtf8("actionVietnamese"))
        self.menuINPUT.addAction(self.actionLandcover_maps)
        self.menuINPUT.addAction(self.actionSubcatchment_maps)
        self.menuINPUT.addSeparator()
        self.menuINPUT.addAction(self.actionRainfall)
        self.menuINPUT.addAction(self.actionRiver)
        self.menuINPUT.addAction(self.actionSoil_and_Plant_Water)
        self.menuINPUT.addAction(self.actionLake)
        self.menuINPUT.addAction(self.actionLake_HEPP)
        self.menuINPUT.addAction(self.actionGrass_and_Cattle)
        self.menuINPUT.addAction(self.actionSoil_Structure_Dynamic)
        self.menuINPUT.addAction(self.actionSubcatchment_Balance)
        self.menuRUN_SPECS.addAction(self.actionInitial_Run)
        self.menuRUN_SPECS.addAction(self.actionRun_Specs)
        self.menuOUTPUT.addAction(self.actionTimeseries)
        self.menuOUTPUT.addAction(self.actionMaps)
        self.menuSIMULATION.addAction(self.actionRun)
        self.menuSIMULATION.addAction(self.actionStop)
        self.menuLANGUAGE.addAction(self.actionEnglish)
        self.menuLANGUAGE.addAction(self.actionVietnamese)
        self.menubar.addAction(self.menuREADME.menuAction())
        self.menubar.addAction(self.menuINPUT.menuAction())
        self.menubar.addAction(self.menuRUN_SPECS.menuAction())
        self.menubar.addAction(self.menuOUTPUT.menuAction())
        self.menubar.addAction(self.menuSIMULATION.menuAction())
        self.menubar.addAction(self.menuLANGUAGE.menuAction())
        self.toolBar.addAction(self.actionRun_Specs)
        self.toolBar.addAction(self.actionInitial_Run)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTimeseries)
        self.toolBar.addAction(self.actionMaps)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "stella Python", None))
        self.menuREADME.setTitle(_translate("MainWindow", "README", None))
        self.menuINPUT.setTitle(_translate("MainWindow", "INPUT", None))
        self.menuRUN_SPECS.setTitle(_translate("MainWindow", "RUN SPECS", None))
        self.menuOUTPUT.setTitle(_translate("MainWindow", "OUTPUT", None))
        self.menuSIMULATION.setTitle(_translate("MainWindow", "SIMULATION", None))
        self.menuLANGUAGE.setTitle(_translate("MainWindow", "LANGUAGE", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionRainfall.setText(_translate("MainWindow", "Rainfall", None))
        self.actionRiver.setText(_translate("MainWindow", "River", None))
        self.actionSoil_and_Plant_Water.setText(_translate("MainWindow", "Soil and Plant Water", None))
        self.actionLake.setText(_translate("MainWindow", "Lake", None))
        self.actionLake_HEPP.setText(_translate("MainWindow", "Lake/HEPP", None))
        self.actionGrass_and_Cattle.setText(_translate("MainWindow", "Grass and Cattle", None))
        self.actionSoil_Structure_Dynamic.setText(_translate("MainWindow", "Soil Structure Dynamic", None))
        self.actionSubcatchment_Balance.setText(_translate("MainWindow", "Subcatchment Balance", None))
        self.actionTimeseries.setText(_translate("MainWindow", "Timeseries", None))
        self.actionMaps.setText(_translate("MainWindow", "Maps", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionInitial_Run.setText(_translate("MainWindow", "Initial Run", None))
        self.actionRun_Specs.setText(_translate("MainWindow", "Run Specs", None))
        self.actionLandcover_maps.setText(_translate("MainWindow", "Landcover maps", None))
        self.actionSubcatchment_maps.setText(_translate("MainWindow", "Subcatchment map", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionEnglish.setText(_translate("MainWindow", "English", None))
        self.actionVietnamese.setText(_translate("MainWindow", "Vietnamese", None))

