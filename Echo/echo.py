import re
import hoshino
from hoshino import Service
from .app.util import isReply, getReply

sv = Service('echo',help_ = '在聊天中对CQ码进行实时转码发送')

@sv.on_message()
async def echo(bot,ctx):
    result = await isReply(ctx['raw_message'])
    if result and result.group(2).strip().upper() == 'ECHO':
        raw_msg = await getReply(bot,result.group(1))
        raw_msg = raw_msg.replace('&#91;','[').replace('&#93;',']')
        if re.match('\[(.*)\]',raw_msg):
            await bot.send(ctx,' え、转码？分かりました...')
            await bot.send(ctx,raw_msg.replace('&#91;','[').replace('&#93;',']'))
        else:
            await bot.send(ctx,'うむ、 这并不是我所能理解的语言呢')