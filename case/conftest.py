import os
import sys
import requests
import pytest
import urllib3
urllib3.disable_warnings()

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from case.func.login import Login
from case.func.getUserToken import GetUserToken
from case.func.uploadImage import UploadImage


# host = 'https://backstageservices.dreawer.com'
# proxies = {
#     "http": "http://127.0.0.1:8888",
#     "https": "http://127.0.0.1:8888",
# }

# file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))+'/image/image.png')

@pytest.fixture(scope='session')
def getSession(getHostAndProxies):
    s = requests.session()
    host, proxies = getHostAndProxies
    l = Login(s,host)
    token,appid = l.getTokenAndAppID(proxies=proxies)
    h = {
        'appid':appid,
        'Authorization':token}
    s.headers.update(h)
    get_token = GetUserToken(s,host)
    real_token = get_token.getToken(appid=appid,proxies=proxies)
    h = {'Authorization':real_token}
    s.headers.update(h)
    return s

@pytest.fixture(scope='session')
def getImagePath(getSession,getHostAndProxies,file_path):
    s = getSession
    host, proxies = getHostAndProxies
    file_path = file_path
    image = UploadImage(s,host)
    image_path = image.getImagePath(file_path=file_path,proxies=proxies)
    return image_path


if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    # s = getSession(host=host,proxies=proxies)
    # print(s.headers)