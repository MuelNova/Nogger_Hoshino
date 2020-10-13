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
        
    @property
    async def config(self):
        if not os.path.isfile(self.path):
            await self.generate_Config()
            return self.cfg
        else:
            co = Sqlite(self.path)
            for k,v in co.sqlite.iteritems():
                self.cfg[k] = v
            return self.cfg
        
    async def generate_Config(self):
        data = await AioAsf(self.bot).get_status()
        if data:
            co = Sqlite(self.path)
            co.sqlite['SteamID'] = data.get('SteamID') if data.get('SteamID') else 0
            co.sqlite['Nickname'] = data.get('Nickname') if data.get('Nickname') else ''
            if data.get('BotConfig'):
                co.sqlite['IdleGames'] = data.get('BotConfig').get('GamesPlayedWhileIdle') if data.get('BotConfig').get('GamesPlayedWhileIdle') else []
            else:
                co.sqlite['IdleGames'] = []
            await self.config
        else:
            print("ERROR: Cant get the bot 's config\n Please check name or internet")