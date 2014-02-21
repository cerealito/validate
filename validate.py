#!/usr/bin/env python
if __name__ == '__main__':
    # explicitly append the ./src directory to the current path.
    # PyCharm does this implicitly but it is better to have it explicit
    # this makes the tool work the same in tests and in CLI
    import sys
    import inspect
    from os.path import dirname, abspath, join
    #when in CLI use inspect to locate the source directory
    src_dir = join(dirname(abspath(inspect.getfile(inspect.currentframe()))), 'src')
    sys.path.append(src_dir)

__author__ = 'saflores'


from PyQt5 import QtWidgets
from gui.Ui_MainWindow import Ui_MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setup_ui(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

