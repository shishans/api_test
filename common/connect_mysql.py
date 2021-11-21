import pymysql

class DbConnect():
    def __init__(self, dbinfo):
        self.dbinfo = dbinfo
        # 打开数据库连接
        self.db = pymysql.connect(cursorclass=pymysql.cursors.DictCursor,
                                  **dbinfo)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        try:
           self.cursor.execute(sql)
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()

def select_sql(db,select_sql):
    '''查询数据库'''
    db = DbConnect(db)
    result = db.select(select_sql)  # 查询
    db.close()
    return result

def execute_sql(db, insert_sql):
    '''执行sql'''
    db = DbConnect(db)
    db.execute(insert_sql)
    db.close()


if __name__ == '__main__':
    db = {
        "host": "192.168.0.123",
        "user": "root",
        "password": 123456,
        "port": 3306,
        "database": "appx",
    }
    sql = '''INSERT INTO classification_add (
                classification_name,
                `status`,
                logo,
                url,
                parentId,
                source)
            VALUES
                ('coco5',
                    'DEFAULT',
                    '/resource/RETAIL/20211119/e8e6c8b16ef842a681e4054f53be2725.png',
                    '',
                    '0',
                    'APPX');
    '''
    execute_sql(db,sql)
    sql = "SELECT * from classification_add;"
    res = select_sql(db, sql)
    print(res)


