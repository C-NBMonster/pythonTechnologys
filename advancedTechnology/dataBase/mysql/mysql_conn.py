#_*_ coding:utf-8 _*_
import pymysql

class C_mysql_conn():
    def mysql_conn(self, host,  user, password,dbName,port=3306, charset='utf8'):
        #封装链接函数
        conn = pymysql.connect(host=host,
                               db=dbName,
                               port=port,
                               user=user,
                               passwd=password,
                               charset='utf8'
                               )
        return conn

    def execute_sql(self, conn, *sql):
        cursor = conn.cursor()
        try:
            global eff_rows
            eff_rows = cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            return cursor,eff_rows


    def close_conn(self, cursor, conn):
        #关闭链接
        cursor.close()
        conn.close()


    import contextlib


    # 定义上下文管理器，连接后自动关闭连接
    @contextlib.contextmanager
    def mysql(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1', charset='utf8'):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield cursor
        finally:
            conn.commit()
            cursor.close()
            conn.close()


    # 执行sql
    with mysql() as cursor:
        print(cursor)
        row_count = cursor.execute("select * from tb7")








