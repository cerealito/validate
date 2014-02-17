# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Feb 15 19:18:12 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import platform

__version__ = '0.0.1'


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 173)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_ref = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ref.setObjectName("lbl_ref")
        self.gridLayout.addWidget(self.lbl_ref, 2, 0, 1, 1)

        self.line_test = QtWidgets.QLineEdit(self.centralwidget)
        self.line_test.setObjectName("line_test")
        self.gridLayout.addWidget(self.line_test, 1, 0, 1, 3)

        self.lbl_test = QtWidgets.QLabel(self.centralwidget)
        self.lbl_test.setObjectName("lbl_test")
        self.gridLayout.addWidget(self.lbl_test, 0, 0, 1, 1)

        self.line_ref = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ref.setObjectName("line_ref")
        self.gridLayout.addWidget(self.line_ref, 3, 0, 1, 3)

        spacerItem = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)

        self.btn_compare = QtWidgets.QPushButton(self.centralwidget)
        self.btn_compare.setObjectName("btn_compare")
        self.gridLayout.addWidget(self.btn_compare, 4, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ###########################################################
        # connections follow

        self.btn_compare.clicked.connect(lambda: self.do_something("lambda makes the function " +
                                                                  "annonymous so that we can pass " +
                                                                  "parameters"))

        self.actionAbout.triggered.connect(self.about)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validate"))
        self.btn_compare.setText(_translate("MainWindow", "Compare"))
        self.lbl_ref.setText(_translate("MainWindow", "Reference File:"))
        self.lbl_test.setText(_translate("MainWindow", "Test File:"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    @pyqtSlot()
    def do_something(self, p):
        print("1: is " + self.line_test.text())
        print("2: is " + self.line_ref.text())
        print(p)

    def about(self):
        str = "<center><b>Validate v{0} </b></center>           " + \
              "<p>Copyright © 2014 Samuel FLORES.               " + \
              "All rights reserved in accordance with GPL v3</p>" + \
              "<p>Python {1} - on {2}</p>"

        QMessageBox.about(self.MainWindow, "Validate",
                          str.format(__version__, platform.python_version(), platform.system()))

        '''Popup a box with about message.'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

