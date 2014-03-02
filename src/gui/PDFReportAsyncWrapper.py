from os.path import basename
from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from report_generators import PDFReport

__author__ = 'saflores'

class PDFReportAsyncWrapper(QObject):
    # This is very strange for me as (an occasional) Python programmer.
    # We must pass a class as an argument (like telling the type of it)
    # I have found that object <built-in> does a good job here.
    pdf_ready = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
        # we declare this here and then set it.
        # for some weird reason i couldn't just pass it to the constructor...!
        self.pdf_report = None

    def set_pdf_report(self, pdf_report_p: PDFReport):
        self.pdf_report = pdf_report_p

    @pyqtSlot()
    def synchronous_pdf_generation(self):
        # TODO: make this configurable
        out_f = str(basename(self.pdf_report.file_cmp_result.file_test))[:-4] + '.pdf'

        self.pdf_report.summary()

        self.pdf_report.plot_results()
        self.pdf_report.output(out_f, 'F')

        # move this object back to the main thread, were it was originally created
        self.moveToThread(QtGui.QGuiApplication.instance().thread())
        self.pdf_ready.emit(out_f)

