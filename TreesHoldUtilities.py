import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import random
import string
import time
import os
import youtube_dl
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
import math
import asyncio
import aiohttp
import json
from random import randint
import traceback
import sqlite3
import sys
import datetime
import traceback
from urllib.parse import quote
import validators
from discord.ext.commands.cooldowns import BucketType
from time import gmtime, strftime
#Perms
Bot = commands.Bot(command_prefix= '.')

#Council = has_role("░▒▓█ Совет-О5 █▓▒░")
#FManager = has_role("░▒▓█ Менеджер объекта █▓▒░")
#SZManager = has_role("►Senior zone manager◄")
#Sponsor = has_role("░▒▓█ Sponsor █▓▒░")
#admin = has_role("►Zone manager◄")
#moderator = has_role("►MTF Unit◄")

#Perms end

ban_message_id = 0
def buildblock(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


client = discord.Client()

bot = Bot
#bot.remove_command("help")


global count
count = 0

@Bot.event
async def on_ready():
    print(">>Bot started.")
    b = buildblock(16)
    a = "Password for debug created. Password: " + b
    print(">>" + a)
    global passwd
    passwd = b
    from discord import opus

#Member warn start

@Bot.command(pass_context=True)
@commands.has_role("Ban report permission")
async def warn(ctx, member : discord.Member,*, reason : str):
    emb=discord.Embed(title=f"Стоять! Руки вверх!", description="Вам выдано предупреждение!")
    emb.add_field(name="Причина:", value=reason)
    await member.send(embed=emb)
    await ctx.send("✅ Предупреждение выдано!")

#Member warn end

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_role("Ban report permission")
async def banrep(ctx, usr, time, *, rule):
    usr = str(usr)
    time = str(time)
    rule = str(rule)
    Emb = discord.Embed(title=f"Выдан бан игроку " + usr, colour = discord.Color.purple())
    author = ctx.author
    Emb.add_field(name="Срок", value=time, inline=True)
    Emb.add_field(name="По причине", value=rule, inline=True)
    await ctx.send(embed=Emb)
    print("Issued ban report. Report arguments: ", usr, time, rule)

#Начало группы vote_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_role("Vote permission")
async def startvote(ctx, *, content):
    #channel = ctx.channel
    emb = discord.Embed(title=f'Голосование начато.', description='Голосуем за: ' + str(content),
                                  colour=discord.Color.purple())
    message = await ctx.send(embed=emb)
    print('>>Started voting. Voting about: ' + str(content))
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    global message_id # Если используется класс, то необходимо создать в классе переменную
    message_id = message.id # Сохраняем id сообщения для голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_role("Vote permission")
async def endvote(ctx):
    channel = ctx.channel
    emb = discord.Embed(title=f'До конца голосования осталось 10 секунд!', description='Успей отдать свой голос!')
    await ctx.send(embed=emb)
    time.sleep(10)
    message = await channel.fetch_message(message_id) # Ищем сообщение
    # Фильтруем реакции, чтобы остались только нужные
    resactions = [reaction for reaction in message.reactions if reaction.emoji in ['✅', '❌']]
    # Превращаем результат голосования в строку (вычитаем 1 из количества, значение по умолчанию)
    result = ''
    for reaction in resactions:
        result += reaction.emoji + ": " + str(reaction.count - 1)
    emb = discord.Embed(title=f'Результат.', description='Голоса: ' + str(result),
                                  colour=discord.Color.purple())
    print('>>Voting finished. Result: ' + str(result))
    await ctx.send(embed=emb)
#Конец группы vote_commands

#Начало группы vote_event_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_role("Vote permission")
async def starteventvote(ctx, content):
    #channel = ctx.channel
    emb = discord.Embed(title=f'Голосование за ивент.', description='Ивент: ' + str(content),
                                  colour=discord.Color.purple())
    message = await ctx.send(embed=emb)
    print('>>Voting for event started. Voting for: ' + str(content))
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    global message_id # Если используется класс, то необходимо создать в классе переменную
    message_id = message.id # Сохраняем id сообщения для голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
@commands.has_role("Vote permission")
async def endeventvote(ctx):
    channel = ctx.channel
    message = await channel.fetch_message(message_id) # Ищем сообщение
    # Фильтруем реакции, чтобы остались только нужные
    resactions = [reaction for reaction in message.reactions if reaction.emoji in ['✅', '❌']]
    # Превращаем результат голосования в строку (вычитаем 1 из количества, значение по умолчанию)
    result = ''
    for reaction in resactions:
        result += reaction.emoji + ": " + str(reaction.count - 1)
    emb = discord.Embed(title=f'Результат.', description='Итог голосования: ' + str(result),
                                  colour=discord.Color.purple())
    print('>>Voting for event finished. Result: ' + str(result))
    await ctx.send(embed=emb)
#Конец группы vote_event_commands

#Начало группы coronavirus
@Bot.command(pass_context=True)
async def cough(ctx):
    emb = discord.Embed(title="Корова с вирусом!", description="У нас человек кашляет! Вызывайте скорую", colour=discord.Color.purple())
    await ctx.send(embed=emb)
    time.sleep(10)
    emb = discord.Embed(title="Корова с вирусом!", description="Мы всё обработали, вируса тут больше нет(если конечно ещё никто не будет кашлять)", colour=discord.Color.purple())
    await ctx.send(embed=emb)

@Bot.command(pass_context=True)
async def scp500(ctx):
    emb = discord.Embed(title="Корова с вирусом!", description="Вы выпили SCP-500.", colour=discord.Color.purple())
    await ctx.send(embed=emb)
    time.sleep(10)
    emb = discord.Embed(title="Корова с вирусом!", description="Ух тыж, коровы с вирусом больше у вас нет.")
    await ctx.send(embed=emb)
#Конец группы coronavirus

#Начало группы OwnerTroll
@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def tnexit(ctx, num, *, passd):
    num = int(num)
    if passd == passwd:
        for i in range(num, 1, -1):
            emb = discord.Embed(title=f"Tactical nuke INCOMING in T-minus " + str(i) + " seconds!", description="RUN AWAY!!!", colour=discord.Color.purple())
            print(">>Tactical nuke engaged. Bot shutdown in T-" + str(i) + " seconds")
            await ctx.send(embed=emb)
            time.sleep(1)
        emb = discord.Embed(title=f"Tactical nuke INCOMING in T-minus " + "1" + " second!", description="RUN AWAY!!!", colour=discord.Color.purple())
        print(">>Tactical nuke engaged. Bot shutdown in T-" + "1" + " second!")
        await ctx.send(embed=emb)
        time.sleep(1)
        emb = discord.Embed(title=f"BOOM", description="We r ded", colour=discord.Color.purple())
        await ctx.send(embed=emb)
        exit(">>Bot destroyed by tactical nuke.")
    else:
        emb = discord.Embed(title=f"Unable to engage nuke!", description="Invalid launch key!")
        await ctx.send(embed=emb)
#Конец группы OwnerTroll

#Начало группы help

@Bot.command(pass_context=True)
async def commands(ctx):
    emb = discord.Embed(title=f"Страница команд.", description="Тут находится список всех команд бота(их мало)")
    emb.add_field(name="help", value="Эта команда")
    emb.add_field(name="cough", value="Покашлять(но не делайте это в реальной жизни, ок да?")
    emb.add_field(name="startvote/starteventvote", value="Начало голосования/голосования за ивент")
    emb.add_field(name="endvote/endeventvote", value="Конец голосования/голосования за ивент")
    emb.add_field(name="scp500", value="Если вы болеете короной, выпейте это чудесное средство!")
    emb.add_field(name="tnexit", value="Завершает скрипт бота. Не выполняет своей функции, т.к. хостинг постоянно его перезапускает!")
    await ctx.send(embed=emb)

#Конец группы help

#Debug section
@Bot.command(pass_context=True)
async def debug(ctx, *, code):
	if code == passwd:
		emb = discord.Embed(title=f"Debug menu.", description="Vars required to be verified")
		emb.add_field(name="Nothing", value="*Cricket noises*")
		await ctx.send(embed=emb)
	else:
		emb = discord.Embed(title=f"Invalid dev_code!", description="Check the logs and retry!")
		await ctx.send(embed=emb)

#SourceCode section

@Bot.command(pass_context=True)
async def source(ctx):
	emb = discord.Embed(title=f"Here we go", description="Исходный код тут: https://github.com/artv15/Treeshold-utilities")
	await ctx.send(embed=emb)

#SourceCode end

#Channel create

#@Bot.command(pass_context=True)
#async def create_room(ctx, type, *, name):
#	guild = ctx.guild
#	if type == "voice":
#		overwrite = {
#		guild.me: discord.PermissionOverwrite(manage_permissions=True)
#		}
#		await guild.create_voice_channel(str(name), overwrites=overwrite, category=765101437793337344)
#	elif type == "text":
#		overwrite = {
#		guild.me: discord.PermissionOverwrite(manage_permissions=True)
#		}
#		await guild.create_text_channel(str(name), overwrites=overwrite, category=765101437793337344)

#Channel create end

#Debug section

#Music section

@Bot.command(pass_context=True, brief="Подключается в вашему каналу", aliases=['j', 'jo'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Вы не находитесь в канале!")
        return
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"Присоединился к {channel}")

@Bot.command(pass_context=True, brief="Проиграет песню по [url]'", aliases=['pl'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Дождитесь окончания текущей песни или выполните команду 'leave'!")
        return
    await ctx.send("Секундочку(это не может занять минуту или две)")
    print(">>Music: Someone wants to play music let me get that ready for them...")
    voice = get(Bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()

@Bot.command(pass_context=True, brief="Tactical nuke INCOMIIIING!!!")
async def nuke(ctx):
	opus._load_default()
	voice = get(Bot.voice_clients, guild=ctx.guild)
	voice.play(discord.FFmpegPCMAudio("TN.mp3"))
	voice.volume = 100
	voice.is_playing()

@Bot.command(pass_context=True, brief="Makes the bot leave your channel", aliases=['l', 'le', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Вышел из {channel}")
    else:
        await ctx.send("Не думаю, что я в канале...")
#Music end

#Voice start

client = discord.Client()

bot = Bot
bot.remove_command("help")

initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

#Voice end



#Hey! Look here!
#Treeshold says: Чувак, тебе прям так интересен код бота? Не знал что это кому-то и нужно...
#Если что, можешь спокойно пиздить его отсюда, но токена тут нет, да если бы и был, то дискорд мне бы уже написал про токен
#Раз 300!(100% не отсылка к трактористу)
#bc 10 <color=red>[SERVER] Treeshold is gay</color> - ©Treeshold#0218

Bot.run(os.environ.get("BOT_TOKEN"))