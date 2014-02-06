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
        pb_list = []

        fc = FileComparator(t, r)
        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')

        # for every couple of variables with problems, generate a png
        for v_tuple in pb_list:
            test, ref = v_tuple
            self.generate_png(test, ref)

        self.assertFalse(r)



        pdf = PDFReport()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times','',12)
        for i in range(1,41):
            pdf.cell(0,10,'Printing line number '+str(i),0,1)
        pdf.output('test2.pdf','F')

if __name__ == '__main__':
    unittest.main()