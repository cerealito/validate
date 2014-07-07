# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Mon Jul  7 15:48:47 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preferences(object):
    def setupUi(self, preferences):
        preferences.setObjectName("preferences")
        preferences.resize(400, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(preferences.sizePolicy().hasHeightForWidth())
        preferences.setSizePolicy(sizePolicy)
        preferences.setMinimumSize(QtCore.QSize(400, 120))
        preferences.setMaximumSize(QtCore.QSize(400, 120))
        self.buttonBox = QtWidgets.QDialogButtonBox(preferences)
        self.buttonBox.setGeometry(QtCore.QRect(10, 80, 381, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.splitter_2 = QtWidgets.QSplitter(preferences)
        self.splitter_2.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lbl_quality = QtWidgets.QLabel(self.splitter)
        self.lbl_quality.setObjectName("lbl_quality")
        self.spinBox = QtWidgets.QSpinBox(self.splitter)
        self.spinBox.setMinimum(70)
        self.spinBox.setMaximum(400)
        self.spinBox.setSingleStep(10)
        self.spinBox.setProperty("value", 120)
        self.spinBox.setObjectName("spinBox")
        self.lbl_quality_help = QtWidgets.QLabel(self.splitter_2)
        self.lbl_quality_help.setStyleSheet("color: rgb(0, 85, 255);")
        self.lbl_quality_help.setObjectName("lbl_quality_help")

        self.retranslateUi(preferences)
        self.buttonBox.accepted.connect(preferences.accept)
        self.buttonBox.rejected.connect(preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(preferences)

    def retranslateUi(self, preferences):
        _translate = QtCore.QCoreApplication.translate
        preferences.setWindowTitle(_translate("preferences", "Validate Preferences"))
        self.lbl_quality.setText(_translate("preferences", "Output graphics quality"))
        self.lbl_quality_help.setText(_translate("preferences", "Use a low quality value for faster PDF generation"))

