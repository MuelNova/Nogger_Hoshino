import json
import re
import requests

steamKey = ''

class Steam(object):
	def __init__(self,user=''):
		if user:
			self.user = self.regUser(user)
			
		
	def getApi(self,r_url):
		'''
		r_url: 参数链
					e.g.  ISteamUser/GetPlayerSummaries/v0002/?steamids={user}
		'''
		url = f'http://api.steampowered.com/{r_url}&key={steamKey}'
		try:
			r = requests.get(url, timeout=20)
			return json.loads(r.text)['response']
		except:
			return False
			
		
	def getSteamConfig(self,user=''):
		if (not user) and self.user:
			user = self.user
		elif not user:
			return False

		url = f'ISteamUser/GetPlayerSummaries/v0002/?steamids={user}'
		result = self.getApi(url)
		try:
			return result['players'][0]
		except:
			return {}
		
	
	def getAvatar(self,size=0,user=''):
		'''
		获取steam头像
		size:0（默认值）Full
			   1 中
			   2 小
		'''
		rawData = self.getSteamConfig(user)
		avatarSize = ['avatarfull','avatarmedium','avatar']
		try:
			pass
		except:
			size = 0
		try:
			return rawData[avatarSize[size]]
		except:
			return False
	
	
	def getPlaying(self,user=''):
		'''
		获取正在游玩
		返回 '名称','gid'
		'''
		rawData = self.getSteamConfig(user)
		if rawData.get('gameextrainfo'):
			return rawData.get('gameextrainfo'),rawData.get('gameid')
		return '',0
	
	def getSteamProfile(self,user=''):
		'''
		获取个人资料链接（优先返回自定义链接）
		'''
		rawData = self.getSteamConfig(user)
		try:
			return rawData['profileurl']
		except:
			return False
			
			
	def getSteamName(self,user=''):
		'''
		获取个人资料链接（优先返回自定义链接）
		'''
		rawData = self.getSteamConfig(user)
		try:
			return rawData['personaname']
		except:
			return False
			
	
	def regUser(self,user):
		'''
		通过不同SteamLink返回对应64位ID
		'''
		if user == '0':
			return '0'
		if re.match('7656119[0-9]+', user):
			#64Bit
			return user
		if reg := re.search('^https://steamcommunity.com/([a-zA-Z]*)/(\S+?)/*$',
		                    user):
			if re.search('[0-9]+', reg[2]):
					#64Bit
				return reg[2]
			user = reg[2]

		#Custom to 64Bit
		url = f'ISteamUser/ResolveVanityURL/v0001/?vanityurl={user}'
		result = self.getApi(url)
		if result and result['success'] == 42:
			return False
		return result['steamid']
			
#Debug, del it when release


#test = Steam('nova_noir')
'''
print(test.user)
print(test.regUser('https://steamcommunity.com/profiles/76561197963299487'))
print(test.regUser('nova_noir'))
print(test.regUser('76561197963299487'))
'''
#print(test.getSteamConfig())
'''
print(test.getAvatar(size=5))
'''