import discord
import math
import asyncio
import aiohttp
import json
import datetime
from discord.ext import commands
import traceback
import sqlite3
from urllib.parse import quote
import validators
from discord.ext.commands.cooldowns import BucketType
from time import gmtime, strftime

class cs(commands.Cog):
    def __init__(self, bot):
    	global flash
        self.Bot = flash

@commands.group
async def cs(self, ctx):
	pass

@flash.command(pass_context=True)
async def flash(self, ctx, bombsite: str):
	bombsite = lower().bombsite
	if bombsite == a or bombsite == b:
		emb = discord.Embed(title=f"ФЛЕШКА НА " + bombsite, description="Бегите нахуй", color=0x4d0000)
		log_message = await ctx.send(embed=emb)
		print("Someone issued `flash` command. Message id: " + str(log_message))
	else:
		emb = discord.Embed(title=f"блять", description="где такой плент то, а?", color=0x4d0000)

@flash.command(pass_context=True)
async def smoke(self, ctx, bombsite: str):
	bombsite = lower().bombsite
	if bombsite == a or bombsite == b:
		emb = discord.Embed(title=f"СМОУК НА " + bombsite, description="Бегите нахуй", color=0x4d0000)
		log_message = await ctx.send(embed=emb)
		print("Someone issued `smoke` command. Message id: " + str(log_message))
	else:
		emb = discord.Embed(title=f"блять", description="где такой плент то, а?", color=0x4d0000)

@flash.command(pass_context=True)
async def module(ctx):
	emb=discord.Embed(title="Автор модуля flash", description="Treeshold#0218", color=0x4d0000)
	emb.add_field(name="Автор идеи:", value="Dlorka#9909", inline=True)
	await ctx.send(embed=emb)