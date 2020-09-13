import os
from sqlitedict import SqliteDict

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
		
