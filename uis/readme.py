from PyQt4 import QtGui, QtCore
from qtdesigners import readme_ui

class Readme(QtGui.QDialog, readme_ui.Ui_readme):
    def __init__(self, parent=None):
        super(Readme, self).__init__(parent)
        self.setupUi(self)
        self.data=None
        self.webView.page().setLinkDelegationPolicy(1)
        QtCore.QObject.connect(self.webView.page(), QtCore.SIGNAL('linkClicked(QUrl)'), self.linkClicked)

    def linkClicked(self, url):
        QtGui.QDesktopServices.openUrl(url)
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = Readme()
    form.show()
    app.exec_()