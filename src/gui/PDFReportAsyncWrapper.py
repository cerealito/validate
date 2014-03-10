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
        self.out_f = None

    def set_output_f(self, out_f):
        self.out_f = out_f

    def set_pdf_report(self, pdf_report_p: PDFReport):
        self.pdf_report = pdf_report_p

    @pyqtSlot()
    def synchronous_pdf_generation(self):
        self.pdf_report.summary()

        self.pdf_report.plot_results()
        self.pdf_report.output(self.out_f, 'F')

        # move this object back to the main thread, were it was originally created
        self.moveToThread(QtGui.QGuiApplication.instance().thread())
        self.pdf_ready.emit(self.out_f)

