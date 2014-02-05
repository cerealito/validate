import unittest


from fpdf import FPDF

__author__ = 'saflores'


class PdfTester(unittest.TestCase):
    #################################################################################
    def test_mini(self):
        pdf=FPDF()
        pdf.compress = True
        pdf.add_page()
        pdf.set_font('Arial','B',16)
        pdf.cell(40,10,'Hello World!')
        pdf.output('test1.pdf','F')

if __name__ == '__main__':
    unittest.main()