# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Mar 14 16:59:00 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_designer_window(object):
    def setupUi(self, designer_window):
        designer_window.setObjectName("designer_window")
        designer_window.resize(650, 266)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(designer_window.sizePolicy().hasHeightForWidth())
        designer_window.setSizePolicy(sizePolicy)
        self.central_widget = QtWidgets.QWidget(designer_window)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_ref = QtWidgets.QLabel(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ref.sizePolicy().hasHeightForWidth())
        self.lbl_ref.setSizePolicy(sizePolicy)
        self.lbl_ref.setObjectName("lbl_ref")
        self.gridLayout.addWidget(self.lbl_ref, 1, 0, 1, 1)
        self.btn_browse_test = QtWidgets.QPushButton(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse_test.sizePolicy().hasHeightForWidth())
        self.btn_browse_test.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gui/icons/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_browse_test.setIcon(icon)
        self.btn_browse_test.setObjectName("btn_browse_test")
        self.gridLayout.addWidget(self.btn_browse_test, 0, 5, 1, 1)
        self.line_test = TgtLine(self.central_widget)
        self.line_test.setObjectName("line_test")
        self.gridLayout.addWidget(self.line_test, 0, 1, 1, 4)
        self.lbl_test = QtWidgets.QLabel(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_test.sizePolicy().hasHeightForWidth())
        self.lbl_test.setSizePolicy(sizePolicy)
        self.lbl_test.setObjectName("lbl_test")
        self.gridLayout.addWidget(self.lbl_test, 0, 0, 1, 1)
        self.line_ref = TgtLine(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_ref.sizePolicy().hasHeightForWidth())
        self.line_ref.setSizePolicy(sizePolicy)
        self.line_ref.setObjectName("line_ref")
        self.gridLayout.addWidget(self.line_ref, 1, 1, 1, 4)
        self.btn_browse_ref = QtWidgets.QPushButton(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse_ref.sizePolicy().hasHeightForWidth())
        self.btn_browse_ref.setSizePolicy(sizePolicy)
        self.btn_browse_ref.setIcon(icon)
        self.btn_browse_ref.setObjectName("btn_browse_ref")
        self.gridLayout.addWidget(self.btn_browse_ref, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 5)
        self.btn_compare = QtWidgets.QPushButton(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_compare.sizePolicy().hasHeightForWidth())
        self.btn_compare.setSizePolicy(sizePolicy)
        self.btn_compare.setObjectName("btn_compare")
        self.gridLayout.addWidget(self.btn_compare, 2, 5, 1, 1)
        self.lbl_result_is = QtWidgets.QLabel(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_result_is.sizePolicy().hasHeightForWidth())
        self.lbl_result_is.setSizePolicy(sizePolicy)
        self.lbl_result_is.setObjectName("lbl_result_is")
        self.gridLayout.addWidget(self.lbl_result_is, 3, 0, 1, 2)
        self.lbl_result = QtWidgets.QLabel(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_result.sizePolicy().hasHeightForWidth())
        self.lbl_result.setSizePolicy(sizePolicy)
        self.lbl_result.setObjectName("lbl_result")
        self.gridLayout.addWidget(self.lbl_result, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 2)
        self.table_view_results = QtWidgets.QTableView(self.central_widget)
        self.table_view_results.setEnabled(True)
        self.table_view_results.setFrameShape(QtWidgets.QFrame.Box)
        self.table_view_results.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_view_results.setAlternatingRowColors(True)
        self.table_view_results.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_view_results.setGridStyle(QtCore.Qt.DashLine)
        self.table_view_results.setObjectName("table_view_results")
        self.table_view_results.horizontalHeader().setHighlightSections(False)
        self.table_view_results.horizontalHeader().setStretchLastSection(True)
        self.table_view_results.verticalHeader().setHighlightSections(False)
        self.table_view_results.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.table_view_results, 4, 0, 1, 6)
        designer_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(designer_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 18))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_validate = QtWidgets.QMenu(self.menubar)
        self.menu_validate.setObjectName("menu_validate")
        designer_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(designer_window)
        self.statusbar.setObjectName("statusbar")
        designer_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(designer_window)
        self.toolBar.setObjectName("toolBar")
        designer_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_about = QtWidgets.QAction(designer_window)
        self.action_about.setObjectName("action_about")
        self.action_to_pdf = QtWidgets.QAction(designer_window)
        self.action_to_pdf.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/gui/icons/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_to_pdf.setIcon(icon1)
        self.action_to_pdf.setObjectName("action_to_pdf")
        self.action_clear_all = QtWidgets.QAction(designer_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/gui/icons/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clear_all.setIcon(icon2)
        self.action_clear_all.setObjectName("action_clear_all")
        self.action_quit = QtWidgets.QAction(designer_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/gui/icons/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon3)
        self.action_quit.setObjectName("action_quit")
        self.menu_help.addAction(self.action_about)
        self.menu_validate.addAction(self.action_to_pdf)
        self.menu_validate.addAction(self.action_clear_all)
        self.menu_validate.addAction(self.action_quit)
        self.menubar.addAction(self.menu_validate.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolBar.addAction(self.action_to_pdf)
        self.toolBar.addAction(self.action_clear_all)
        self.toolBar.addAction(self.action_quit)

        self.retranslateUi(designer_window)
        QtCore.QMetaObject.connectSlotsByName(designer_window)
        designer_window.setTabOrder(self.line_test, self.line_ref)
        designer_window.setTabOrder(self.line_ref, self.table_view_results)

    def retranslateUi(self, designer_window):
        _translate = QtCore.QCoreApplication.translate
        designer_window.setWindowTitle(_translate("designer_window", "Validate"))
        self.lbl_ref.setText(_translate("designer_window", "Ref:"))
        self.btn_browse_test.setText(_translate("designer_window", "Browse ..."))
        self.lbl_test.setText(_translate("designer_window", "Test:"))
        self.btn_browse_ref.setText(_translate("designer_window", "Browse ..."))
        self.btn_compare.setText(_translate("designer_window", "Compare"))
        self.lbl_result_is.setText(_translate("designer_window", "Overall result is:"))
        self.lbl_result.setText(_translate("designer_window", "Not Passed"))
        self.menu_help.setTitle(_translate("designer_window", "Help"))
        self.menu_validate.setTitle(_translate("designer_window", "Validate"))
        self.toolBar.setWindowTitle(_translate("designer_window", "toolBar"))
        self.action_about.setText(_translate("designer_window", "About"))
        self.action_to_pdf.setText(_translate("designer_window", "Export as PDF"))
        self.action_to_pdf.setToolTip(_translate("designer_window", "Export the current comparision as a PDF file"))
        self.action_to_pdf.setShortcut(_translate("designer_window", "Ctrl+S"))
        self.action_clear_all.setText(_translate("designer_window", "Clear"))
        self.action_quit.setText(_translate("designer_window", "Quit"))
        self.action_quit.setToolTip(_translate("designer_window", "Exit the application"))

from gui.custom import TgtLine
import icons_rc
