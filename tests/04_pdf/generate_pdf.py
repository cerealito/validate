import unittest


from fpdf import FPDF
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

    def test_maxi(self):
        pdf = PDFReport()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times','',12)
        for i in range(1,41):
                pdf.cell(0,10,'Printing line number '+str(i),0,1)
        pdf.output('test2.pdf','F')

if __name__ == '__main__':
    unittest.main()