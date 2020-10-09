import hoshino
from hoshino import Service
from .app.util import isReply, getReply

sv = Service('echo',help='在聊天中对CQ码进行实时转码发送')

@sv.on_message()
async def echo(bot,ctx):
    result = await isReply(ctx['raw_message'])
    if result and result.group(2).strip().upper() == 'ECHO':
        await bot.send(ctx,'えぇ、 转码？じゃ...')
        raw_msg = await getReply(bot,result.group(1))
        await bot.send(ctx,raw_msg.replace('&#91;','[').replace('&#93;',']'))