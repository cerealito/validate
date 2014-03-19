from PyQt5.QtCore import QAbstractTableModel, QSortFilterProxyModel, QModelIndex
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from Results import FileCmpResult, ResultCouple

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
            if result_couple.status == ResultCouple.STS_KO:
                #RED
                color = QBrush(Qt.red)
            if result_couple.status == ResultCouple.STS_WARN:
                #YELLOW
                color = QBrush(QColor(255, 157, 0, 255))
            if result_couple.status == ResultCouple.STS_PASS:
                # Yellowish-GREEN
                color = QBrush(QColor(153, 204, 0, 255))
            if result_couple.status == ResultCouple.STS_MATCH:
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


########################################################################################################################
class StatusSortingProxyModel(QSortFilterProxyModel):
    def lessThan(self, first: QModelIndex, second: QModelIndex):
        """
        Returns true if the value of the item referred to by the given index 'first'
        is less than the value of the item referred to by the given index 'second',
        otherwise returns false.
        """
        first_data = self.sourceModel().data(first, Qt.DisplayRole)
        second_data = self.sourceModel().data(second, Qt.DisplayRole)

        if first.column() == ResultTableMdl.STATUS_COLUMN:
            if first_data == ResultCouple.STS_KO:
                if second_data in [ResultCouple.STS_WARN, ResultCouple.STS_PASS, ResultCouple.STS_MATCH]:
                    return True
            if first_data == ResultCouple.STS_WARN:
                if second_data in [ResultCouple.STS_PASS, ResultCouple.STS_MATCH]:
                    return True
            if first_data == ResultCouple.STS_PASS:
                if second_data in [ResultCouple.STS_MATCH]:
                    return True

            # in any other case
            return False
        else:
            # keep the usual order if user is not ordering by status
            return super().lessThan(first, second)
