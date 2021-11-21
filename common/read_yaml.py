import yaml
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from common.mylogger import logger

def readyml(yamlPath):
    '''读取yaml文件内容
    yamlPath: 文件的绝对路径 '''
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    data = yaml.load(cfg, Loader=yaml.FullLoader )
    return data

if __name__ == '__main__':
    curPath = os.path.dirname(os.path.dirname(__file__))
    yamlFilePath = os.path.join(curPath, 'environment.yml')
    data = readyml(yamlFilePath)
    data = data['test']['file_path']
    print(eval(data))