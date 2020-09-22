from quart import Quart, websocket
from nonebot import *
import os
from sqlitedict import SqliteDict
try:
	from .asf_plus import ASF_Plus
	from .Steam import Steam
	#from .database import db
except:
	from asf_plus import ASF_Plus
	from Steam import Steam
	#from database import db
import jinja2

template_folder = os.path.join(os.path.dirname(__file__),'templates')
print(template_folder)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_folder),
    enable_async=True
    )

async def render_template(template,**kwargs):
    t = env.get_template(template)
    return await t.render_async(**kwargs)
    

class db(object):
	def __init__(self,user):
		self.user = str(user)
		self.db = SqliteDict(self.getCfgPath(),autocommit=True)
		
	def get(self,key=''):
		if key:
			return self.db.get(key)
		else:
			return self.db.iteritems()
			
	def set(self,key='',data=''):
			if not key:
				key = self.user
			if data:
				self.db[key] = data
			else:
				self.db.__delitem__(key)
			
	def getCfgPath(self):
		if os.path.isdir('hoshino'):
			if not os.path.isdir('hoshino/modules/ASF_Plus/config'):
				os.mkdir('hoshino/modules/ASF_Plus/config')
			return os.path.join(os.path.abspath('hoshino/modules/ASF_Plus/config'),f'{self.user}.sqlite')
		else:
			if not os.path.isdir('../config'):
				os.mkdir('../config')
			return os.path.join(os.path.abspath('../config'),f'{self.user}.sqlite')
		



app = get_bot().server_app
@app.route('/')
async def hello():
    return 'This is a useless ester egg'
    
def getNickname(user):
    url = Steam(str(ASF_Plus(user).getBot()['SteamID'])).getSteamName()
    if not url:
       url = '出错！请尝试重新登录！'
    return url
    
def getUrl(user):
	url = Steam(str(ASF_Plus(user).getBot()['SteamID'])).getSteamProfile()
	if not url:
		url = 'https://store.steampowered.com'
	return url

def getAvatar(user):
	url = Steam(str(ASF_Plus(user).getBot()['SteamID'])).getAvatar()
	if not url:
		url = 'https://qasf.novanoir.cn/imgs/NWS_Logo2.png.jpg'
	return url
	
def getPlaying(user):
	raw_data = ASF_Plus(user).getBot()
	game,id = Steam(str(raw_data['SteamID'])).getPlaying()
	#print(raw_data)
	onWork = raw_data.get('Enabled')
	if not id: #or not onWork:
		game = '没有在玩游戏'
		return [False,game]
	
	url = f'https://store.steampowered.com/app/{id}'
	imgs = f'https://media.st.dl.pinyuncloud.com/steam/apps/{id}/header.jpg'
	return [True,game,url,imgs]
			

app.add_template_global(getUrl, 'getUrl')
@app.route('/user/<usern>')
async def user(usern):
    d = db(usern)
    user_info = d.get('defaultBot')
    return await render_template('user_info.html', page_title=f'{usern}\'s Bots',user_info = getNickname(user_info),avaUrl=getAvatar(user_info),steamUrl=getUrl(user_info),gameInfo=getPlaying(user_info),bot_name = user_info)


@app.route('/Bot/Start/<bot>',methods=['POST'])
async def botOn(bot):
    abot = ASF_Plus(bot)
    return abot.startBot()
    
@app.route('/Bot/Stop/<bot>',methods=['POST'])
async def botOff(bot):
    abot = ASF_Plus(bot)
    return abot.stopBot()
    