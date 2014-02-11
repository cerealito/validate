from os.path import abspath, basename
from charts.generation import generate_png

__author__ = 'cerealito'

from fpdf import FPDF

class PDFReport(FPDF):

    def __init__(self, file_cmp_result):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.file_cmp_result = file_cmp_result
        self.title = 'Validation Report for ' + basename(file_cmp_result.file_test)

        self.alias_nb_pages()
        self.add_page()
        self.set_font('Arial', '', 12)

    def header(self):
        # no header for page 1
        if self.page_no() == 1:
            return

        # Arial bold 15
        self.set_font('Arial', 'B', 6)
        # Title
        self.cell(w=190, h=5, txt=self.title, border='B', ln=0, align='C')
        # Line break
        self.ln(20)


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial','I',8)
        # Page number
        self.cell(0, 10, 'Page '+str(self.page_no())+'/{nb}', 0, 0, 'C')

    def summary(self):
        #######################################################################
        # Big title in the first page
        self.set_y(30)
        self.set_font('Arial', 'B', 18)
        self.cell(w=190, h=10, txt=self.title, ln=1, border=0, align='C')

        #######################################################################
        # body of the report
        self.set_font('Arial', 'B', 12)
        self.ln()
        self.ln()
        self.multi_cell(w=0, h=5, txt='Validation report for files:', border=0)
        self.ln()
        self.cell(w=0, h=5, txt=abspath(self.file_cmp_result.file_test), border=0, ln=1)
        self.cell(w=0, h=5, txt=abspath(self.file_cmp_result.file_ref), border=0, ln=1)
        self.ln()

        self.cell(w=0, h=5, txt='Over all result is ' + str(self.file_cmp_result.files_are_equal), border=0, ln=1)
        self.ln()

        self.cell(w=0, h=5, txt='The following variables were compared:', border=0, ln=1)
        self.set_font('Courier', 'B', 12)
        self.cell(w=0, h=5, txt='{:<60} {:>}'.format('Variable', 'Error'), border=0, ln=1)
        for r in self.file_cmp_result.result_l:
            self.cell(w=0, h=5, txt=str(r), border=0, ln=1)

        # for every couple of variables, generate a png
        for result in self.file_cmp_result.result_l:
            tmp_img_f = generate_png(result.test_var, result.ref_var)
            self.image(tmp_img_f, w=190 )