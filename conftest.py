import os
import sys
import pytest
import urllib3
urllib3.disable_warnings()

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.read_yaml import readyml
from common.mylogger import logger

curPath = os.path.dirname(__file__)
yamlFilePath = os.path.join(curPath, 'environment.yml')

def pytest_addoption(parser):
    parser.addoption(
        '--environment', action='store''', default='test', help='运行环境选择：test/pro，默认test环境'
    )

@pytest.fixture(scope='session',autouse=True)
def environment(request):
    os.environ['environment'] = request.config.getoption('--environment')
    logger.info('当前运行环境：%s'%os.environ['environment'])
    return os.environ['environment']

@pytest.fixture(scope='session',autouse=True)
def getHostAndProxies(environment):
    env = environment
    host = readyml(yamlFilePath)[env]['host']
    logger.info('当前host地址:%s'%host)
    proxies = readyml(yamlFilePath)[env]['proxies']
    if sys.platform != 'win32':
        proxies = None
    logger.info('当前代理环境:%s' % proxies)
    return host,proxies

@pytest.fixture(scope='session',autouse=True)
def file_path(environment):
    env = environment
    file_path = readyml(yamlFilePath)[env]['file_path']
    return eval(file_path)

@pytest.fixture(scope='session',autouse=True)
def dbinfo(environment):
    env = environment
    db = readyml(yamlFilePath)[env]['db']
    logger.info('当前数据库为:%s'%db)
    return db


