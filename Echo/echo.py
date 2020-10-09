import hoshino
from hoshino import Service
from .app.util import isReply, isCQ

sv = Service('echo')

@sv.on_message()
async def echo(bot,ctx):
    result = await isReply(ctx['raw_message'])
    if result and result.group(2).strip() == 'echo':
        raw = await bot.get_group_msg(message_id=int(result.group(1)))
        raw_msg = raw['content']
        await bot.send(ctx,raw_msg.replace('&#91;','[').replace('&#93;',']'))