import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.typing = False  # You can adjust these as needed
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of words to exclude
excluded_words = ["her", "er", "deer", "beer"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # print(f'Received message: {message.content}')
    # Avoid responding to the bot's own messages to prevent loops
    if message.author == bot.user:
        return

    # Split the message into words
    words = message.content.split()

    response = ""
    for word in words:
        # Check if the word ends with "er" sound (including variations)
        if re.search(r'er$', word.lower()) and word.lower() not in excluded_words:
            response += f'{word}?! I hardly know her! '
            await message.channel.send(response)
            break
        

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE1ODg2OTMxNTg1Mjk2ODA2Nw.GtmddK.HF9gws5KH2v0PvoU4sWaKsAACTaK29vGVnPN-Y')