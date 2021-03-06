# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DateBase_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 766)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 901, 711))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.SplitBy100 = QtWidgets.QComboBox(self.centralwidget)
        self.SplitBy100.setGeometry(QtCore.QRect(910, 60, 191, 31))
        self.SplitBy100.setObjectName("SplitBy100")
        self.SplitBy100.addItem("")
        self.Label_SearchBy = QtWidgets.QLabel(self.centralwidget)
        self.Label_SearchBy.setGeometry(QtCore.QRect(910, 10, 191, 41))
        self.Label_SearchBy.setObjectName("Label_SearchBy")
        self.SearchBut = QtWidgets.QPushButton(self.centralwidget)
        self.SearchBut.setGeometry(QtCore.QRect(910, 100, 191, 31))
        self.SearchBut.setObjectName("SearchBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1109, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menuAdd = QtWidgets.QMenu(self.menuBar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuAdd_data_row = QtWidgets.QMenu(self.menuAdd)
        self.menuAdd_data_row.setObjectName("menuAdd_data_row")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSearch = QtWidgets.QMenu(self.menuBar)
        self.menuSearch.setObjectName("menuSearch")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionRemove_data_row = QtWidgets.QAction(MainWindow)
        self.actionRemove_data_row.setObjectName("actionRemove_data_row")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSearch_by_Nickname = QtWidgets.QAction(MainWindow)
        self.actionSearch_by_Nickname.setObjectName("actionSearch_by_Nickname")
        self.actionSearc_by_Phone_number = QtWidgets.QAction(MainWindow)
        self.actionSearc_by_Phone_number.setObjectName("actionSearc_by_Phone_number")
        self.actionSearch_by_Surname = QtWidgets.QAction(MainWindow)
        self.actionSearch_by_Surname.setObjectName("actionSearch_by_Surname")
        self.actionUpdate_data = QtWidgets.QAction(MainWindow)
        self.actionUpdate_data.setObjectName("actionUpdate_data")
        self.actionEnter_row = QtWidgets.QAction(MainWindow)
        self.actionEnter_row.setObjectName("actionEnter_row")
        self.actionSave_row = QtWidgets.QAction(MainWindow)
        self.actionSave_row.setObjectName("actionSave_row")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionLoad)
        self.menu.addAction(self.actionSave)
        self.menuAdd_data_row.addAction(self.actionEnter_row)
        self.menuAdd_data_row.addAction(self.actionSave_row)
        self.menuAdd.addAction(self.menuAdd_data_row.menuAction())
        self.menuAdd.addAction(self.actionRemove_data_row)
        self.menuAdd.addAction(self.actionUpdate_data)
        self.menuHelp.addAction(self.actionHelp)
        self.menuSearch.addAction(self.actionSearch_by_Nickname)
        self.menuSearch.addAction(self.actionSearc_by_Phone_number)
        self.menuSearch.addAction(self.actionSearch_by_Surname)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuSearch.menuAction())
        self.menuBar.addAction(self.menuAdd.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "UID"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Nickname"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "WO"))
        self.SplitBy100.setItemText(0, _translate("MainWindow", "1st 100 elem"))
        self.Label_SearchBy.setText(_translate("MainWindow", "Search by nothing:\n"
""))
        self.SearchBut.setText(_translate("MainWindow", "Search"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menuAdd.setTitle(_translate("MainWindow", "Edit"))
        self.menuAdd_data_row.setTitle(_translate("MainWindow", "Add data row"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.actionOpen.setText(_translate("MainWindow", "Load data in date base"))
        self.actionLoad.setText(_translate("MainWindow", "Load search query"))
        self.actionSave.setText(_translate("MainWindow", "Save search query"))
        self.actionRemove_data_row.setText(_translate("MainWindow", "Remove data row"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSearch_by_Nickname.setText(_translate("MainWindow", "Search by Nickname"))
        self.actionSearc_by_Phone_number.setText(_translate("MainWindow", "Search by Phone number"))
        self.actionSearch_by_Surname.setText(_translate("MainWindow", "Search by Surname"))
        self.actionUpdate_data.setText(_translate("MainWindow", "Update data"))
        self.actionEnter_row.setText(_translate("MainWindow", "Enter row"))
        self.actionSave_row.setText(_translate("MainWindow", "Save row"))
