from .ASF import ASF

url = '填写你的ASF IPC面板链接'
password = '填写ASF IPC密码（没有则留空）'

class ASF_Plus(ASF):
	def __init__(self,bot):
		self.bot = bot
		super().__init__(url, password)
		
	def startBot(self,tfa=''):
		result = f'{self.bot}: {str(self.bot_login(self.bot,tfa))}'
		return result
	
	def stopBot(self):
		result = f'{self.bot}: {str(self.bot_stop(self.bot))}'
		return result
		
		
