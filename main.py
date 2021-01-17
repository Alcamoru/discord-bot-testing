import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

with open("TOKEN.txt", "r") as infile:
    TOKEN = infile.read()

bot.run(TOKEN)
