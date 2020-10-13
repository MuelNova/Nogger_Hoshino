import json

from .aiorequests import get, post
from config import asf_url, asfPassword, steamKey

def generate_url(path,para={}):
    if asfPassword:
        return '{}?password={}'.format(path,asfPassword) + ''.join('&{}={}'.format(i,para.get(i)) for i in para)
    return '{}?'.format(path) + '&'.join('{}={}'.format(i,para.get(i)) for i in para)

class AioAsf(object):
    def __init__(self,bot):
        self.bot = bot
        
    async def get_status(self):
        a = await get(url=generate_url('{}Api/Bot/{}'.format(asf_url,self.bot)))
        a = await a.text
        a = json.loads(a)
        return a.get('Result').get(self.bot)
        