from PyQt5.QtCore import QThread, pyqtSignal
from Variable import Variable
from charts.svg import generate_svg

__author__ = 'saflores'
class SVGAsyncGenerator(QThread):
    svg_ready = pyqtSignal(object)

    def __init__(self, test_var: Variable, ref_var: Variable, tmp_dir):
        super().__init__()
        self.test_var = test_var
        self.ref_var = ref_var
        self.tmp_dir = tmp_dir

    def run(self):
        f = generate_svg(self.test_var, self.ref_var, self.tmp_dir)
        self.svg_ready.emit(f)
