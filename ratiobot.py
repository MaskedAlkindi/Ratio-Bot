import discord
from discord.ext import commands
from decouple import config


TOKEN = config('TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
intents.guilds = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='Ratio')
async def ratio(ctx):
    if not ctx.message.reference:
        await ctx.send("Please reply to a message with `/Ratio` to ratio it.")
        return

    target_message = await ctx.fetch_message(ctx.message.reference.message_id)

    if target_message.author.bot:
        await ctx.send("Can't ratio a bot's message!")
        return

    emojis = [
    '👍', '👎', '❤️', '😂', '😭', '🔥', '🤔', '🎉', '😍', '🙏', 
    '🌟', '🍕', '🎈', '🌈', '📚', '🎶', '🌺', '🍎', '🚀', '🌙', 
    ]
    for emoji in emojis:
        await target_message.add_reaction(emoji)

bot.run(TOKEN)