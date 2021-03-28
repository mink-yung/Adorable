import base64
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='')
fake = "T0RJME5UUXhORFU1TmpZek1ESTRNak0wLllGdzRFdy5vM3I2WHYyLUFhNHpBNFpXbXI3TmN1T1F2a3c="
secret_code = base64.b64decode(fake)
print(secret_code.decode("ascii"))
TOKEN = secret_code.decode("ascii")

bad_word=['시발', '씨발', '씨빨', '시빨', 'ㅅ1발', '쉬빨', '시123발', '십팔',
       '새끼', '개객끼', '개샛기'
       '병신', '병1신', '병진', '병쉰', '예원쟝']


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('아파'))
    print('알림!!어도라가 성공적으로 구동되었습니다!!!')


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    await bot.process_commands(msg)


@bot.event
async def on_message(ctx):
    fleg=False
    if ctx.author.bot:
        return
    for i in bad_word:
        if i in ctx.content:
            fleg=True
            await ctx.delete()
    if fleg:
        await ctx.channel.send("욕은 나쁘댓서 씨빨새끼야!!")




@bot.command(aliases=['안녕'])
async def hello(ctx):
    await ctx.channel.send('안녕!')


@bot.command(aliases=['기현이', '전기현', '기현'])
async def gihyeon(ctx):
    await ctx.channel.send('나나난나ㅏ 나 그거 알아!!수원의 카사노바!!')


@bot.command(aliases=['알려줘', '도움말'])
async def dora_inform(ctx):
    await ctx.channel.send('도라는 아직 배우는중이야! 나중에 알려주께!')


@bot.command(aliases=['도라야', '어도라', '도라'])
async def hey_adora(ctx):
    await ctx.channel.send('웅!도라 여기떠!!')



@bot.command(aliases=['삭제'])
async def delete(ctx, num: int = 1):
    await ctx.channel.purge(limit=num)
    await ctx.channel.send('비밀이양!!')


bot.run(TOKEN)
