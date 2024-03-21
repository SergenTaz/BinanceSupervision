import pymysql.cursors

class DBReader():
    def __init__(self,host,user,password,db,port=3306):
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

    def __execSQL(self, sql):
        rows = None
        try:
            conn = self.connect()
            with conn.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
            conn.close()
            return rows
        except Exception as e:
            print("Cannot access to database " + self.db + " : " + e.__str__())
    def getSumDeposits(self):
        sql = "SELECT SUM(`Change`) FROM `BinanceTransactions` WHERE `Operation` LIKE '%Deposit%';"
        return self.__execSQL(sql)

    def getCoinHistory(self, coin):
        sql = "SELECT * FROM `BinanceTransactions` WHERE `Coin` LIKE '%" + coin + "%';"
        return self.__execSQL(sql)

    def getTransactionsOrderedByCoin(self):
        sql = "SELECT * FROM `BinanceTransactions` ORDER BY `Coin`;"
        return self.__execSQL(sql)
