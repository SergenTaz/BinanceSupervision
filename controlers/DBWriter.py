import pandas

from models.History import History
import pymysql.cursors

class DBWriter():
    def __init__(self,host,user,password,db,port=0):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        self.port=port

    def connect(self):
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            cursorclass=pymysql.cursors.DictCursor,
            port=self.port)

        return conn

    def writeHistory(self,history : History):
        conn=self.connect()
        cursor=conn.cursor()

        sql = "INSERT INTO `Historique` (`User_ID`, `Date`, `Account`, `Operation`, `Coin`, `Amount`) " \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s');"
        for transaction in history.history:
            user = transaction.getUserid()
            date = transaction.getDate().strftime("%Y-%m-%d %H:%M:%S")
            account = transaction.getAccount()
            operation = transaction.getOperation()
            token = transaction.getToken()
            amount = transaction.getAmount()

            cursor.execute(sql % (user, date, account, operation, token, amount))

        conn.commit()
        conn.close()

    def truncateTable(self, table: str):
        conn = self.connect()
        cursor = conn.cursor()

        sql = "TRUNCATE "+table+ ";"
        conn.commit()
        conn.close()
