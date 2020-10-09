import hoshino
from hoshino import Service
from .app.util import isReply, getReply

sv = Service('echo')

@sv.on_message()
async def echo(bot,ctx):
    result = await isReply(ctx['raw_message'])
    if result and result.group(2).strip().upper() == 'ECHO':
        raw_msg = await getReply(bot,result.group(1))
        await bot.send(ctx,raw_msg.replace('&#91;','[').replace('&#93;',']'))