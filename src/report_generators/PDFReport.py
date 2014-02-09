__author__ = 'cerealito'

from fpdf import FPDF

class PDFReport(FPDF):

    def __init__(self, result_summary):
        super().__init__()
        self.r_summary = result_summary
        self.title = 'untitled'

        self.alias_nb_pages()
        self.add_page()
        self.set_font('Arial', '', 12)

    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 10)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30,10, self.title , 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial','I',8)
        # Page number
        self.cell(0, 10, 'Page '+str(self.page_no())+'/{nb}',0,0,'C')

    def summary(self):

        self.multi_cell(w=0, h=5, txt='Test report for files:', border=0)

        self.cell(w=0, h=5, txt=self.r_summary.file_test, border=0, ln=1)
        self.cell(w=0, h=5, txt=self.r_summary.file_ref, border=0, ln=1)

        self.cell(w=0, h=5, txt='Over all result is ' + str(self.r_summary.files_are_equal), border=0, ln=1)
        for r in self.r_summary.result_l:
            self.cell(w=0, h=5, txt=str(r), border=0, ln=1)