#run.py
import nest_asyncio
nest_asyncio.apply()
 
import asyncio, discord, random
from dice import *
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

Token = "{토큰}"

@bot.event
async def on_ready():
    print("We have loggedd in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Game(name="$추첨"))

@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임 결과", color = _color)
    embed.add_field(name = "1번", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = "2번", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.command()
async def 추첨(ctx, count=0):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        members = channel.members
        connect_members = []
        if count != 0:
            for i in range (count):
                for member in members:
                    connect_members.append(member.id)
                rand_user = random.choice(connect_members)
                await ctx.send(f':tada: 당첨 :trophy: <@{rand_user}>')
        else:
            await ctx.send("추첨할 인원수를 입력해주세요.")
    else:
        await ctx.send("음성 채널에 접속하여 사용해주세요.")

@bot.command()
async def 뽑기(ctx, count=0):
    if count != 0:
        rand = random.randint(1, count)
        await ctx.send(f"{rand}번")
        print("[LOG] : Random choice command is activate")
    else:
        await ctx.send("뽑을 최대 인원수를 입력해주세요.")

@bot.command()
async def send(ctx, message):
    await ctx.send(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다.")

bot.run(Token)

