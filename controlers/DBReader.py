
import pymysql.cursors

class DBReader():
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

    def getSumDeposits(self):
        conn = self.connect()

        try:
            with conn.cursor() as cursor:
                sql = "SELECT Coin, SUM(Amount) FROM `Historique` WHERE Operation='Deposit' GROUP BY Coin;"
                cursor.execute(sql)

                # Fetch all rows
                rows = cursor.fetchall()

                # Print results
                for row in rows:
                    print(row)
        finally:
            conn.close()

