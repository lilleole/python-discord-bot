from discord.ext import commands
import discord
import os
import random


class sendMeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="sendMeme", description="send a random meme from the meme folder")
    async def sendMeme(self, ctx):
        dir = "src/memes"
        list = os.listdir(dir)
        random.shuffle(list)
        file = list[random.randrange(0, len(list) - 1)]
        with open(os.path.join(dir, file), "rb") as f:
            await ctx.send(file=discord.File(f))


def setup(bot):
    bot.add_cog(sendMeme(bot))
