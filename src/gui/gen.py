# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Feb 24 18:02:34 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_designer_window(object):
    def setupUi(self, designer_window):
        designer_window.setObjectName("designer_window")
        designer_window.resize(648, 173)
        self.central_widget = QtWidgets.QWidget(designer_window)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_test = TgtLine(self.central_widget)
        self.line_test.setObjectName("line_test")
        self.gridLayout.addWidget(self.line_test, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.btn_compare = QtWidgets.QPushButton(self.central_widget)
        self.btn_compare.setObjectName("btn_compare")
        self.gridLayout.addWidget(self.btn_compare, 4, 1, 1, 1)
        self.line_ref = TgtLine(self.central_widget)
        self.line_ref.setObjectName("line_ref")
        self.gridLayout.addWidget(self.line_ref, 3, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.lbl_ref = QtWidgets.QLabel(self.central_widget)
        self.lbl_ref.setObjectName("lbl_ref")
        self.gridLayout.addWidget(self.lbl_ref, 2, 0, 1, 1)
        self.lbl_test = QtWidgets.QLabel(self.central_widget)
        self.lbl_test.setObjectName("lbl_test")
        self.gridLayout.addWidget(self.lbl_test, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 3)
        designer_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(designer_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 18))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_validate = QtWidgets.QMenu(self.menubar)
        self.menu_validate.setObjectName("menu_validate")
        designer_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(designer_window)
        self.statusbar.setObjectName("statusbar")
        designer_window.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(designer_window)
        self.action_about.setObjectName("action_about")
        self.action_preferences = QtWidgets.QAction(designer_window)
        self.action_preferences.setObjectName("action_preferences")
        self.menu_help.addAction(self.action_about)
        self.menu_validate.addAction(self.action_preferences)
        self.menubar.addAction(self.menu_validate.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(designer_window)
        QtCore.QMetaObject.connectSlotsByName(designer_window)

    def retranslateUi(self, designer_window):
        _translate = QtCore.QCoreApplication.translate
        designer_window.setWindowTitle(_translate("designer_window", "Validate"))
        self.btn_compare.setText(_translate("designer_window", "Compare"))
        self.lbl_ref.setText(_translate("designer_window", "Reference File:"))
        self.lbl_test.setText(_translate("designer_window", "Test File:"))
        self.menu_help.setTitle(_translate("designer_window", "Help"))
        self.menu_validate.setTitle(_translate("designer_window", "validate"))
        self.action_about.setText(_translate("designer_window", "About"))
        self.action_preferences.setText(_translate("designer_window", "preferences"))

from gui.custom import TgtLine
