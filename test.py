from PyQt5 import QtSql
import mysql.connector

class DbConnection(object):
    def connect(self):
        try:
            self.__db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
            self.__db.setHostName("localhost")
            self.__db.setDatabaseName("employees")
            self.__db.setUserName("root")
            self.__db.setPassword("root")
            self.__ok = self.__db.open()
        except:
            print(self.__db.lastError().text())

        return self.__ok

    def closeConnection(self):
        try:
            self.__db.close()
        except:
            pass

if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)

    conn = DbConnection()
    print("Connected: " + str(conn.connect()))
    conn.closeConnection()

    sys.exit(app.exec_())
