import sys
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2.QtGui import QIcon
class FistMainWin(QMainWindow):
    def __init__(self):
        super(FistMainWin,self).__init__()
        self.setWindowTitle("第一个应用程序")
        self.setWindowIcon(QIcon("./images/Dragon.ico"))
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage("只存在5秒的消息",5000)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FistMainWin()
    win.show()
    sys.exit(app.exec_())

