#pylint:disable=W0603
import os
import random
import string
import sqlitedict
import yaml


config = dict()


def getConfig(item=''):
    '''
    get config
    获取配置
    item:获取全部（默认）
            ['var1','var2']
            'var'
    return (str / dict)
    
    eg.
        item=['pixiv','pwd']
            output 'password'
          item='pixiv'
            output {'user':'abc','pwd':'oassword'}
    '''
    global config
    # init config
    cfg_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'config.yml'))
    if not config:
        if not os.path.isfile(cfg_path):
            setConfig('pixiv',{'user':'','pwd':''})
            print('[nPixiv]: cfg not exist,creating...')
        else:
            with open(cfg_path,'r') as f:
                config = yaml.load(f.read(),Loader=yaml.FullLoader)
                
    # get config
    if not item:
        return config
    else:
        if isinstance(item,list):
            a = config
            for i in item:
                a = a.get(i) if isinstance(a,dict) else a
            return a
        elif isinstance(item,str):
            return config.get(item)
        else:
            return False
                    
            
            
def setConfig(data=None,item='',key=''):
    '''
    Set Config
    设置配置文件
    item,key:(str)
    data:(list) 
        e.g. [('a','avc'),('b',{'a':1,'bb':'cc'})]
    '''
    global config
    if not data and item and key:
        config[item] = key
    elif data:
        for i in data:
            if len(i) == 2:
                config[i[0]] = i[1]
    else:
        return False
    cfg_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'config.yml'))
    with open(cfg_path,'w') as f:
        f.write(yaml.dump(config))

def randString(n=10,type_=0):
    '''
    return random String
    返回一个随机字符串
        n = length (default:10)
        type_ = 0: Number + Lower + Upper (default)
                    1: Number
               
     return str
    '''
    if type_ == 1:
        chaset = string.digits
    else:
        chaset = (string.ascii_uppercase + string.ascii_lowercase + string.digits)
    return ''.join(random.choice(chaset)for _ in range(n))
    
   
# Debugger / Del it when release. 
#print(getConfig())

setConfig(data=[('test2',{'a':1,'b':'1'}),('test3','a')])