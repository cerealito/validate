__author__ = 'saflores'

from PyQt5 import QtCore
from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import QLineEdit


class TgtLine(QLineEdit):
    def __init__(self, *args):
        super().__init__(*args)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # we need to accept the proposed action or change it.
        # otherwise dropEvent() won't be called.
        # accept only if there is a copy...
        if event.proposedAction() == QtCore.Qt.CopyAction:
            event.acceptProposedAction()

    # the ': Type' is a python3 annotation. This helps IDEs to guess the parameter type!
    # can also be achieved with @type in the docstring...
    def dropEvent(self, event: QDropEvent):

        if event.mimeData().hasUrls():
            str_p = event.mimeData().urls()[0].toLocalFile()
            print(str_p)
            self.setText(str_p)
