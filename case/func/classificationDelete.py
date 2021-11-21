import os
import sys
import requests
import pytest
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from common.mylogger import logger

class ClassificationDelete():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/gc/classification/delete'

    @allure.step('删除分类')
    def classificationDelete(self,classificationId,proxies=None):
        data = {
            "storeId": "1514e1d61686438f95fa46f19070c126",
            "id": classificationId
        }
        r = self.s.post(url=self.url,json=data,verify=False,proxies=proxies)
        logger.info('classificationDelete接口运行时间：%f' % (r.elapsed.total_seconds()))
        return r.json()

