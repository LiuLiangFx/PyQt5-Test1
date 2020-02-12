import sys
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtGui import QIcon
class FistMainWin(QMainWindow):
    def __init__(self):
        super(FistMainWin,self).__init__()
        self.setWindowTitle("第一个应用程序")
        #self.setWindowIcon(QIcon("./images/Dragon.ico"))
        self.statu = self.statusBar()
        self.statu.showMessage("此消息只存在5秒",5000)
        self.resize(800,600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/Dragon.ico"))
    win = FistMainWin()
    win.show()
    sys.exit(app.exec_())
