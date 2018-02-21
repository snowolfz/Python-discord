import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, user : discord.Member):
        """This does stuff!"""

        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
