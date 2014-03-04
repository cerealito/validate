from os.path import basename
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from Results import FileCmpResult
from report_generators.PDFReport import PDFReport

__author__ = 'saflores'


class PDFWrapper2(QThread):
    pdf_ready = pyqtSignal(object)

    def __init__(self, file_cmp_result_p: FileCmpResult, parent: QObject):
        super().__init__(parent)
        self.file_cmp_result = file_cmp_result_p

    def __del__(self):
        self.wait()

    def run(self):

        pdf_report = PDFReport(self.file_cmp_result)

        # TODO: make this configurable.
        out_f = str(basename(pdf_report.file_cmp_result.file_test))[:-4] + '.pdf'

        pdf_report.summary()

        pdf_report.plot_results()
        pdf_report.output(out_f, 'F')

        self.pdf_ready.emit(out_f)
        return
