import re

async def isReply(msg):
    return re.match('^\[CQ:reply,id=(.+?)]\[CQ:at,qq=.+?\](.*)$',msg)
    
