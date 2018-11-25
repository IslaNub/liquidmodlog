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
            b = "**Before:**\n" \
                + "*{}*".format(before.content)
            a = "**After:**\n" \
                + "*{}*".format(after.content)
            m = "{}\n{}".format(b, a)
            await self.bot.send_message(self.channel(), m)
        
def setup(bot):
    n = liquidmodlog(bot)
    bot.add_cog(n)
