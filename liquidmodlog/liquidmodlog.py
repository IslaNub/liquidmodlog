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
        
    @commands.command(pass_context = True)
    async def testingwork(self, ctx):
        await self.bot.say('Yeet')
        
        
def setup(bot):
    n = liquidmodlog(bot)
    bot.add_cog(n)
