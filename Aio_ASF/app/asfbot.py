import os

from .aio_asf import AioAsf
from .util import Sqlite

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,'config'))
if not os.path.isdir(base_path):
    os.mkdir(base_path)


class asfbot(object):
    def __init__(self,bot):
        self.bot = bot
        self.path = os.path.join(base_path, self.bot + '.sqlite')
        self.cfg = dict()
        self.aio = AioAsf(self.bot)
        
    @property
    async def config(self):
        if not os.path.isfile(self.path):
            await self.generate_Config()
            return self.cfg
        else:
            co = Sqlite(self.path)
            self.aio.set_id(str(co.sqlite.get('SteamID')))
            for k,v in co.sqlite.iteritems():
                self.cfg[k] = v
            return self.cfg
        
    async def generate_Config(self):
        
        data = await self.aio.get_Asf_Config()
        if data:
            co = Sqlite(self.path)
            co.sqlite['SteamID'] = data.get('SteamID') if data.get('SteamID') else 0
            co.sqlite['Nickname'] = data.get('Nickname') if data.get('Nickname') else ''
            if data.get('SteamID'):
                self.aio.set_id(str(data.get('SteamID')))
                print(self.aio.id_)
                steam_data = await self.aio.get_Steam_Config()
                co.sqlite['PersonaName'] = steam_data.get('personaname') if steam_data.get('personaname') else ''
                co.sqlite['Avatar'] = steam_data.get('avatarfull') if steam_data.get('avatarfull') else ''
            if data.get('BotConfig'):
                co.sqlite['IdleGames'] = data.get('BotConfig').get('GamesPlayedWhileIdle') if data.get('BotConfig').get('GamesPlayedWhileIdle') else []
            else:
                co.sqlite['IdleGames'] = []
            await self.config
        else:
            print("ERROR: Cant get the bot 's config\n Please check name or internet")
            
    async def playing_Info(self):
        if await self.config:
            stat = await self.aio.get_Playing()
            info = dict()
            if stat:
                gid,game,gicon = stat
                info['now_playing'] = {'gid':gid,'game':game,'gicon':gicon}
            recent = await self.aio.get_Recently()
            if recent:
                info['recent_total'], info['recent'] = recent
                
            return info
        return False
            
    
    
    
    
#https://wiki.teamfortress.com/wiki/User:RJackson/StorefrontAPI
#https://partner.steamgames.com/doc/webapi