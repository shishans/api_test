import os
import sys
import requests
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from common.mylogger import logger

class UploadImage():
    def __init__(self,s,host):
        self.s = s
        self.host= host
        self.url = host+'/ic/uploadImage'

    @allure.step('上传图片')
    def uploadImage(self,file_path,proxies=None):
        file_name = os.path.split(file_path)[1]
        data = {
            'appname':'RETAIL',
            'type':'IMAGE'
        }
        files = {
            'file':(file_name,open(file_path,'rb'),'image/jpeg')
        }
        r = self.s.post(url=self.url,data=data,files=files,proxies=proxies,verify=False)
        logger.info('上传图片接口运行时间：%f' % (r.elapsed.total_seconds()))
        return r.json()

    @allure.step('获取图片地址')
    def getImagePath(self,file_path,proxies=None):
        r = self.uploadImage(file_path,proxies)
        image_path = r['data'][0]
        return image_path

if __name__ == '__main__':
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    file_path = './../../image/image.png'
    image = UploadImage(s,host)
    # r = image.uploadImage(host,file_path,proxies=proxies)
    #
    image_path = image.getImagePath(file_path,proxies)
    print(image_path)

