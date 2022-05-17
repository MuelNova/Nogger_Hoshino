import re
try:
    from .app.aiorequests import get, post
    from .app.aio_asf import AioAsf, generate_url
    from .app.asfbot import asfbot
except:
    from app.aiorequests import get, post
    from app.aio_asf import AioAsf, generate_url
    from app.asfbot import asfbot
from hoshino import Service
from nonebot import MessageSegment


sv = Service('aio_asf')

@sv.on_message()
async def main(bot,ctx):
    raw = ctx['raw_message'].split(' ')
    if re.match('aasf', raw[0].lower()) and len(raw) == 2:
        await bot.send(ctx, f'马上就用魔法查询{raw[1]}～')
        b = asfbot(raw[1])
        stat = await b.playing_Info()
        if stat:
            msg = stat.get('now_playing').get('game')
            msg += MessageSegment.image(stat.get('now_playing').get('gicon')) + '\n\nRecently:\n'
            msg_r = ''.join('{}\n     Last_2weeks:{}h\n    Total_played:{}h\n\n'.format(i.get('name'),str(round(i.get('playtime_2weeks')/60,1)),str(round(i.get('playtime_forever')/60,1))) for i in stat.get('recent'))
            await bot.send(ctx,msg + msg_r)
        else:
            await bot.send(ctx,'魔法书里找不到这个人的信息呢')
    