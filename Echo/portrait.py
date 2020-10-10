import asyncio
import re
import random
import os
import datetime
import hoshino
from hoshino import Service
from .app.util import isReply, getReply

sv = Service('portrait',help_ = '每日定期更换头像',enable_on_default=False)

@sv.on_message()
async def portrait(bot,ctx):
    result = await isReply(ctx['raw_message'])
    if result and result.group(2).strip().upper() == 'PORTRAIT':
        await bot.set_group_portrait(group_id=ctx['group_id'],file='file:////home/qqbot/NiggerBot/res/portraits/{}'.format(random.choice(os.listdir('/home/qqbot/NiggerBot/res/portraits/'))))
        
        
@sv.scheduled_job('cron',hour='0')
async def portrait_sche():
    grps = await sv.get_enable_groups()
    t = str(datetime.date.today().weekday())
    for k in grps:
        await asyncio.sleep(10)
        await sv.getbot.set_group_portrait(group_id=k,file=f'file:////home/qqbot/NiggerBot/res/portraits/{t}.jpg')