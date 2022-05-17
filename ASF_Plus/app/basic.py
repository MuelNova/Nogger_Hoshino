# 填写ASF密码在这
pw = 'dalizm8881018'

class asfbot:
	def __init__(self,name):
		self.name = name
		self.owner = 'public'
		self.config = self.getConfig()
		self.exist = self.isExist()
		
	def bind(self,owner):
		asf_addBot(self.name,owner)
		self.update()
		
	def update(self):
		self.config = self.getConfig()
		self.exist = self.isExist()
		
	def getConfig(self):
		path = os.path.join(getConfigPath(),f'{self.name}.cfg')
		if not os.path.isfile(path):
			return []
		with open(path,'r') as f:
			cfg = json.loads(f.read())
			self.owner = cfg['Owner']
			return cfg
			
	def isExist(self):
		return bool(self.config)
		
	def delBot(self):
		path = os.path.join(getConfigPath(),f'{self.name}.cfg')
		if os.path.isfile(path):
			os.remove(path)
		self.update()
		
	def createBot(self,ac,pw,ow):
		if self.exist:
			return False
		data = {'BotConfig':{'SteamLogin':ac,'SteamPassword':pw}}
		resp = asf_re('Bot',self.name,data,True)
	
	def loginBot(self,tfa=''):
		if tfa:
			data = {'Type':'TwoFactorAuthentication','Value':tfa}
			asf_re('Bot', f'{self.name}/Input', data, True)
		else:
			asf_re('Bot', f'{self.name}/Start', post=True)
	#	if resp[self.name]:
		#	return True
		
		
		
		


import requests, json, os


def asf_re(par,bot='',req=[],post=False):
	if bot:
		url = f'https://asf.novanoir.cn/Api/{par}/{bot}?password={pw}'
	else:
		url = f'https://asf.novanoir.cn/Api/{par}?password={pw}'
	try:
		if not post:
			with requests.get(url, timeout=20) as resp:
				res = resp.json()
				print(res)
				return res['Result']
		else:
			with requests.post(url, timeout=20,json=req) as resp:
				res = resp.json()
				print(res)
				return res['Result']
	except:
		return False
		
def asf_addBot(bot,owner):
	path = os.path.join(getConfigPath(),f'{bot}.cfg')
	if data := asf_re('Bot', bot)[bot]:
		with open(path,'w') as config:
			data.update({'Owner':str(owner)})
			config.write(json.dumps(data,indent=2))
	
	
def getConfigPath():
	if os.path.isdir('hoshino'):
		return os.path.abspath('hoshino/modules/ASF_Plus/config')
	else:
		return os.path.abspath('config')

if not os.path.isdir(getConfigPath()):
	os.mkdir(getConfigPath())
