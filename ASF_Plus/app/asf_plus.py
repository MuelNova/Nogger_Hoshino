from .ASF import ASF

class ASF_Plus(ASF):
	def __init__(self,bot):
		self.bot = bot
		super().__init__('https://asf.novanoir.cn','dalizm8881018')
		
	def startBot(self,tfa=''):
		result = f'{self.bot}: {str(self.bot_login(self.bot,tfa))}'
		return result
	
	def stopBot(self):
		result = f'{self.bot}: {str(self.bot_stop(self.bot))}'
		return result
	
	def getBot(self):
		return self.bot_get(self.bot)
		
		
