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
voice = Bot
#class voice(commands.Cog):
#    def __init__(self, bot):
#        self.bot = bot
    
#@coro()
async def on_voice_state_update(self, member, before, after):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    guildID = member.guild.id
    c.execute("SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
    voice=c.fetchone()
    if voice is None:
        pass
    else:
        voiceID = voice[0]
        try:
            if after.channel.id == voiceID:
                c.execute("SELECT * FROM voiceChannel WHERE userID = ?", (member.id,))
                cooldown=c.fetchone()
                if cooldown is None:
                    pass
                else:
                    await member.send("Creating channels too quickly you've been put on a 15 second cooldown!")
                    await asyncio.sleep(15)
                c.execute("SELECT voiceCategoryID FROM guild WHERE guildID = ?", (guildID,))
                voice=c.fetchone()
                c.execute("SELECT channelName, channelLimit FROM userSettings WHERE userID = ?", (member.id,))
                setting=c.fetchone()
                c.execute("SELECT channelLimit FROM guildSettings WHERE guildID = ?", (guildID,))
                guildSetting=c.fetchone()
                if setting is None:
                    name = f"{member.name}'s channel"
                    if guildSetting is None:
                        limit = 0
                    else:
                        limit = guildSetting[0]
                else:
                    if guildSetting is None:
                        name = setting[0]
                        limit = setting[1]
                    elif guildSetting is not None and setting[1] == 0:
                        name = setting[0]
                        limit = guildSetting[0]
                    else:
                        name = setting[0]
                        limit = setting[1]
                categoryID = voice[0]
                id = member.id
                category = self.bot.get_channel(categoryID)
                channel2 = await member.guild.create_voice_channel(name,category=category)
                channelID = channel2.id
                await member.move_to(channel2)
                await channel2.set_permissions(self.bot.user, connect=True,read_messages=True)
                await channel2.edit(name= name, user_limit = limit)
                c.execute("INSERT INTO voiceChannel VALUES (?, ?)", (id,channelID))
                conn.commit()
                def check(a,b,c):
                    return len(channel2.members) == 0
                await self.bot.wait_for('voice_state_update', check=check)
                await channel2.delete()
                await asyncio.sleep(3)
                c.execute('DELETE FROM voiceChannel WHERE userID=?', (id,))
        except:
            pass
    conn.commit()
    conn.close()

@voice.command()
async def setup(self, ctx):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    guildID = ctx.guild.id
    id = ctx.author.id
    if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 151028268856770560:
        def check(m):
            return m.author.id == ctx.author.id
        await ctx.channel.send("**You have 60 seconds to answer each question!**")
        await ctx.channel.send(f"**Enter the name of the category you wish to create the channels in:(e.g Voice Channels)**")
        try:
            category = await self.bot.wait_for('message', check=check, timeout = 60.0)
        except asyncio.TimeoutError:
            await ctx.channel.send('Took too long to answer!')
        else:
            new_cat = await ctx.guild.create_category_channel(category.content)
            await ctx.channel.send('**Enter the name of the voice channel: (e.g Join To Create)**')
            try:
                channel = await self.bot.wait_for('message', check=check, timeout = 60.0)
            except asyncio.TimeoutError:
                await ctx.channel.send('Took too long to answer!')
            else:
                try:
                    channel = await ctx.guild.create_voice_channel(channel.content, category=new_cat)
                    c.execute("SELECT * FROM guild WHERE guildID = ? AND ownerID=?", (guildID, id))
                    voice=c.fetchone()
                    if voice is None:
                        c.execute ("INSERT INTO guild VALUES (?, ?, ?, ?)",(guildID,id,channel.id,new_cat.id))
                    else:
                        c.execute ("UPDATE guild SET guildID = ?, ownerID = ?, voiceChannelID = ?, voiceCategoryID = ? WHERE guildID = ?",(guildID,id,channel.id,new_cat.id, guildID))
                    await ctx.channel.send("**You are all setup and ready to go!**")
                except:
                    await ctx.channel.send("You didn't enter the names properly.\nUse `.voice setup` again!")
    else:
        await ctx.channel.send(f"{ctx.author.mention} only the owner of the server can setup the bot!")
    conn.commit()
    conn.close()

@voice.command()
async def setlimit(self, ctx, num):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 151028268856770560:
        c.execute("SELECT * FROM guildSettings WHERE guildID = ?", (ctx.guild.id,))
        voice=c.fetchone()
        if voice is None:
            c.execute("INSERT INTO guildSettings VALUES (?, ?, ?)", (ctx.guild.id,f"{ctx.author.name}'s channel",num))
        else:
            c.execute("UPDATE guildSettings SET channelLimit = ? WHERE guildID = ?", (num, ctx.guild.id))
        await ctx.send("You have changed the default channel limit for your server!")
    else:
        await ctx.channel.send(f"{ctx.author.mention} only the owner of the server can setup the bot!")
    conn.commit()
    conn.close()

@voice.command()
async def lock(self, ctx):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} You don't own a channel.")
    else:
        channelID = voice[0]
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        channel = self.bot.get_channel(channelID)
        await channel.set_permissions(role, connect=False,read_messages=True)
        await ctx.channel.send(f'{ctx.author.mention} Voice chat locked! 🔒')
    conn.commit()
    conn.close()

