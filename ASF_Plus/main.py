from .app.basic import asfbot
from .app.asf_plus import  ASF_Plus
from hoshino import *
import re

sv = Service('asf_plus', help_='''发送asf_help获取详情''', bundle='ASF')


# 填写主人QQ
master = [4050909]
bindCommand = ['bind','绑定','Bind','绑','BIND']
findCommand = ['查','查询','Find','Search','find','search']
delCommand = ['删','删除']
startCommand = ['开启','开']
stopCommand = ['关闭','关','停止','停']

@sv.on_command('ASF',aliases=['asf','asfbot'],only_to_me=True)
async def e(session):
	msg = session.current_arg
	sender = str(session.ctx['user_id'])
	para = msg.split(' ')
	if len(para) >= 1:
		
		# 开启Bot
		if para[0] in startCommand:
			if len(para) >= 2:
				abot = ASF_Plus(para[1])
				await session.send(abot.bot + ': 正在启用Bot...')
				if len(para) >= 3:
					await session.send(abot.startBot(para[2]))
				else:
					await session.send(abot.startBot())
					
		# 关闭Bot
		if para[0] in stopCommand:
			if len(para) >= 2:
				abot = ASF_Plus(para[1])
				await session.send(abot.bot + ': 正在关闭Bot...')
				await session.send(abot.stopBot())
			
'''
	if len(para) >= 2 and para[0] in bindCommand:
		abot = asfbot(para[1])
		if int(sender) in master and len(para) >= 3:
			if abot.exist:
				abot.delBot()
			if re.match('[0-9]{5,11}',para[2]):
				abot.bind(para[2])
			elif re.match("\[CQ:at,qq=([0-9]{5,11})\]",para[2]):
				qq = re.match('\[CQ:at,qq=([0-9]{5,11})\]',para[2])
				abot.bind(qq.group(1))
			else:
				await session.send('你在绑定些🐔🐔')
			if abot.exist:
				await session.send('成功将BOT' +abot.name +'绑定到' + abot.owner)
		elif abot.exist:
			await session.send('已经绑定过了！拥有者是：' + abot.owner)
		else:
			abot.bind(sender)
			if abot.exist:
				await session.send('成功！BOT'+abot.name + '已经被绑定至'+abot.owner)
			else:
				await session.send('错误！可能没有这个BOT')
 	   		
	elif  len(para) == 2 and para[0] in findCommand:
		abot = asfbot(para[1])
		if abot.exist:
			msgChain = ''
			b_id = abot.config['SteamID']
			msgChain = msgChain + abot.config['Nickname'] + f'\n\nDestiny Report:\n★RaidReport:https://raid.report/pc/{b_id}\n★DungeonReport:https://dungeon.report/pc/{b_id}\n★DestinyTracker:https://destinytracker.com/destiny-2/profile/steam/{b_id}/overview'
			await session.send(msgChain)
		else:
			await session.send('查找不到这个bot噢')
				
	elif len(para) == 2 and para[0] in delCommand:
		abot = asfbot(para[1])
		if sender == abot.owner or int(sender) in master:
			abot.delBot()
			if not abot.exist:
				await session.send(f'删除BOT{abot.name}成功')
			else:
				await session.send('失败，请检查原因')
		else:
			await session.send('不是你的BOT你删你🐴')
		
	else:
		await session.send('错误的参数，请输入【@BOT ASF 帮助】查看使用方法')
'''
