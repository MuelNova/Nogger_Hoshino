try:
	from .ASF import ASF
	from .Steam import  Steam
except:
	from ASF import ASF
	from Steam import  Steam
from threading import Thread

password = '填写ASF IPCPassword在这（没有则不填）'
url = '填写ASF链接在这'

class ASF_Plus(ASF):
	def __init__(self,bot):
		self.bot = bot
		super().__init__(url, password)
		
		
		try:
			self.steamID = self.getBot()['SteamID']
		except:
			self.steamID = 0
		
	def startBot(self,tfa=''):
		return f'{self.bot}: {str(self.bot_login(self.bot,tfa))}'
	
	def stopBot(self):
		return f'{self.bot}: {str(self.bot_stop(self.bot))}'
	
	def getBot(self):
		return self.bot_get(self.bot)
		
	async def th_startBot(self,session,tfa=''):
		th1 = Thread(target=self.startBot, args=(session,tfa))
		await th1.start()
		
		
# print(ASF_Plus('nova').steamID)