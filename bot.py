import discord
from discord.ext import commands
from discord import app_commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# Run the bot with your token
def run(TOKEN):
    bot.run(TOKEN)
