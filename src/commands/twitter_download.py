import discord
from discord.ext import commands
import twitter_downloader


class twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="twitter", description="Download a Twitter video")
    async def twitter(self, ctx, link: str):
        """Download a video from a Twitter link and send it to Discord"""
        print(f"Twitter link received: {link}")

        list = link.replace(" ", "").split(",")
        print(list)

        for i in list:
            try:
                twitter_downloader.download_twitter_video(i)
                file_path = r"/output.mp4"
                with open(file_path, "rb") as f:
                    await ctx.send(file=discord.File(f, "output.mp4"))
            except Exception as e:
                await ctx.send(e)

# Setup the cog in the bot
def setup(bot):
    bot.add_cog(twitter(bot))
