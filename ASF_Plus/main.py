from .app.basic import asfbot
from .app.asf_plus import  ASF_Plus
from .app.database import db
from hoshino import *
from nonebot import *
import re

sv = Service('asf_plus', help_='''发送asf_help获取详情''', bundle='ASF')


# 填写主人QQ
master = [4050909]
bindCommand = ['bind','绑定','Bind','绑','BIND']
findCommand = ['查','查询','Find','Search','find','search']
delCommand = ['删','删除']
startCommand = ['开启','开']
stopCommand = ['停止','停','关闭','关']
setDefaultCommand = ['设置默认','默认']

@sv.on_command('ASF',aliases=['asf','asfbot'],only_to_me=False)
async def e(session):
	msg = session.current_arg
	sender = str(session.ctx['user_id'])
	para = msg.split(' ')
	if len(para) >= 1:
		datab = db(sender)
		# 开启Bot
		if para[0] in startCommand:
			if datab.get('defaultBot') and len(para) == 1:
				abot = ASF_Plus(datab.get('defaultBot'))
				await session.send(abot.bot + ': 正在启用Bot...')
				await abot.th_startBot(session)
				return
				
			
			elif len(para) >= 2 and len(para) <= 3:
				abot = ASF_Plus(para[1])
				if (datab.get('bot') and para[1] in datab.get('bot')) or int(sender) in master:
					await session.send(abot.bot + ': 正在启用Bot...')
					if len(para) == 3:
						await session.send(abot.startBot(para[2]))
					else:
						await session.send(abot.startBot())
				else:
					await session.send('不是你的Bot你开你妈')
				return
					
		# 关闭Bot
		elif para[0] in stopCommand:
			if datab.get('defaultBot') and len(para) == 1:
				abot = ASF_Plus(datab.get('defaultBot'))
				await session.send(abot.bot + ': 正在关闭Bot...')
				await session.send(abot.stopBot())
				return

			if len(para) == 2:
				if (datab.get('bot') and para[1] in datab.get('bot')) or int(sender) in master:
					abot = ASF_Plus(para[1])
					await session.send(abot.bot + ': 正在关闭Bot...')
					await session.send(abot.stopBot())
				else:
					await session.send('不是你的BOT你停你妈')
				return
			
		#设置默认Bot
		
		elif para[0] in setDefaultCommand:
			if len(para) == 2:
				abot = ASF_Plus(para[1])
				if datab.get('bot') and para[1] in datab.get('bot'):
					datab.set('defaultBot',abot.bot)
					await session.send(f'已成功将{abot.bot}设置为' + MessageSegment.at(int(sender)) + '的默认Bot')
				else:
					await session.send(f'ERROR: {para[1]}并不属于{sender}')
				return
					
		elif para[0] in bindCommand:
			if len(para) >= 2 and len(para) <= 3:
				if len(para) == 3 and int(sender) in master:
					sender = para[2]
					datab = db(sender)
				abot = ASF_Plus(para[1])
				if not 'err' in abot.getBot():
					botd = db('Bot')
					if botd.get(para[1]):
						await session.send(f'ERROR:{abot.bot} 已经被绑定到{botd.get(para[1])}')
					else:
						botd.set(para[1],sender)
						if datab.get('bot'):
							bots = datab.get('bot')
						else:
							bots = set()
							datab.set('defaultBot',para[1])
						bots.add(para[1])
						datab.set('bot',bots)
						await session.send(f'成功: {abot.bot} 已经被绑定到' + MessageSegment.at(int(sender)))
				else:
					await session.send('ERROR: ' + abot.getBot()['err'])
				return
						
		elif para[0] in delCommand:
			if len(para) == 2:
				
				botd = db('Bot')
				if botd.get(para[1]):
					if sender == botd.get(para[1]) or int(sender) in master:
						await session.send(f'完成！{para[1]} 不再属于{botd.get(para[1])}')
						datab = db(botd.get(para[1]))
						bots = datab.get('bot')
						bots.discard(para[1])
						datab.set('bot',bots)
						botd.set(para[1])
						if datab.get('defaultBot') and para[1] == datab.get('defaultBot'):
							datab.set('defaultBot')
					else:
						await session.send(f'ERROR: {para[1]} 并不属于你')
				else:
					await session.send(f'ERROR: 没有Bot {para[1]} 噢')
				return
		await session.send('ERROR：参数错误！请查询\nhttps://github.com/the-25th-Nova/Nogger_Hoshino\n查看所有命令')
		
			
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