import sys
import json
import pymongo
import os
import timeit
import multiprocessing as mlp
from PySide2 import QtCore, QtWidgets, QtGui
from DateBase_UI import Ui_MainWindow

client = pymongo.MongoClient('localhost', 27017)
db = client['DateBase']  # Название базы данных
coll = db['Row']  # Название колекции в базе данных
coll.create_index('Nick')
coll.create_index('Phone')
coll.create_index('Surname')


def CreateDick(num, name, fname, phone, uid, nick, wo):
    return {
        'Number': num,
        'Name': name,
        'Surname': fname,
        'Phone': phone,
        'UID': uid,
        'Nick': nick,
        'WO': wo
    }


def UpdateData(id, update_data):
    coll.update_one(id, {'$set': update_data})


def LoadData(collection, data_dict):
    return collection.insert_one(data_dict).inserted_id


def FoundData(collection, elem_dict, combo_mult=0, limit=100):
    return collection.find(elem_dict).skip(combo_mult * 100).limit(limit)


def DeleteData(collection, id):
    collection.delete_one(id)


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ###
        self.ui.actionOpen.setShortcut('Ctrl+O')
        self.ui.actionOpen.triggered.connect(self.OpenData)  # Открытие файла с данными и загрузка их в дб
        ###
        self.ui.actionSave.setShortcut('Ctrl+S')
        self.ui.actionSave.triggered.connect(self.SaveData)  # Сохранение посикового запроса по дб
        ###
        self.ui.actionLoad.setShortcut('Ctrl+L')
        self.ui.actionLoad.triggered.connect(self.LoadData)  # Загрузка поискового запроса по дб
        ###
        self.ui.actionEnter_row.setShortcut('Ctrl+A')
        self.ui.actionEnter_row.triggered.connect(
            self.ClearRow_forEnter)  # Создание пустой строки для заполнения информацией
        self.ui.actionSave_row.setShortcut('Ctrl+D')
        self.ui.actionSave_row.triggered.connect(self.SaveRow_inDB)  # Занисение одной пустой строки в базу данных
        self.ui.actionSave_row.setDisabled(True)
        ###
        self.ui.actionRemove_data_row.setShortcut('Ctrl+R')
        self.ui.actionRemove_data_row.triggered.connect(self.DeletData)  # Удаление одного документа из дб
        ###
        self.ui.actionUpdate_data.setShortcut('Ctrl+U')
        self.ui.actionUpdate_data.triggered.connect(self.Update_Data)  # Обновление данных
        ###
        self.ui.actionHelp.setShortcut('Ctrl+H')
        self.ui.actionHelp.triggered.connect(self.HelpButt)  # Подсказки
        ###
        self.label = self.ui.Label_SearchBy
        self.elem_for_search = False
        self.id_array = []
        self.status = self.ui.statusBar
        ###
        self.ui.actionSearch_by_Nickname.setShortcut('Ctrl+1')
        self.ui.actionSearch_by_Nickname.triggered.connect(self.SearchByNickname)
        self.ui.actionSearc_by_Phone_number.setShortcut('Ctrl+2')
        self.ui.actionSearc_by_Phone_number.triggered.connect(self.SearchByPhonenumber)
        self.ui.actionSearch_by_Surname.setShortcut('Ctrl+3')
        self.ui.actionSearch_by_Surname.triggered.connect(self.SearchBySurname)
        ###
        self.ui.SearchBut.clicked.connect(self.Search)

    def OpenData(self):
        open_file_data = QtWidgets.QFileDialog.getOpenFileName(self, "Select file for open.", "C:/users/", '(*.csv)')
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Upload values to database?")
        msgBox.setWindowTitle("Do you want to continue?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            size_file = os.path.getsize(open_file_data[0])
            with open(open_file_data[0], 'r') as file:
                size = 0
                for i in range(100):
                    line = file.readline()
                    size += sys.getsizeof(line)
            whait = (size_file / size) * 100
            whait = int(whait) - 1
            print(size_file, size, whait)
            p = QtWidgets.QProgressDialog(str("Load data in database"), "Cancel", 0, whait)
            p.setMinimumDuration(0)
            p.setWindowTitle('please, wait')
            with open(open_file_data[0], 'r') as log_file:
                j = 0
                for line in log_file:
                    p.setValue(j)
                    j += 1
                    QtWidgets.QApplication.processEvents()
                    k = line.split('|')
                    LoadData(coll, CreateDick(k[1], k[2], k[3], k[4], k[5], k[6], k[7]))
                    if p.wasCanceled():
                        break
                p.setValue(whait)

    def SearchByNickname(self):
        nickname, ok = QtWidgets.QInputDialog.getText(self, "Search by nickname.", "Enter nickname for searching:",
                                                      QtWidgets.QLineEdit.Normal, '')
        if ok and nickname:
            self.label.setText("Search by nickname: " + '\n' + nickname)
            self.elem_for_search = {'Nick': nickname}
            result = coll.find(self.elem_for_search)
            k = 0
            j = 0
            kratno100 = False
            self.ui.SplitBy100.clear()
            for i in result:
                kratno100 = False
                j += 1
                if ((j % 99) == 0):
                    k += 1
                    self.ui.SplitBy100.addItem("{0} - 100 elem".format(k))
                    kratno100 = True
            self.ui.SplitBy100.setCurrentIndex(0)
            if kratno100:
                pass
            else:
                self.ui.SplitBy100.addItem("Остаток")
        elif ok and not nickname:
            QtWidgets.QMessageBox.about(self, 'Error', "Please enter nickname.")

    def SearchByPhonenumber(self):
        phone_num, ok = QtWidgets.QInputDialog.getText(self, "Search by phone number.",
                                                       "Enter phone number for searching:",
                                                       QtWidgets.QLineEdit.Normal, '')
        if ok and phone_num:
            self.label.setText("Search by phone number: " + '\n' + phone_num)
            self.elem_for_search = {'Phone': phone_num}
            result = coll.find(self.elem_for_search)
            k = 0
            j = 0
            kratno100 = False
            self.ui.SplitBy100.clear()
            for i in result:
                kratno100 = False
                j += 1
                if ((j % 99) == 0):
                    k += 1
                    self.ui.SplitBy100.addItem("{0} - 100 elem".format(k))
                    kratno100 = True
            self.ui.SplitBy100.setCurrentIndex(0)
            if kratno100:
                pass
            else:
                self.ui.SplitBy100.addItem("Остаток")
        elif ok and not phone_num:
            QtWidgets.QMessageBox.about(self, 'Error', "Please enter phone number.")

    def SearchBySurname(self):
        surname, ok = QtWidgets.QInputDialog.getText(self, "Search by surname.", "Enter surname for searching:",
                                                     QtWidgets.QLineEdit.Normal, '')
        if ok and surname:
            self.label.setText("Search by surname: " + '\n' + surname)
            self.elem_for_search = {'Surname': surname}
            result = coll.find(self.elem_for_search)
            k = 0
            j = 0
            kratno100 = False
            self.ui.SplitBy100.clear()
            for i in result:
                kratno100 = False
                j += 1
                if ((j % 99) == 0):
                    k += 1
                    self.ui.SplitBy100.addItem("{0} - 100 elem".format(k))
                    kratno100 = True
            self.ui.SplitBy100.setCurrentIndex(0)
            if kratno100:
                pass
            else:
                self.ui.SplitBy100.addItem("Остаток")
        elif ok and not surname:
            QtWidgets.QMessageBox.about(self, 'Error', "Please enter surname.")

    def Search(self):
        self.ui.actionSave_row.setDisabled(True)
        self.id_array = []
        if coll.estimated_document_count() == 0:
            QtWidgets.QMessageBox.about(self, 'Error', "Current Database is empty")
        else:
            if not self.elem_for_search:
                QtWidgets.QMessageBox.about(self, 'Error', "Please, enter a parameter for search.")
            else:
                result = FoundData(coll, self.elem_for_search, self.ui.SplitBy100.currentIndex())
                self.ui.tableWidget.setRowCount(0)
                row_num = 0
                for dick in result:
                    self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                    colum_num = 0
                    for key, value in dick.items():
                        if key == '_id':
                            self.id_array.append(value)
                            continue
                        it = QtWidgets.QTableWidgetItem()
                        it.setData(QtCore.Qt.DisplayRole, value)
                        self.ui.tableWidget.setItem(row_num, colum_num, it)
                        colum_num += 1
                    row_num += 1
                if row_num == 0:
                    QtWidgets.QMessageBox.about(self, 'Error 404', "Data not found.")

    def SaveData(self):
        if not self.elem_for_search:
            QtWidgets.QMessageBox.about(self, 'Error', 'There was no search query.')
        else:
            save = QtWidgets.QFileDialog.getSaveFileName(self, "Choose a filename to save under", "/data_save",
                                                         "(*.json)")
            if save[0] == '':
                QtWidgets.QMessageBox.about(self, 'Error', 'Your cancel save.')
            else:
                save_data = self.elem_for_search
                save_data['ComboBoxID'] = self.ui.SplitBy100.currentIndex()
                with open(save[0], 'w')as save_file:
                    json.dump(save_data, save_file)

    def LoadData(self):
        open_load_file = QtWidgets.QFileDialog.getOpenFileName(self, "Select file for open.", "C:/users/",
                                                               '(*.json)')
        with open(open_load_file[0], 'r')as load_file:
            data = json.load(load_file)
        comboID = data['ComboBoxID']
        del data['ComboBoxID']
        name_file = os.path.basename(open_load_file[0])
        self.label.setText("Load Search query from file: " + '\n' + name_file)
        self.ui.SplitBy100.clear()
        result = FoundData(coll, data, comboID)
        self.ui.tableWidget.setRowCount(0)
        row_num = 0
        for dick in result:
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            colum_num = 0
            for key, value in dick.items():
                if key == '_id':
                    continue
                it = QtWidgets.QTableWidgetItem()
                it.setData(QtCore.Qt.DisplayRole, value)
                self.ui.tableWidget.setItem(row_num, colum_num, it)
                colum_num += 1
            row_num += 1
        if row_num == 0:
            QtWidgets.QMessageBox.about(self, 'Error 404', "Data not found.")

    def ClearRow_forEnter(self):
        self.ui.actionSave_row.setDisabled(False)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(1)

    def SaveRow_inDB(self):
        data = []
        try:
            for i in range(7):
                data.append(self.ui.tableWidget.item(0, i).text())
        except AttributeError:
            QtWidgets.QMessageBox.about(self, 'Error', 'Column ' + str(i + 1) + ' is empty')
            return 1
        LoadData(coll, CreateDick(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        QtWidgets.QMessageBox.about(self, 'Completed.', "Data added to database.")
        self.ui.tableWidget.setRowCount(0)

    def DeletData(self):
        tabel = self.ui.tableWidget
        current_row = tabel.currentRow()
        id = {'_id': self.id_array[current_row]}
        if current_row == -1:
            QtWidgets.QMessageBox.about(self, 'Error', "Unselected row.")
            return 1
        tabel.removeRow(current_row)
        self.id_array.remove(self.id_array[current_row])
        DeleteData(coll, id)

    def HelpButt(self):
        pass

    def Update_Data(self):
        tabel = self.ui.tableWidget
        current_row = tabel.currentRow()
        if current_row == -1:
            QtWidgets.QMessageBox.about(self, 'Error', "Unselected row.")
            return 1
        id = {'_id': self.id_array[current_row]}
        columMax = 7
        data_row = []
        for currentColum in range(columMax):
            data_row.append(tabel.item(current_row, currentColum).text())
        UpdateData(id, CreateDick(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4], data_row[5],
                                  data_row[6]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())