import time

def timestamp(num):
    '''生成不同位数的时间戳'''
    now = time.time()
    if num == 10:
        r = round(now)
    elif num<10:
        r = round(now*(0.1**(10-num)))
    else:
        r = round(now*(10**(num-10)))
    return r

def timmer(func):
    '''统计接口请求的时间'''
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('接口请求时间:%s'%(end_time-start_time))
        return res
    return wrapper

if __name__ == '__main__':
    r = timestamp(16)
    print(len(str(r)),r)