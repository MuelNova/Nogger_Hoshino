# 填写ASF密码在这
pw = 'password'

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
			else:
				with open(path,'r') as f:
					cfg = json.loads(f.read())
					self.owner = cfg['Owner']
					return cfg
			
	def isExist(self):
		return True if self.config else False
		
	def delBot(self):
		path = os.path.join(getConfigPath(),f'{self.name}.cfg')
		os.remove(path)
		self.update()
		


import requests, json, os


def asf_re(par,bot='',req=[]):
	if bot:
		url = f'https://asf.novanoir.cn/Api/{par}/{bot}?password={pw}'
	else:
		url = f'https://asf.novanoir.cn/Api/{par}?password={pw}'
	try:
		with requests.get(url, timeout=20) as resp:
			res = resp.json()
			return res['Result']
	except:
		return False
		
def asf_addBot(bot,owner):
	path = os.path.join(getConfigPath(),f'{bot}.cfg')
	data = asf_re('Bot',bot)
	if data:
		with open(path,'w') as config:
			data.update({'Owner':str(owner)})
			config.write(json.dumps(data,indent=2))
	
	
def getConfigPath():
	if os.path.isdir('hoshino'):
		return os.path.abspath('hoshino/modules/ASF_Plus/config')
	else:
		return os.path.abspath('config')
