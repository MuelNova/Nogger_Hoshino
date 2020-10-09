import re

async def isReply(msg):
    return re.match('^\[CQ:reply,id=(.+?)]\[CQ:at,qq=.+?\](.*)$',msg)
    
async def getReply(bot,id):
    sr = await bot.get_group_msg(message_id=int(id))
    return sr['content']
