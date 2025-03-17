from discord.ext import commands
import aiohttp
import os


class addToDir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="addToDir", description="Retrieve an attachment from your message")
    async def addToDir(ctx):

        if ctx.message.attachments:

            await ctx.respond("Retrieving files...")
            for attachment in ctx.message.attachments:
                file_path = os.path.join("src/memes", attachment.filename)
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachment.url) as response:
                        if response.status == 200:
                            with open(file_path, 'wb') as f:
                                f.write(await response.read())
                            await ctx.send(f'{attachment.filename} downloaded successfully.')
                        else:
                            await ctx.send(f'Failed to download {attachment.filename}.')
        else:
            await ctx.respond("No attachments found in the message.")


def setup(bot):
    bot.add_cog(addToDir(bot))
