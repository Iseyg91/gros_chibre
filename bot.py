import os
import time
import discord
from discord.ext import commands

# --- Configuration du bot ---
intents = discord.Intents.all()
start_time = time.time()
bot = commands.Bot(command_prefix="!!", intents=intents, help_command=None)

# --- Événements ---
@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user} ({bot.user.id})")

# --- Lancement du bot ---
token = os.environ['ETHERYA']
bot.run(token)
