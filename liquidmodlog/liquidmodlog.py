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

class liquidmodlog:
    """liquidmodlog"""
    
    def __init__(self, bot):
        self.bot = bot

    def channel(self):
        c = self.bot.get_channel('439026223025225730')
        return c
        
    async def on_message_edit(self, before, after):
        if before.author.id != '413945138914656276':
            name = message.author
            name = " ~ ".join((name.name, name.nick)) if name.nick else name.name
            delmessage = discord.Embed(description=name, colour=discord.Color.purple())
            infomessage = "A message by owo __{}__, was deleted in {}".format(
                message.author.nick if message.author.nick else message.author.name, message.channel.mention)
            delmessage.add_field(name="Info:", value=infomessage, inline=False)
            delmessage.add_field(name="Message:", value=cleanmsg)
            delmessage.set_footer(text="User ID: {}".format(message.author.id))
            delmessage.set_author(name=time.strftime(fmt) + " - Deleted Message", url="http://i.imgur.com/fJpAFgN.png")
            delmessage.set_thumbnail(url="http://i.imgur.com/fJpAFgN.png")
        
def setup(bot):
    n = liquidmodlog(bot)
    bot.add_cog(n)
