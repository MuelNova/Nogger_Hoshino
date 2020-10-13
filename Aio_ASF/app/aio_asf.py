from .aiorequests import get, post
from ..config import asf_url, asfPassword

def generate_url(path,para=[]):
    if asfPaassword:
        return '{}{}?password={}'.format(asf_url,path,asfPassword) + '&'.join('{}={}'.format(i,para.get(i)) for i in para)
    return '{}{}?'.format(asf_url,path) + '&'.join('{}={}'.format(i,para.get(i)) for i in para)

class AioAsf(object):
    def __init__(self):
        pass
        
    async def get_status(self,url):
        a = await get(url=url)
        a = await a.text
        print(a)