import os

from sqlitedict import SqliteDict


class Sqlite(object):
    def __init__(self,path):
        self.path = path
        self.isExist = os.path.isfile(self.path)
        self.sqlite = SqliteDict(self.path, autocommit=True)