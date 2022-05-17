import json
import re
from .aiorequests import get, post
try:
    from ..config import asf_url, asfPassword, steamKey
except:
    from config import asf_url, asfPassword, steamKey
from .util import Sqlite

def generate_url(path,para={}):
    if asfPassword:
        return f'{path}?password={asfPassword}' + ''.join(
            f'&{i}={para.get(i)}' for i in para
        )

    return f'{path}?' + '&'.join(f'{i}={para.get(i)}' for i in para)

class AioAsf(object):
    def __init__(self,bot,id_=0):
        self.bot = bot
        self.id_ = id_
        
    def set_id(self,id_):
        self.id_ = id_
    
    async def get_Asf_Config(self):
        a = await get(url=generate_url(f'{asf_url}Api/Bot/{self.bot}'))
        a = await a.text
        a = json.loads(a)
        return a.get('Result').get(self.bot)
    
    async def get_Steam_Config(self,id_=0):
        if not id_:
            id_ = self.id_
        a = await get(
            url=f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002?steamids={id_}&key={steamKey}'
        )

        a = await a.text
        a = json.loads(a)
        return a.get('response').get('players')[0]
    
    async def get_Playing(self,id_=0):
        if not id_:
            id_ = self.id_
        r = await self.get_Steam_Config(id_)
        if r:
            if r.get('gameid'):
                return (
                    r.get('gameid'),
                    r.get('gameextrainfo'),
                    f"https://steamcdn-a.akamaihd.net/steam/apps/{r.get('gameid')}/header.jpg",
                )

            return False
    
    async def get_Recently(self,id_=0):
        if not id_:
            id_ = self.id_
        r = await get(
            url=f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1?key={steamKey}&steamid={id_}'
        )

        try:
            r = await r.json()
            if r.get('response').get('total_count'):
                return (r.get('response').get('total_count'),r.get('response').get('games'))
            return False
        except:
            return False
    
    
    
        