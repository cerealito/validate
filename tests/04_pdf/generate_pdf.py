import os
import unittest

from fpdf import FPDF
from AsyncFileComparator import AsyncFileComparator
from report_generators.PDFReport import PDFReport

__author__ = 'saflores'


class PdfTester(unittest.TestCase):
    def setUp(self):
        try:
            os.remove('big.pdf')
            os.remove('small.pdf')
            os.remove('mini.pdf')
        except FileNotFoundError:
            pass
    #################################################################################
    def test_mini(self):
        pdf = FPDF()
        #pdf.compress = True
        pdf.add_page()
        pdf.set_font('Arial', 'B', 18)
        pdf.cell(40, 10, 'PDF TEST!', border=1, ln=1)
        pdf.cell(100, 10, 'Powered by FPDF.', border=0, ln=0, align='C')

        pdf.output('mini.pdf','F')

    def test_small(self):
        print('Comparing and graphing a mini error')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        fc = AsyncFileComparator(t, r)
        res = fc.compare()
        self.assertFalse(res.is_acceptable)

        print('\n### Overall result is: ', res.is_acceptable)
        print('generating pdf report...')
        out_f = 'small.pdf'
        pdf_report = PDFReport(res)

        pdf_report.summary()
        pdf_report.plot_results()

        pdf_report.output(out_f, 'F')

        self.assertTrue(os.path.exists(out_f))

    def test_big(self):
        print('Comparing and graphing a mini error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        fc = AsyncFileComparator(t, r)
        res = fc.compare()
        self.assertTrue(res.is_acceptable)

        print('\n### Overall result is: ', res.is_acceptable)
        print('generating pdf report...')
        out_f = 'big.pdf'
        pdf_report = PDFReport(res)

        pdf_report.summary()
        pdf_report.plot_results()

        pdf_report.output(out_f, 'F')

        self.assertTrue(os.path.exists(out_f))

if __name__ == '__main__':
    unittest.main()