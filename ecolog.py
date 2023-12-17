import discord
from discord.ext import commands
import random

TOKEN = ('MTE4NTg3ODI2NTE0NDAzMzM2MA.G_V8DK.51oS4XmXtreaz5R_Sw2ZKN_SZr8NACrjJaqbGM')

PREFIX = '!'

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='!')

waste_advice = [
    "Помните, что нужно разделять перерабатываемые материалы, такие как пластик, бумага и стекло.",
    "Утилизируйте опасные отходы, такие как батарейки и электронные устройства, в специальных пунктах сбора.",
    "Компостируйте органические отходы, такие как пищевые остатки и садовые отходы, вместо выбрасывания их."
]

@bot.event
async def on_ready():
    print('Вошел как {bot.user.name}')

@bot.command()
async def advice(ctx):
    random_advice = random.choice(waste_advice)
    await ctx.send(random_advice)

bot.run('TOKEN')