from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from Results import FileCmpResult

__author__ = 'saflores'

class Result_table_mdl(QAbstractTableModel):

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
            if QModelIndex.column() == 0:
                return result_couple.test_var.name
            if QModelIndex.column() == 1:
                return '{:.3f}%'.format(result_couple.error)
            if QModelIndex.column() == 2:
                return result_couple.status

        # TODO: fix this, it does not work :P
        if int_role == Qt.FontRole:
            color = QBrush(Qt.black)
            if result_couple.status == 'ko':
                #RED
                color = QBrush(Qt.red)
            if result_couple.status == 'warning':
                #YELLOW
                color = QBrush(Qt.darkYellow)
            if result_couple.status == 'passed':
                # Yellowish-GREEN
                color = QBrush(Qt.green)
            if result_couple.status == 'matched':
                # GREEN
                color = QBrush(Qt.darkGreen)
            return color

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role == Qt.DisplayRole:
            if Qt_Orientation == Qt.Horizontal:
                if p_int == 0:
                    return 'Variable'
                if p_int == 1:
                    return 'Error'
                if p_int == 2:
                    return 'Status'
            if Qt_Orientation == Qt.Vertical:
                return p_int + 1