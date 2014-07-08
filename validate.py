#!/usr/bin/env python
if __name__ == '__main__':
    # explicitly append the ./src directory to the current path.
    # PyCharm does this implicitly but it is better to have it explicit
    # this makes the tool work the same in tests and in CLI
    import sys
    import inspect
    from os.path import dirname, abspath, join, exists
    #when in CLI use inspect to locate the source directory
    src_dir = join(dirname(abspath(inspect.getfile(inspect.currentframe()))), 'src')
    sys.path.append(src_dir)

__author__ = 'saflores'


from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from gui.ui import UI
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

##### check if settings exist, otherwise initialize them #####
mySettings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'Sogeti', 'validate')

if not exists(mySettings.fileName()):
    mySettings.setValue("report/imageQuality", 120)
    mySettings.sync()
    print("settings written to " + mySettings.fileName())
##############################################################

ui = UI(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
