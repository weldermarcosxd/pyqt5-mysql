from PyQt5 import QtSql 
from settings import Settings

class Connector:

    db = None

    def createConnection(self,env):
        settings = Settings(env)
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName(settings.host)
        self.db.setDatabaseName(settings.database)
        self.db.setUserName(settings.user)
        self.db.setPassword(settings.password)
        self.db.setPort(settings.port)
        return self.db.open

    def getConnection(self, env='dev'):
        if(self.db is None):
            if(self.createConnection(env)):
                return self.db
            else:
                raise QtSql.QSqlError.ConnectionError
        else:
            return self.db
            
