import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Load the Cogs (twitter and youtube commands)
bot.load_extension('commands')

#bot.load_extension('commands.twitter_download')


load_dotenv()
TOKEN = os.getenv("TOKEN")  # Get token from .env file
bot.run(TOKEN)


