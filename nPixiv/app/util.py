import random
import string
import sqlitedict


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
print(randString(n=30,type_=2))
print(''.join('★' for _ in range(10)))