import base64
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='')
aa = "T0RJME5UUXhORFU1TmpZek1ESTRNak0wLllGdzRFdy5vM3I2WHYyLUFhNHpBNFpXbXI3TmN1T1F2a3c="
bb=base64.b64decode(aa)
print (bb.decode("ascii"))
TOKEN = bb.decode("ascii")
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('공부'))
    print('알림!!어도라가 성공적으로 구동되었습니다!!!')


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return None
    await bot.process_commands(msg)


@bot.command(aliases=['안녕', '도라야 안녕'])
async def hello(ctx):
    await ctx.channel.send('안녕!')


@bot.command(aliases=['도라야', '어도라', '도라'])
async def hey_adora(ctx):
    await ctx.channel.send('웅!도라 여기떠!!')


@bot.command(aliases=['기현이', '전기현', '기현'])
async def gihyeon(ctx):
    await ctx.channel.send('나나난나ㅏ 나 그거 알아!!수원의 카사노바!!')


@bot.command(aliases=['삭제'])
async def delete(ctx, num: int = 2):
    await ctx.channel.purge(limit=num)
    await ctx.channel.send('비밀이양!!')


bot.run(TOKEN)
