import os
import re
import requests
import time


class ASF(object):
	'''
	url:IPC面板链接，基础连接即可,（如：https://asf.baidu.com）
    password:IPC配置文件中的名字,没有则不填
	'''
	def __init__(self,url,password=''):
		self.logPath = ''
		self.logInited = False
		self.initLog('/home/asf/ArchiSteamFarm/log.txt')
		if password:
			self.isAuth = True
			self.__password = password
		else:
			self.isAuth = False
		if url[-1:] != '/':
			url += '/'
		self.__url = url+'Api/'
			
	def __pathCreate(self,path):
		if self.isAuth:
			return f'{self.__url}{path}?password={self.__password}'
		return f'{self.__url}{path}'
	
	def initLog(self,path):
		'''
		注册log
		path:log文件位置
				e.g 'E:/SexyBoy/ASF/log.txt'
		'''
		if os.path.isfile(os.path.abspath(path)):
			self.logPath = os.path.abspath(path)
			self.logInited = True
			return True
		return False
		
	def generateLog(self,line=5):
		'''
		产生Log数据
		line:返回最新n条（可选）
		
		返回值： dict [['1通知类型','1对象','1函数','1返回值']['2通知类型','2对象','2函数','2返回值']]
						e.g.[['INFO', 'testAc','OnConnected()', '登录中……'], ['WARN', 'ASF', 'GetUserInput()', '收到一个用户输入请求，但进程目前正在以', 'Headless', '模式运行！'], ['ERROR', 'testAc', 'OnLoggedOn()', 'twoFactorCode', ' 无效！']]
		'''
		if self.logInited:
			with open(self.logPath, 'rb') as f:
				off = -10
				while True:
					f.seek(off, 2)
					lines = f.readlines()
					if len(lines)>= line: 
						result = []
						for i in lines:
							try:
								rer = re.search('\|ArchiSteamFarm-[0-9]+\|(.*)',i.decode())
							except Exception as e:
								rer = ''
								print(f'Error: {e}')
							if rer:
								req=rer.group(1).replace('() ','()|').split('|')
								result.append(req)
						return result[::-1]
					off *= 2
		return False
		
	def ASF_get(self,path):
		'''
		发送Get请求
		path： 请求地址
					e.g. 'Bot/匿鸽'
		
		返回值: dict 响应结果 / str 错误
		'''
		try:
			w = requests.get(self.__pathCreate(path),timeout=20)
			return w.json()
		except Exception as e:
			return '失败！请检查ASF网页、密码是否出错，并测试是否被屏蔽！'
	
	def ASF_post(self,path,req=[]):
		'''
		发送Post请求
		path： 请求地址
					e.g. 'Bot/匿鸽/Start'
		req: 数据包 （可选）
		
		返回值:dict 响应结果 / str 错误
		'''
		try:
			w = requests.post(self.__pathCreate(path),timeout=20,json=req)
			return w.json()
		except Exception as e:
			return '失败！请检查ASF网页、密码是否出错，并测试是否被屏蔽！'
			
			
	def bot_get(self,botName):
		'''
		获取一个bot的参数
		botName: bot名称
		
		返回值:dict 获取结果
		'''
		result = self.ASF_get(f'Bot/{botName}')
		if isinstance(result, str):
			pass
		elif result.get('Result') and result['Result'].get(botName):
			return result['Result'][botName]
		else:
			result = f'找不到Bot {botName}！'
		print(f'Error occured while running function {self.bot_get.__name__}:{result}')
		return {'err':result}
		
	def bot_login(self,botName,tfa=''):
		if tfa:
			tfa = tfa.upper()
			data = {'Type':'TwoFactorAuthentication','Value':tfa}
			print(f'令牌{tfa}Post...' + str(self.ASF_post(f'Bot/{botName}/Input', data)))
			time.sleep(1)
		req = self.ASF_post(f'Bot/{botName}/Start')
		result = 'Unknown Error'
		if not req.get('Success') and req.get('Message'):
			result = req.get('Message')
		print(f'登录{botName}Post...' + str(req))
		
		time.sleep(5)
		log = self.generateLog()
		for i in log:
			if i[1] == botName and i[2] == 'OnLoggedOn()':
				if i[0] == 'INFO':
					return i[3]
				elif i[0] == 'ERROR':
					return i[3]
		return 'ERROR: ' + result
		
	def bot_stop(self,botName):
		req = self.ASF_post(f'Bot/{botName}/Stop')
		result = 'Unknown Error'
		if not req.get('Success') and req.get('Message'):
			result = req.get('Message')
		print(f'停止{botName}Post...' + str(req))
		time.sleep(3)
		log = self.generateLog()
		for i in log:
			if i[1] == botName and i[2] == 'OnDisconnected()':
				if i[0] == 'INFO':
					return i[3]
		return 'ERROR:' + result
		
	def debug(self,tfa):
		data = {'Type':'TwoFactorAuthentication','Value':tfa}
		w = requests.post(self.__pathCreate('Bot/testAc/Input'),timeout=20,json=data)
		print(w.text)
		time.sleep(3)
		w = requests.post(self.__pathCreate('Bot/testAc/Stop'),timeout=20,json=[])
		print(w.text)
		
'''Debug
a=ASF('https://asf.novanoir.cn/','dalizm8881018')
if 'er' in a.bot_get('黑鬼'):
	print('Ye')
#a.debug('92VB7')
#print(a.initLog('/home/asf/ArchiSteamFarm/log.txt'))
#print(a.generateLog())
# print(a.bot_login('testAc','8RFCK'))
#print(a.bot_stop('testAc'))
print(a.ASF_post('Bot/nova/Start'))
#print(a.bot_get('nova'))'''
