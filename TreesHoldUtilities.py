import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import random
import string
import time
import os

ban_message_id = 0
def buildblock(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
Bot = commands.Bot(command_prefix= '#')

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

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def banrep(ctx, usr, time, *, rule):
    usr = str(usr)
    time = str(time)
    rule = str(rule)
    Emb = discord.Embed(title=f"Выдан бан игроку " + usr, colour = discord.Color.purple())
    Emb.add_field(name="Срок", value=time, inline=True)
    Emb.add_field(name="По причине", value=rule, inline=True)
    await ctx.send(embed=Emb)
    print("Issued ban report. Report arguments: " + usr + time + rule)

#Начало группы vote_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
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
    FinalResultY = result[3]
    FinalResultN = result[7]
    if FinalResultY > FinalResultN:
        Final = 'Принято'
    elif FinalResultY == FinalResultN:
        Final = 'Голоса равны. Решение за организатором голосования.'
    elif FinalResultY < FinalResultN:
        Final = 'Отказано.'
    emb = discord.Embed(title=f'Результат.', description='Голоса: ' + str(result),
                                  colour=discord.Color.purple())
    emb.add_field(name="Итог: ", value=Final, inline=True)
    print('>>Voting finished. Result: ' + str(result) + ' Final result: ' + Final)
    await ctx.send(embed=emb)
#Конец группы vote_commands

#Начало группы vote_event_commands
message_id = 0 # Переменная для сообщения голосования

@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
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
async def endeventvote(ctx):
    channel = ctx.channel
    message = await channel.fetch_message(message_id) # Ищем сообщение
    # Фильтруем реакции, чтобы остались только нужные
    resactions = [reaction for reaction in message.reactions if reaction.emoji in ['✅', '❌']]
    # Превращаем результат голосования в строку (вычитаем 1 из количества, значение по умолчанию)
    result = ''
    for reaction in resactions:
        result += reaction.emoji + ": " + str(reaction.count - 1)
    #Посчёт результата(Принято/Отказано)
    FinalResultY = result[3]
    FinalResultN = result[7]
    if FinalResultY > FinalResultN:
        Final = 'Принято'
    elif FinalResultY == FinalResultN:
        Final = 'Голоса равны. Решение за организатором голосования.'
    elif FinalResultY < FinalResultN:
        Final = 'Отказано.'
    emb = discord.Embed(title=f'Результат.', description='Итог голосования: ' + str(result),
                                  colour=discord.Color.purple())
    emb.add_field(name="Итог: ", value=Final, inline=True)
    print('>>Voting for event finished. Result: ' + str(result) + ' Final result: ' + Final)
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
    emb = discord.Embed(title="Корова с вирусом!", description="Вы выпили SCP-500.")
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
    print(">>Receieved " + str(passd) + " as code. Corrent one: " + str(passwd))
    if passd == passwd:
        for i in range(num, 1, -1):
            emb = discord.Embed(title=f"Tactical nuke INCOMING in T-minus " + str(i) + " seconds!", description="RUN AWAY!!!")
            print(">>Tactical nuke engaged. Bot shutdown in T-" + str(i) + " seconds")
            await ctx.send(embed=emb)
            time.sleep(1)
        emb = discord.Embed(title=f"Tactical nuke INCOMING in T-minus " + "1" + " second!", description="RUN AWAY!!!")
        print(">>Tactical nuke engaged. Bot shutdown in T-" + "1" + " second!")
        await ctx.send(embed=emb)
        time.sleep(1)
        emb = discord.Embed(title=f"BOOM", description="We r ded")
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
    emb.add_field(name="tnexit", value="Завершает скрипт бота.")
    await ctx.send(embed=emb)

#Конец группы help
Bot.run(os.environ.get("BOT_TOKEN"))