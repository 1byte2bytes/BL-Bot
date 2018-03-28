import os
import random
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO


class Lewd:
    def __init__(self, bot):
        self.bot = bot

        self.hold_self = []
        self.hold_self.append('*{holder}* looks in the mirror and grabs his their own hand.')
        self.hold_self.append('*{holder}* feels lonely and wonders what it\'s like to be held by your hand.')
        self.hold_self.append('*{holder}* holds their hands together.')
        
        self.hold_person = []
        self.hold_person.append('*{holder}* secretly gets hold of *{victim}\'s* hand.')
        self.hold_person.append('*{holder}* looks *{victim}* in the eyes and grabs their hand.')
        self.hold_person.append('*{holder}* accidentally touches *{victim}\'s* hand, they like it.')
        self.hold_person.append('A spider drops, *{holder}* grabs *{victim}\'s* hand in angst.')

    @commands.command(pass_context=True, no_pm=False, name='handhold')
    async def _eat(self, context, victim: discord.Member):
        """Hold another users hand."""
        author = context.message.author
        if victim.id == author.id:
            message = str(random.choice(self.hold_self))
        else:
            message = str(random.choice(self.hold_person)).format(victim=victim.display_name, holder=author.display_name)
        await self.bot.say(message)

    @commands.command(no_pm=True, hidden=True)
    async def hug(self, user : discord.Member, intensity : int=1):
        """Because everyone likes hugs

        Up to 10 intensity levels."""
        name = italics(user.display_name)
        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        elif intensity >= 10:
            msg = "(づ￣ ³￣)づ{} ⊂(´・ω・｀⊂)".format(name)
        await self.bot.say(msg)


def setup(bot):
    bot.add_cog(Lewd(bot))