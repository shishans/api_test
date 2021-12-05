import os
import sys
import requests
import pytest
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from common.mylogger import logger

class ClassificationUpdateStatus():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/gc/classification/updateStatus'

    def classificationUpdateStatus(self,ids,status='DEFAULT',msg=None,proxies=None):
        '''
        :param ids: 必填  List 	分类ID列表
        :param status: 必填  String 分类状态（DEFAULT-正常、DISABLED-已禁用）
        :param msg: 非必填 String
        :return: dict
        '''
        data = {
        'ids':ids,
        'status':status,
        }
        r = self.s.post(url=self.url,json=data,verify=False,proxies=proxies)
        logger.info('classificationUpdateStatus接口运行时间：%f' % (r.elapsed.total_seconds()))
        return r.json()

    def db_checkouStatus(self):pass