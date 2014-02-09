import os
import unittest


from fpdf import FPDF
from src.FileComparator import FileComparator
from report_generators.PDFReport import PDFReport

__author__ = 'saflores'


class PdfTester(unittest.TestCase):
    #################################################################################
    def test_mini(self):
        pdf = FPDF()
        #pdf.compress = True
        pdf.add_page()
        pdf.set_font('Arial', 'B', 18)
        pdf.cell(40, 10, 'PDF TEST!', border=1, ln=1)
        pdf.cell(100, 10, 'Powered by FPDF.', border=0, ln=0, align='C')

        pdf.output('test1.pdf','F')

    def test_small(self):
        print('Comparing and graphing a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        fc = FileComparator(t, r)
        res = fc.compare()
        self.assertFalse(res.files_are_equal)

        print('\n### Overall result is: ', res.files_are_equal)
        print('generating pdf report...')
        out_f = 'test2.pdf'
        pdf_report = PDFReport(res)

        pdf_report.summary()

        for i in range(1,41):
            pdf_report.cell(0, 10, 'Printing line number ' + str(i), 0, 1)

        pdf_report.output(out_f, 'F')

        self.assertTrue(os.path.exists(out_f))


if __name__ == '__main__':
    unittest.main()