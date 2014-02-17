from PyQt5.QtGui import QDropEvent

__author__ = 'saflores'

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import platform

__version__ = '0.0.1'

class TgtLine(QLineEdit):
    def __init__(self, *args):
        super().__init__(*args)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # we need to accept the proposed action or change it.
        # otherwise dropEvent() won't be called.
        # accept only if there is a copy...
        if event.proposedAction() == QtCore.Qt.CopyAction:
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            str_p = event.mimeData().urls()[0].path()
            print(str_p)
            self.setText(str_p)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 173)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_ref = QLabel(self.centralwidget)
        self.lbl_ref.setObjectName("lbl_ref")
        self.gridLayout.addWidget(self.lbl_ref, 2, 0, 1, 1)

        self.line_test = TgtLine(self.centralwidget)
        self.line_test.setObjectName("line_test")
        self.gridLayout.addWidget(self.line_test, 1, 0, 1, 3)

        self.lbl_test = QLabel(self.centralwidget)
        self.lbl_test.setObjectName("lbl_test")
        self.gridLayout.addWidget(self.lbl_test, 0, 0, 1, 1)

        self.line_ref = QLineEdit(self.centralwidget)
        self.line_ref.setObjectName("line_ref")
        self.gridLayout.addWidget(self.line_ref, 3, 0, 1, 3)

        spacerItem = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)

        self.btn_compare = QPushButton(self.centralwidget)
        self.btn_compare.setObjectName("btn_compare")
        self.gridLayout.addWidget(self.btn_compare, 4, 1, 1, 1)

        spacerItem1 = QSpacerItem(269, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QAction(MainWindow)
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
        """Popup a box with about message."""
        about_str = "<center><b>Validate v{0} </b></center>           " + \
                    "<p>Copyright © 2014 Samuel FLORES.               " + \
                    "All rights reserved in accordance with GPL v3</p>" + \
                    "<p>Python {1} - on {2}</p>"

        QMessageBox.about(self.MainWindow, "Validate",
                          about_str.format(__version__, platform.python_version(), platform.system()))

