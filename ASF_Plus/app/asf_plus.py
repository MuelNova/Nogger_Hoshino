from .ASF import ASF

url = '填写ASF链接在这'
password = '填写ASF IPCPassword在这（没有则不填）'

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
	
	def getBot(self):
		return self.bot_get(self.bot)
		
		