@voice.command()
async def unlock(self, ctx):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} You don't own a channel.")
    else:
        channelID = voice[0]
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        channel = self.bot.get_channel(channelID)
        await channel.set_permissions(role, connect=True,read_messages=True)
        await ctx.channel.send(f'{ctx.author.mention} Voice chat unlocked! 🔓')
    conn.commit()
    conn.close()

@voice.command(aliases=["allow"])
async def permit(self, ctx, member : discord.Member):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} You don't own a channel.")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        await channel.set_permissions(member, connect=True)
        await ctx.channel.send(f'{ctx.author.mention} You have permited {member.name} to have access to the channel. ✅')
    conn.commit()
    conn.close()

@voice.command(aliases=["deny"])
async def reject(self, ctx, member : discord.Member):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    guildID = ctx.guild.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} You don't own a channel.")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        for members in channel.members:
            if members.id == member.id:
                c.execute("SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
                voice=c.fetchone()
                channel2 = self.bot.get_channel(voice[0])
                await member.move_to(channel2)
        await channel.set_permissions(member, connect=False,read_messages=True)
        await ctx.channel.send(f'{ctx.author.mention} You have rejected {member.name} from accessing the channel. ❌')
    conn.commit()
    conn.close()



@voice.command()
async def limit(self, ctx, limit):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} You don't own a channel.")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        await channel.edit(user_limit = limit)
        await ctx.channel.send(f'{ctx.author.mention} You have set the channel limit to be '+ '{}!'.format(limit))
        c.execute("SELECT channelName FROM userSettings WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            c.execute("INSERT INTO userSettings VALUES (?, ?, ?)", (id,f'{ctx.author.name}',limit))
        else:
            c.execute("UPDATE userSettings SET channelLimit = ? WHERE userID = ?", (limit, id))
    conn.commit()
    conn.close()


@voice.command()
async def name(self, ctx,*, name):
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    id = ctx.author.id
    c.execute("SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
    voice=c.fetchone()
    if voice is None:
        await ctx.channel.send(f"{ctx.author.mention} You don't own a channel.")
    else:
        channelID = voice[0]
        channel = self.bot.get_channel(channelID)
        await channel.edit(name = name)
        await ctx.channel.send(f'{ctx.author.mention} You have changed the channel name to '+ '{}!'.format(name))
        c.execute("SELECT channelName FROM userSettings WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            c.execute("INSERT INTO userSettings VALUES (?, ?, ?)", (id,name,0))
        else:
            c.execute("UPDATE userSettings SET channelName = ? WHERE userID = ?", (name, id))
    conn.commit()
    conn.close()

@voice.command()
async def claim(self, ctx):
    x = False
    conn = sqlite3.connect('voice.db')
    c = conn.cursor()
    channel = ctx.author.voice.channel
    if channel == None:
        await ctx.channel.send(f"{ctx.author.mention} you're not in a voice channel.")
    else:
        id = ctx.author.id
        c.execute("SELECT userID FROM voiceChannel WHERE voiceID = ?", (channel.id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} You can't own that channel!")
        else:
            for data in channel.members:
                if data.id == voice[0]:
                    owner = ctx.guild.get_member(voice [0])
                    await ctx.channel.send(f"{ctx.author.mention} This channel is already owned by {owner.mention}!")
                    x = True
            if x == False:
                await ctx.channel.send(f"{ctx.author.mention} You are now the owner of the channel!")
                c.execute("UPDATE voiceChannel SET userID = ? WHERE voiceID = ?", (id, channel.id))
        conn.commit()
        conn.close()


def setup(bot):
    bot.add_cog(voice(bot))
#Voice end

#Hey! Look here!
#Treeshold says: Чувак, тебе прям так интересен код бота? Не знал что это кому-то и нужно...
#Если что, можешь спокойно пиздить его отсюда, но токена тут нет, да если бы и был, то дискорд мне бы уже написал про токен
#Раз 300!(100% не отсылка к трактористу)
#bc 10 <color=red>[SERVER] Treeshold is gay</color> - ©Treeshold#0218

Bot.run(os.environ.get("BOT_TOKEN"))