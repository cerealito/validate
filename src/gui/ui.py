from gui.gen import Ui_designer_window
from gui.Result_table_mdl import Result_table_mdl

from os.path import exists, basename, abspath
from FileComparator import FileComparator
from report_generators.PDFReport import PDFReport


from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

__author__ = 'saflores'

import platform

__version__ = '0.0.1'


class UI (Ui_designer_window):
    """
    This Class extends the Ui_main_window generated by QT designer so that we can
    add or modify it's behaviour without editing the generated code.
    """
    def __init__(self, main_window_p):
        super().__init__()
        self.setupUi(main_window_p)
        self.main_window = main_window_p

        self.comparision_result = None

        ###########################################################
        # connections follow
        self.btn_compare.clicked.connect(self.compare_files)

        self.action_about.triggered.connect(self.about)

        self.action_to_pdf.triggered.connect(self.export_as_pdf)

    @pyqtSlot()
    def compare_files(self):
        #self.statusbar.clearMessage()

        t = self.line_test.text()
        r = self.line_ref.text()

        if not exists(t):
            self.statusbar.showMessage('Test file does not exist')
            return

        if not exists(r):
            self.statusbar.showMessage('Reference file does not exist')
            return

        # TODO: catch exceptions/handle errors
        fc = FileComparator(t, r)

        self.comparision_result = fc.compare()

        ########## visual output to the user:
        self.lbl_result_is.setText('Overall result is:')
        if self.comparision_result.is_acceptable:
            self.lbl_result.setText('<div style="color:green;font-weight:bold;">Passed</div>')
            self.statusbar.showMessage('Files do not have significant differences :)', 5000)
        else:
            self.lbl_result.setText('<div style="color:red;font-weight:bold;">Not Passed</div>')
            self.statusbar.showMessage('Files have significant differences :(', 5000)

        self.table_view_results.setModel(Result_table_mdl(self.comparision_result))

        ########## enable pdf export:
        self.action_to_pdf.setEnabled(True)

    def export_as_pdf(self):
        out_f = str(basename(self.comparision_result.file_test))[:-4] + '.pdf'

        pdf_report = PDFReport(self.comparision_result)
        pdf_report.summary()

        self.statusbar.showMessage('generating pdf report, please wait...')

        # TODO: this guy is blocking! maybe put in a different thread?
        pdf_report.plot_results()

        pdf_report.output(out_f, 'F')

        if exists(out_f):
            self.statusbar.showMessage('Done. Output file is: ' + abspath(out_f), 10000)
            self.clear_results()
        else:
            self.statusbar.showMessage('Oops! something went wrong. Cannot continue', 10000)

    def clear_results(self):
        self.line_test.clear()
        self.line_ref.clear()
        self.lbl_result.clear()
        self.lbl_result_is.clear()
        self.action_to_pdf.setEnabled(False)
        self.comparision_result = None
        self.table_view_results.setModel(None)

    def about(self):
        """Popup a box with about message."""
        about_str = "<center><b>Validate v{0} </b></center>           " + \
                    "<p>Copyright © 2014 Samuel FLORES.               " + \
                    "All rights reserved in accordance with GPL v3</p>" + \
                    "<p>Python {1} - on {2}</p>"

        QMessageBox.about(self.main_window, "Validate",
                          about_str.format(__version__, platform.python_version(), platform.system()))

