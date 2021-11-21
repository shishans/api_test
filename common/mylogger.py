import logging
import os
import datetime

log_dir = os.path.dirname(os.path.dirname(__file__))+'/log/'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_name = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
log_path = os.path.join(log_dir,log_name)



class Mylogger(logging.Logger):
    def __init__(self,name='coco', level=logging.INFO,file=None):
        super(Mylogger, self).__init__(name, level)

        # 日志格式
        fmt = '%(asctime)s [%(levelname)s] -- [%(filename)s:%(funcName)s] -- message:%(message)s'
        formatter = logging.Formatter(fmt)

        #控制台渠道
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        self.addHandler(sh)


        #文件渠道
        if file:
            fh = logging.FileHandler(file,encoding='utf-8')
            fh.setFormatter(formatter)
            self.addHandler(fh)

logger = Mylogger(file=log_path)