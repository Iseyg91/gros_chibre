import os
import time
import discord
from discord.ext import commands
from keep_alive import keep_alive

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
keep_alive()  # Lance le petit serveur Flask pour maintenir le service en ligne
bot.run(token)
