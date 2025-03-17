import os
import random
from discord.ext import commands


class shuffle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="shuffle", description="shuffles the meme folder")
    async def shuffle(self, ctx):
        dir = "src/memes"
        i = 1
        list = os.listdir(dir)
        random.shuffle(list)
        for f in list:
            file_name, file_extension = os.path.splitext(f)
            new_name = f"Unusual Videos#{i}{file_extension}"
            try:
                os.rename(os.path.join(dir, f), os.path.join(dir, new_name))
            except Exception as e:
                print(e)

            i += 1

        i = 1
        list = os.listdir(dir)
        random.shuffle(list)
        for f in list:
            file_name, file_extension = os.path.splitext(f)
            new_name = f"Unusual Videos #{i}{file_extension}"
            try:
                os.rename(os.path.join(dir, f), os.path.join(dir, new_name))
            except Exception as e:
                print(e)

            i += 1
        await ctx.send("shuffled")


def setup(bot):
    bot.add_cog(shuffle(bot))
