from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QRadioButton, QLabel
from Tools.scripts.generate_re_casefix import hexint

from combo_radio import *
import sys, MySQLdb as mdb

conn = mdb.connect("localhost", "root", "", "pixmap")

class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        MainWin.setObjectName("MainWindow")
        MainWin.resize(451, 233)
        layout = QtWidgets.QVBoxLayout(self)
        data = self.get_zagadka()
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(120, 60, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 172, 121, 31))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Rubik\";")
        self.pushButton_2.setObjectName("pushButton_2")

        for i in data:
            self.comboBox.addItem(i[1])


    def get_zagadka(self):
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM zagadki;")
        res = cur.fetchall()
        cur.close()
        return res

    def get_var_otv(self):
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM zagadki;")
        radios = cur.fetchall()
        cur.close()
        return radios

    def radio_append(self):
        radios = self.get_var_otv()
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.setGeometry(QtCore.QRect(10, 100, 300, 200))
        for i in radios:
            self.rad = QtWidgets.QRadioButton(self)
            self.vbox.addWidget(self.rad)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())