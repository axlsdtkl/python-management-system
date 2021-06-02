import pymysql

def mul(x,y):
    return x*y
class Database(object):
    def __init__(self):
        "连接数据库"
        self.db=pymysql.connect(host="localhost",user="root",passwd="gunxueqiu",database="badminton",charset="utf8")
        self.cursor=self.db.cursor()

    def prepare(self,sql):
        "执行sql语句"
        return self.cursor.execute(sql)

    def update(self):
        "提交到数据库"
        self.db.commit()

    def close(self):
        "关闭数据库"
        self.db.close()