import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import random
from random import choice
from copy import deepcopy
from random import randint
from random import choice as randchoice
import base64
import json
import aiohttp
import itertools
import datetime

class liquidmodlog:
    """liquidmodlog"""
    
    def __init__(self, bot):
        self.bot = bot

    def channel(self):
        c = self.bot.get_channel('439026223025225730')
        return c
        
    async def on_message_edit(self, before, after):
        if before.author.id != '413945138914656276':
            if before.content == after.content:
                return
        if before.author.bot:
            return
        cleanbefore = before.content
        for i in before.mentions:
            cleanbefore = cleanbefore.replace(i.mention, str(i))
        cleanafter = after.content
        for i in after.mentions:
            cleanafter = cleanafter.replace(i.mention, str(i))
        channel = db[server.id]["Channel"]
        time = datetime.datetime.now()
        fmt = '%H:%M:%S'
        name = before.author
        name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
        delmessage = discord.Embed(description=name, colour=discord.Color.green())
        infomessage = "A message by owo __{}__, was edited in {}".format(
            before.author.nick if before.author.nick else before.author.name, before.channel.mention)
        delmessage.add_field(name="Info:", value=infomessage, inline=False)
        delmessage.add_field(name="Before Message:", value=cleanbefore, inline=False)
        delmessage.add_field(name="After Message:", value=cleanafter)
        delmessage.set_footer(text="User ID: {}".format(before.author.id))
        delmessage.set_author(name=time.strftime(fmt) + " - Edited Message", url="http://i.imgur.com/Q8SzUdG.png")
        delmessage.set_thumbnail(url="http://i.imgur.com/Q8SzUdG.png")
        
def setup(bot):
    n = liquidmodlog(bot)
    bot.add_cog(n)
