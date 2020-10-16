import re

from app.aiorequests import get, post
from app.aio_asf import AioAsf, generate_url
from app.asfbot import asfbot
from hoshino import Service
from nonebot import MessageSegment


sv = Service('aio_asf')

@sv.on_message()
async def main(bot,ctx):
    raw = ctx['raw_message'].lower().split(' ')
    if re.match('aasf',raw[0]):
        if len(raw) == 2:
            b = asfbot(raw[1])
            stat = await b.playing_Info()
            if stat:
                msg = stat.get('now_playing').get('game')
                msg += MessageSegment.image(stat.get('now_playing').get('gicon')) + '\n\nRecently:\n'
                msg.join('{}\n 2week:{}\n'.format(i.get('name'),str(i.get('playtime_2weeks')/60)) for i in stat.get('recent'))
                await bot.send(ctx,msg)
    