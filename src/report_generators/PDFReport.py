from os.path import abspath, basename
from charts.generation import generate_png

__author__ = 'cerealito'

from fpdf import FPDF

class PDFReport(FPDF):

    def __init__(self, file_cmp_result):
        super().__init__(orientation='L', unit='mm', format='A4')
        # right and bottom are automatic
        self.set_margins(left=15, top=15)
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
        self.set_font('Arial', '', 6)
        # Title
        self.cell(w=0, h=5, txt=self.title, border='B', ln=0, align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 6)
        # Page number
        self.cell(w=0, h=5, txt='Page '+str(self.page_no())+'/{nb}', border=0, ln=0, align='C')

    def summary(self):
        #######################################################################
        # Big title in the first page
        self.set_y(25)
        self.set_font('Arial', 'B', 16)
        self.cell(w=0, h=10, txt=self.title, ln=1,  align='C')

        #######################################################################
        # body of the report
        self.set_font('Arial', '', 10)
        self.ln()

        #######################################################################
        # date/time of the comparison
        self.cell(w=0, h=5, txt='Date and time of comparison:', ln=1)
        self.set_font('Courier', '', 10)
        self.cell(w=0, h=5, txt='    ' + self.file_cmp_result.date.strftime('%d/%m/%Y at %H:%M'), ln=1)

        #######################################################################
        # compared files
        self.set_font('Arial', '', 10)
        self.cell(w=0, h=5, txt='Test File:', ln=1)

        self.set_font('Courier', '', 10)
        self.cell(w=0, h=5, txt='    ' + abspath(self.file_cmp_result.file_test), ln=1)

        self.set_font('Arial', '', 10)
        self.cell(w=0, h=5, txt='Reference File:', ln=1)

        self.set_font('Courier', '', 10)
        self.cell(w=0, h=5, txt='    ' + abspath(self.file_cmp_result.file_ref), ln=1)

        self.set_font('Arial', '', 10)
        self.ln()

        #######################################################################
        # Overall result of the file cmp
        line = 'The overall result is '
        self.cell(self.get_string_width(line), h=5, txt=line, ln=0)
        if self.file_cmp_result.is_acceptable:
             # GREEN
            self.set_text_color(0, 204, 0)
            self.cell(w=0, h=5, txt='Passed.', ln=1)
        else:
            # RED
            self.set_text_color(255 ,0, 0)
            self.cell(w=0, h=5, txt='Not Passed.', ln=1)
        self.ln()

        #######################################################################
        # variable table
        self.set_text_color(0, 0, 0)
        self.cell(w=0, h=5, txt='Summary of the variables compared:', ln=1)

        #######################################################################
        # header
        self.set_font('Courier', '', 10)
        self.cell(w=0, h=5, txt='{:<60} {:<}  {:<7}'.format('Variable', 'Error', 'Status'),  ln=1)

        #######################################################################
        # rows
        for r in self.file_cmp_result.result_l:
            line = '{:<60} {:.2f}%  '.format(r.test_var.name, r.error)
            self.cell(self.get_string_width(line), h=5, txt=line, ln=0)

            line = '{:<7}'.format(r.status)
            if r.status == 'ko':
                #RED
                self.set_text_color(255, 0, 0)
                self.cell(w=0, h=5, txt=line, ln=1)
            if r.status == 'warning':
                #YELLOW
                self.set_text_color(255, 157, 0)
                self.cell(w=0, h=5, txt=line, ln=1)
            if r.status == 'passed':
                # Yellowish-GREEN
                self.set_text_color(153, 204, 0)
                self.cell(w=0, h=5, txt=line, ln=1)
            if r.status == 'matched':
                # GREEN
                self.set_text_color(0, 204, 0)
                self.cell(w=0, h=5, txt=line, ln=1)
            # go back to black
            self.set_text_color(0, 0, 0)

        # for every couple of variables, generate a png
        for result in self.file_cmp_result.result_l:
            tmp_img_f = generate_png(result.test_var, result.ref_var)
            self.set_x(50)
            self.image(tmp_img_f, h=150)