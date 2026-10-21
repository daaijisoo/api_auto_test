import pymysql

from conf.globaldata import SQLOPTIONS


class DBHelper:
    def __init__(self,
                 host=SQLOPTIONS["host"],
                 port=SQLOPTIONS["port"],
                 user=SQLOPTIONS["user"],
                 password=SQLOPTIONS["password"],
                 database=SQLOPTIONS["database"]):
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.database = database

    def connect(self):
        try:
            conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            cursor = conn.cursor()
        except Exception as e:
            print(e)
        else:
            self.conn = conn
            self.cursor = cursor

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self,sql,params,num):
        self.connect()
        self.cursor.execute(sql,params)
        data = None
        if num == 1:
            data = self.cursor.fetchone()
        elif num == -1:
            data = self.cursor.fetchall()
        else:
            data = self.cursor.fetchmany(num)
        self.close()
        return data


if __name__ == "__main__":
    db = DBHelper("localhost",3306,"root","root","plus")
    data = db.query("select id from ls_user where mobile=%s",["18888888888"],1)
    print(data)






