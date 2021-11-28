import requests
from discord.ext import commands

class Cats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def catfact(self, ctx) -> None:
        """
        returns a random cat fact
        :param ctx: discord context object
        :return: None
        """

        response = requests.get("https://catfact.ninja/fact")
        await ctx.message.channel.send(response.json()['fact'])

def setup(bot):
    bot.add_cog(Cats(bot))
