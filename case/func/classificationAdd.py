import os
import sys
import requests
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from common.mylogger import logger
from common.connect_mysql import execute_sql

class ClassificationAdd():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/gc/classification/add'

    @allure.step('添加分类')
    def classificationAdd(self,name,
                          parentId,
                          status,
                          source,
                          sequence=None,
                          logo=None,
                          introduction=None,
                          url=None,
                          recommend=None,
                          remark=None,
                          proxies=None):
        data = {
            'name':name,
            'parentId':parentId,
            'sequence':sequence,
            'logo':logo,
            'introduction':introduction,
            'status':status,
            'url':url,
            'recommend':recommend,
            'remark':remark,
            'source':source,
        }
        r = self.s.post(url=self.url,json=data,verify=False,proxies=proxies)
        logger.info('classificationAdd接口运行时间：%f'%(r.elapsed.total_seconds()))
        return r.json()



def db_classificationDelete(db,name):
    sql ='''
    DELETE from classification_add where classification_name='{name}'
    '''.format(name=name)
    r = execute_sql(db,sql)
    logger.info('执行的sql语句为：%s'%sql)
    print(r)



if __name__ == '__main__':
    # from case.getSession import getSession
    # host = 'https://backstageservices.dreawer.com'
    # proxies = {
    #     "http": "http://127.0.0.1:8888",
    #     "https": "http://127.0.0.1:8888",
    # }
    # s = getSession(host=host,proxies=proxies)
    # add = ClassificationAdd(s,host)
    # data = {
    #     'name': 'coco',
    #     'parentId': '0',
    #     'status': 'DEFAULT',
    #     'source': 'RETAIL',
    #     'proxies':proxies
    # }
    # r = add.classificationAdd(**data)
    # print(r)
    db = {
        "host": "192.168.0.123",
        "user": "root",
        "password": "123456",
        "port": 3306,
        "database": "appx",
    }
    db_classificationDelete(db,'coco1033')
