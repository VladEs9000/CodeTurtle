import sys
import csv
import datetime
from Roma import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chek = False
        self.login_array = []
        self.data_array = []
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.OpenFile.clicked.connect(self.OpenFile)
        self.ui.AnalizFile.clicked.connect(self.Analyze)
        self.ui.serchLogin.clicked.connect(self.serch_Login)
        self.ui.serchData.clicked.connect(self.search_Data)
        self.ui.saveData.clicked.connect(self.save_Data)

    def OpenFile(self):
        fileD = QtWidgets.QFileDialog()
        open_file = fileD.getOpenFileName(self, filter="Файл Microsoft Excel (*.csv)")
        self.ui.PathFile.setText('')
        path = open_file[0]
        self.ui.PathFile.setText(path)

    def Analyze(self):
        self.ui.tableWidget.setRowCount(0)
        self.path_file = self.ui.PathFile.text()
        if self.path_file == '':
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Введите путь')
            return 1
        format_file = self.path_file.split('.')
        format = format_file[len(format_file) - 1]
        if format != 'csv':
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Неверный формат')
            self.ui.PathFile.setText('')
        else:
            with open(self.path_file, 'r')as csv_file:
                reader = csv.reader(csv_file)  
                data = list(reader)
            miim = 0
            maam = len(data) - 2
            id = self.ui.comboBox.currentIndex()
            count_box = self.ui.comboBox.count()
            for i in range(1, count_box):
                if id == i:
                    miim = (i - 1) * 100
                    maam = i * 100 - 1
            ost = len(data) % 100
            count_id = len(data) - ost
            count_id = int(count_id / 100)
            if self.data_array != []:
                self.data_array.clear()
            if self.data_array != []:
                self.login_array.clear()
            self.ui.tableWidget.setHorizontalHeaderLabels(data[0])
            self.ui.progressBar.setMaximum(len(data))
            value = 0
            for i, row in enumerate(data[1:]):
                value += 1
                self.ui.progressBar.setValue(value)
                if miim <= i <= maam:
                    self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                    for j, v in enumerate(row):
                        if j == 0:
                            self.data_array.append(v)
                        elif j == 3:
                            self.login_array.append(v)
                        it = QtWidgets.QTableWidgetItem()
                        it.setData(QtCore.Qt.DisplayRole, v)
                        self.ui.tableWidget.setItem((i - miim), j, it)
            c = self.ui.comboBox.count()
            if c > 1:
                self.ui.comboBox.clear()
                self.ui.comboBox.addItem("Все элементы")
            for i in range(count_id):
                self.ui.comboBox.addItem("{0} - ая сотня элементов".format(i + 1))
            self.ui.comboBox.addItem("Последние элементы")
            self.ui.progressBar.setValue(value + 1)
            self.ui.progressBar.setValue(0)
            self.chek = True

    def search_Login(self):
        if self.data_array != []:
            self.data_array.clear()
        if self.chek:
            login, ok = QtWidgets.QInputDialog.getText(self, "Ввод логина",
                                                       "Введите логин для поиска:", QtWidgets.QLineEdit.Normal,
                                                       '')
            if ok and login:
                if login in self.login_array:
                    self.login_array.clear()
                    self.ui.tableWidget.setRowCount(0)
                    with open(self.path_file, 'r')as csv_file:
                        reader = csv.reader(csv_file)  
                        data = list(reader)
                        self.ui.tableWidget.setHorizontalHeaderLabels(data[0])
                        self.ui.progressBar.setMaximum(len(data))
                        p = 0
                        value = 0
                        for i, row in enumerate(data[1:]):
                            value += 1
                            self.ui.progressBar.setValue(value)
                            if login in row:
                                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                                for j, v in enumerate(row):
                                    if j == 0:
                                        self.data_array.append(v)
                                    it = QtWidgets.QTableWidgetItem()
                                    it.setData(QtCore.Qt.DisplayRole, v)
                                    self.ui.tableWidget.setItem(p, j, it)
                                p += 1
                        self.ui.progressBar.setValue(value + 1)
                        self.ui.progressBar.setValue(0)
                else:
                    QtWidgets.QMessageBox.about(self, 'Ошибка', 'Логина не найдено.')
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Введите логин.')
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')

    def serch_Data(self):
        if self.login_array != []:
            self.login_array.clear()
        if self.chek:
            enter = self.ui.dateTimeEdit.text()
            enter = enter.split(' ')
            age = enter[0]
            clock = enter[1]
            age = age.split('.')
            clock = clock.split(':')
            unix_time = datetime.datetime(int(age[2]), int(age[1]), int(age[0]), int(clock[0]), int(clock[1]),
                                          int(clock[2])).timestamp()
            unix_time = int(unix_time)
            unix_time += 36000
            unix_time = str(unix_time)
            if unix_time in self.data_array:
                self.data_array.clear()
                self.ui.tableWidget.setRowCount(0)
                with open(self.path_file, 'r')as csv_file:
                    reader = csv.reader(csv_file)  
                    file_data = list(reader)
                    self.ui.tableWidget.setHorizontalHeaderLabels(file_data[0])
                    self.ui.progressBar.setMaximum(len(file_data))
                    p = 0
                    value = 0
                    for i, row in enumerate(file_data[1:]):
                        value += 1
                        self.ui.progressBar.setValue(value)
                        if unix_time == row[0]:
                            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                            for j, v in enumerate(row):
                                if j == 3:
                                    self.login_array.append(v)
                                it = QtWidgets.QTableWidgetItem()
                                it.setData(QtCore.Qt.DisplayRole, v)
                                self.ui.tableWidget.setItem(p, j, it)
                            p += 1

                    self.ui.progressBar.setValue(value + 1)
                    self.ui.progressBar.setValue(0)
                pass
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Дата не найдена')
        else:
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл')

    def save_Data(self):
        header = ['begin', 'end', 'time interval', 'login', 'mac ab', 'ULSK1', 'BRAS ip', 'start count', 'alive count',
                  'stop count', 'incoming', 'outcoming', 'error_count', 'code 0', 'code 1011', 'code 1100', 'code -3',
                  'code -52', 'code -42', 'code -21', 'code -40', ' code -44', 'code -46', ' code -38']
        rowCount = self.ui.tableWidget.rowCount()
        columCount = 24
        d = QtWidgets.QFileDialog.getSaveFileName(self, "Choose a filename to save under", "/data_save",
                                                  "Файл Microsoft Excel (*.csv)")
        if d[0] == '':
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Вы отменили сохранение')
            return 1
        self.ui.progressBar.setMaximum(rowCount)
        value = 0
        with open(d[0], 'w', newline='') as file_csv:
            writher = csv.writer(file_csv)
            writher.writerow(header)
            for i in range(rowCount):
                save = []
                value += 1
                self.ui.progressBar.setValue(value)
                for j in range(columCount):
                    p = self.ui.tableWidget.item(i, j).text()
                    save.append(p)
                writher.writerow(save)
        self.ui.progressBar.setValue(value + 1)
        self.ui.progressBar.setValue(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
