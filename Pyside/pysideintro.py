
import sys

from PySide.QtGui import *



class Widg(QWidget):
    def __init__(self):
        super(Widg,self).__init__()
        self.vlayout=QVBoxLayout()
        self.label=QLabel("boo")
        self.button=QPushButton("test")
        self.vlayout.addWidget(self.label)
        self.vlayout.addWidget(self.button)

        self.hlayout=QHBoxLayout()
        self.button2=QPushButton("hbutton1")
        self.button3=QPushButton("hbutton2")
        self.button4=QPushButton("hbutton3")
        self.button5=QPushButton("hbutton4")
        self.hlayout.addWidget(self.button2)
        self.hlayout.addWidget(self.button3)
        self.hlayout.addWidget(self.button4)
        self.hlayout.addWidget(self.button5)
        self.masterlayout=QLayout
        self.masterlayout.addItem(self.hlayout)
        self.setLayout(self.masterlayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Widg()
    frame.show()
    app.exec_()
sys.exit()