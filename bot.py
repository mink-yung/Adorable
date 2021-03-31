import base64
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='도라야 ')
fake = "T0RJME5UUXhORFU1TmpZek1ESTRNak0wLllGdzRFdy5vM3I2WHYyLUFhNHpBNFpXbXI3TmN1T1F2a3c="
secret_code = base64.b64decode(fake)
print(secret_code.decode("ascii"))
TOKEN = secret_code.decode("ascii")

bad_word = ['지랄', '시발', '시123발', '십팔', '새끼', '개객끼', '개샛기', '병신', '병1신', '병진', '병쉰', '병123신', '시발',
            '씨발', '씨빨', '시빨', 'ㅅ1발', '쉬빨']


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('귀여운척'))
    print('알림!!어도라가 성공적으로 구동되었습니다!!!')


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    await bot.process_commands(msg)


@bot.listen()
async def on_message(ctx):
    if ctx.author.bot:
        return
    for i in bad_word:
        if i in ctx.content:
            await ctx.delete()
            await ctx.channel.send("욕은 나쁘댓서 씨빨새끼야!!")
            break


@bot.command(aliases=['안녕', '반가워', '반갑당'])
async def hello(ctx):
    await ctx.channel.send('웅 안녕!')


@bot.command(aliases=['한예원', '예원쟝', '예원'])
async def kdk(ctx):
    await ctx.channel.send('오잉? 아빠친구다!!')


@bot.command(aliases=['기현이', '전기현', '기현'])
async def gihyeon(ctx):
    await ctx.channel.send('나나난나ㅏ 나 그거 알아!!수원의 카사노바!!')


@bot.command(aliases=['알려줘', '도움말'])
async def dora_inform0(ctx):
    await ctx.channel.send('도라가 아직 부족하지만,,,, 이거는 할 수 있어!!'
                           '\n-도라한테 말할때는 도라야(공백)하고싶은말 치면 대답해줄게!'
                           '\n-삭제(공백)지울갯수 치면 도라가 그만큼 지워줄게!! 당연히 내용은 비밀보장이야><'
                           '\n-도라는 욕은 나쁜거라구 배웠어ㅡㅡ. 욕하면 혼내줄거야!'
                           '\n-도라에 대해 궁금하면, 도라는 누구야? 라고 물어봐줘!'
                           '\n-도라가 대답 안하면,,,,좀만 기다리면 배워올수도..?')


@bot.command(aliases=['누구야?'])
async def dora_inform(ctx):
    await ctx.channel.send('도라는 해랑님이 만드신 친구봇이야!\n도라 생일은 아빠랑 똑같은 3월 25일이구,'
                           '\n도라는 여자야! 그리구 또,,,,도라MBTI는 ENFP야! 엄마랑 똑같아!!')


@bot.command(aliases=['도라에몽'])
async def dora_angry(ctx):
    await ctx.channel.send('야!!!!지금 그딴 너구리랑 도라를 비교하는거야??(쒸익쒸익)')


@bot.command(aliases=['화났어?'])
async def dora_angry2(ctx):
    await ctx.channel.send('도라는 화같은거 안내거든요....흥')


@bot.command(aliases=['돌았어', '도라', '바보냥', '바보', '멍청이'])
async def dora_angry3(ctx):
    await ctx.channel.send('놀리지마 멍충아 ㅗㅗ')


@bot.command(aliases=['엄마는?'])
async def dora_inform3(ctx):
    await ctx.channel.send('해랑님!')


@bot.command(aliases=['아빠는?'])
async def dora_inform4(ctx):
    await ctx.channel.send('조찐따!')


@bot.command(aliases=['남친있어?', '남친'])
async def dora_inform5(ctx):
    await ctx.channel.send('어,,,, 일단 넌 아닐걸ㅋㅋ..')


@bot.command(aliases=['이쁜짓!', '이쁜짓'])
async def dora_inform6(ctx):
    await ctx.channel.send('뀨><')


@bot.command(aliases=['누구꺼야?', '주인', '누구꺼'])
async def dora_inform7(ctx):
    await ctx.channel.send(';;난 내꺼야')


@bot.command(aliases=['사귀자', '사귈래?', '좋아해', '결혼하자'])
async def dora_inform8(ctx):
    await ctx.channel.send('아빠보다 못생긴 남자는 시러시러! 퉤!!')


@bot.command(aliases=['조수빈', '수빈', '수빈이', '빈'])
async def papa(ctx):
    await ctx.channel.send('아빠 사랑행♥♥')


@bot.command(aliases=['왔어?'])
async def hey_adora(ctx):
    await ctx.channel.send('웅!도라 여기떠!!')


@bot.command(aliases=['박민경', '민경', '해랑'])
async def mama(ctx):
    await ctx.channel.send('엄마 안녕!!')


@bot.command(aliases=['김동규', '김똥꾸', '동듀', '김동듀', '동규'])
async def kimddong(ctx):
    await ctx.channel.send('삼촌안녕 ~,~')


@bot.command(aliases=['삭제'])
async def delete(ctx, num: int = 1):
    await ctx.channel.purge(limit=num)
    await ctx.channel.send('비밀이양!!')


bot.run(TOKEN)
