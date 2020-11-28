
import cx_Oracle as cx      #导入模块
import os
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'

con = cx.connect('jjzd', 'zhzx', '45.6.205.4/orcl')
con.version
cursor = con.cursor()                          # 创建游标
cursor.execute("select count(1) from vio_violation")  # 执行sql语句
data = cursor.fetchone()                       # 获取一条数据
print(data)                                    # 打印数据
cursor.close()                                 # 关闭游标
con.close()                                    # 关闭数据库连接

"""
import cx_Oracle

class PyOracle(object):
#创建python操作oracle类
    def __init__(self, username, password, hosts):
        # 连接oracle数据库
        self.conn = cx_Oracle.connect(username, password, hosts)
        # 建立游标对象
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        # 关闭数据库连接
        self.cursor.close()
        self.conn.close()
    
    def get_row(self, sql):
        # 生成器获取数据
        self.cursor.execute(sql)
        for row in self.cursor:
            yield row
    
    def get_column(self, sql):
        # 获取字段
        self.cursor.execute(sql)
        fieldnames = []
        columns = self.cursor.description
        if columns:
            for column in columns:
                column = column[0].lower()
                fieldnames.append(column)
        return fieldnames
    
    def get_one(self, sql):
        # 获取一条数据
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    def get_all(self, sql):
        # 获取所有数据
        self.cursor.execute(sql)
        return self.cursor.fetchall()
"""