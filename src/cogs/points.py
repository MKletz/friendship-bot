import re
from discord.ext import commands

class Points(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.userDict = {}

    @commands.command()
    async def p(self, ctx) -> None:
        """
        modifies points of the mentioned friends(s)
        :param ctx: discord context object
        :return: None
        """

        amount = int(re.search(r"(?![^<]*>)-?\d+",ctx.message.content).group(0))

        for friend in ctx.message.mentions:
            if friend.mention not in self.userDict.keys():
                self.userDict[friend.mention] = 0

            self.userDict[friend.mention] += amount
            message = (f'{friend.mention} now has {self.userDict[friend.mention]} friendship points.')
            await ctx.message.channel.send(message)

def setup(bot):
    bot.add_cog(Points(bot))
