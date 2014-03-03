from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from Results import FileCmpResult

__author__ = 'saflores'

class ResultTableMdl(QAbstractTableModel):

    NAME_COLUMN = 0
    ERROR_COLUMN = 1
    STATUS_COLUMN = 2

    def __init__(self, cmp_res: FileCmpResult):
        super().__init__()
        self.cmp_res = cmp_res

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.cmp_res.result_l)

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return 3

    def data(self, QModelIndex, int_role=None):
        result_couple = self.cmp_res.result_l[QModelIndex.row()]

        if int_role == Qt.DisplayRole:
            if QModelIndex.column() == ResultTableMdl.NAME_COLUMN:
                return result_couple.test_var.name
            if QModelIndex.column() == ResultTableMdl.ERROR_COLUMN:
                return '{:.3f}%'.format(result_couple.error)
            if QModelIndex.column() == ResultTableMdl.STATUS_COLUMN:
                return result_couple.status

        if int_role == Qt.ForegroundRole and QModelIndex.column() == ResultTableMdl.STATUS_COLUMN:
            color = QBrush(Qt.black)
            if result_couple.status == 'ko':
                #RED
                color = QBrush(Qt.red)
            if result_couple.status == 'warning':
                #YELLOW
                color = QBrush(QColor(255, 157, 0, 255))
            if result_couple.status == 'passed':
                # Yellowish-GREEN
                color = QBrush(QColor(153, 204, 0, 255))
            if result_couple.status == 'matched':
                # GREEN
                color = QBrush(QColor(0, 204, 0, 255))
            return color

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role == Qt.DisplayRole:
            # column headers: the name of the columns
            if Qt_Orientation == Qt.Horizontal:
                if p_int == ResultTableMdl.NAME_COLUMN:
                    return 'Variable'
                if p_int == ResultTableMdl.ERROR_COLUMN:
                    return 'Error'
                if p_int == ResultTableMdl.STATUS_COLUMN:
                    return 'Status'
            # row headers: just a number
            if Qt_Orientation == Qt.Vertical:
                return p_int + 1