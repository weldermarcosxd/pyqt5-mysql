from PyQt5 import QtCore, QtGui, QtWidgets
from connector import Connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        self.menuConfigurar = QtWidgets.QMenu(self.menubar)
        self.menuConfigurar.setObjectName("menuConfigurar")
        MainWindow.setMenuBar(self.menubar)
        self.actionPropiedades = QtWidgets.QAction(MainWindow)
        self.actionPropiedades.setObjectName("actionPropiedades")
        self.menuConfigurar.addAction(self.actionPropiedades)
        self.menubar.addAction(self.menuConfigurar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Filtrar"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.menuConfigurar.setTitle(_translate("MainWindow", "Configurar"))
        self.actionPropiedades.setText(_translate("MainWindow", "Propiedades"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    conn = Connector()
    db = conn.getConnection(sys.argv[1]) if len(sys.argv) > 1 else conn.getConnection()

    print(db.lastError().text())
    print("PluginsPath =>          " + QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath))

    MainWindow.show()
    sys.exit(app.exec_())

