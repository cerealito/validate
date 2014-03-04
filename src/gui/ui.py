from PyQt5 import QtWidgets
from os.path import exists, abspath

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QThread, QModelIndex
from Results import FileCmpResult
from charts.generation import show
from gui.FileComparatorAsyncWrapper import FileComparatorAsyncWrapper
from gui.PDFReportAsyncWrapper import PDFReportAsyncWrapper
from gui.PDFWrapper2 import PDFWrapper2
from gui.ResultTableMdl import ResultTableMdl

from gui.gen import Ui_designer_window
from report_generators.PDFReport import PDFReport


__author__ = 'saflores'

import platform

__version__ = '0.0.1'


class UI (Ui_designer_window):
    """
    This Class extends the Ui_main_window generated by QT designer so that we can
    add or modify it's behaviour without editing the generated code.
    """
    ####################################################################################################################
    def __init__(self, main_window_p):
        super().__init__()
        self.setupUi(main_window_p)
        self.main_window = main_window_p

        self.comparision_result = None
        self.cmp_thread = None
        self.pdf_t = None

        self.fc_wrapper = FileComparatorAsyncWrapper()

        self.table_view_results.hide()
        self.lbl_result_is.hide()
        # add an expanding vertical spacer at the bottom
        self.spacer_v_btm = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                  QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacer_v_btm, 6, 0, 1, 1)

        ###########################################################
        # connections follow reminder: signal.connect(slot)
        # main button
        self.btn_compare.clicked.connect(self.start_comparision)

        # do something upon arrival of results
        self.fc_wrapper.result_ready.connect(self.handle_result)

        # do something on extra thread errors:
        self.fc_wrapper.sig_error_ocurred.connect(self.handle_input_error)

        # actions in our menu
        self.action_about.triggered.connect(self.about)
        self.action_to_pdf.triggered.connect(self.start_pdf_generation)
        self.action_clear_all.triggered.connect(self.clear_all)

        # what to do on result selection
        self.table_view_results.doubleClicked.connect(self.start_graph)

    ####################################################################################################################
    def start_graph(self, selected: QModelIndex):
        result_couple = self.comparision_result.result_l[selected.row()]
        # show will automatically spawn a separate thread, so there is no need to
        # wrap it as the comparison or the pdf generation. OTOH we need to disable the main window
        # in order not to call show again, that will mess everything up (see matplotlib doc)
        self.main_window.setEnabled(False)
        show(result_couple.test_var, result_couple.ref_var)
        self.main_window.setEnabled(True)

    ####################################################################################################################
    @pyqtSlot()
    def start_comparision(self):
        # disable the use of the button while comparing
        self.btn_compare.setEnabled(False)
        self.clear_results()

        t = self.line_test.text()
        r = self.line_ref.text()

        ########## Some Error Handling:
        if not exists(t):
            self.handle_input_error('Test file does not exist')
            return

        if not exists(r):
            self.handle_input_error('Reference file does not exist')
            return

        self.fc_wrapper.set_files_to_compare(t, r)

        # we can now put the wrapper in a separate thread
        self.cmp_thread = QThread()
        self.fc_wrapper.moveToThread(self.cmp_thread)
        # the code above will fail the second time because the fc_wrapper will live in the cmp_thread.
        # we can only "push" objects from the current thread.
        # the solution is to move it back at the end of the cmp_thread

        # tell the thread what to do when started and when finished; then go!
        self.cmp_thread.started.connect(self.fc_wrapper.synchronous_compare)
        self.cmp_thread.finished.connect(self.cmp_thread.deleteLater)

        self.cmp_thread.start()

        self.statusbar.showMessage('Comparing...')
        # nothing else to do here, handle result will be called when our thread emits a signal

    ####################################################################################################################
    def start_pdf_generation(self):
        self.statusbar.showMessage('generating pdf report, please wait...')
        # disable further pdf exports until this one finishes
        self.action_to_pdf.setEnabled(False)

        self.pdf_t = PDFWrapper2(self.comparision_result, self.main_window)
        self.pdf_t.pdf_ready.connect(self.handle_pdf)

        self.pdf_t.start()

    ####################################################################################################################
    @pyqtSlot()
    def handle_result(self, res: FileCmpResult):
        self.statusbar.showMessage('Done')
        self.comparision_result = res

        # Make the results table view visible:
        self.table_view_results.show()

        ########## output to the user:
        self.lbl_result_is.show()

        if self.comparision_result.is_acceptable:
            self.lbl_result.setText('<div style="color:green;font-weight:bold;">Passed</div>')
            self.statusbar.showMessage('Files do not have significant differences :)', 5000)
        else:
            self.lbl_result.setText('<div style="color:red;font-weight:bold;">Not Passed</div>')
            self.statusbar.showMessage('Files have significant differences :(', 5000)

        # create a Result_table_model with the results and associate it with the view.
        # it should show up immediately
        self.table_view_results.setModel(ResultTableMdl(self.comparision_result))
        self.table_view_results.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        ########## enable pdf export:
        self.action_to_pdf.setEnabled(True)
        ########## re-enable cmp button:
        self.btn_compare.setEnabled(True)


    ####################################################################################################################
    @pyqtSlot()
    def handle_pdf(self, out_f):
        if exists(out_f):
            self.statusbar.showMessage('Done. Output file is: ' + abspath(out_f), 10000)
            self.clear_all()
        else:
            self.statusbar.showMessage('Oops! something went wrong. Cannot continue', 10000)

        self.pdf_t = None

    ####################################################################################################################
    def handle_input_error(self, message):
        self.clear_results()
        self.statusbar.showMessage(message)
        self.btn_compare.setEnabled(True)

    ####################################################################################################################
    def clear_results(self):
        self.lbl_result.clear()
        self.lbl_result_is.hide()
        self.action_to_pdf.setEnabled(False)
        self.comparision_result = None
        self.table_view_results.setModel(None)
        self.table_view_results.hide()

    ####################################################################################################################
    def clear_all(self):
        self.line_test.clear()
        self.line_ref.clear()
        self.clear_results()

    ####################################################################################################################
    def about(self):
        """Popup a box with about message."""
        about_str = "<center><b>Validate v{0} </b></center>           " + \
                    "<p>Copyright © 2014 Samuel FLORES.               " + \
                    "All rights reserved in accordance with GPL v3</p>" + \
                    "<p>Python {1} - on {2}</p>"

        QMessageBox.about(self.main_window, "Validate",
                          about_str.format(__version__, platform.python_version(), platform.system()))

