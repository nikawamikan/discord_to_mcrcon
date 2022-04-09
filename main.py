import discord
from discord import Option
from discord.ext import commands
from dotenv import load_dotenv
from mcrcon import MCRcon
import os

load_dotenv()


TOKEN = os.getenv('TOKEN')
GUILD_IDS = [int(os.getenv('GUILDID'))]

bot = discord.Bot(description='これはテスト用ニートです')

HOST = os.getenv('HOST')
PASSWD = os.getenv('PASSWD')
PORT = int(os.getenv('PORT'))


async def send_rcon(com, debug):
    with MCRcon(HOST, PASSWD, PORT) as mcr:
        res = mcr.command(com)
        if debug:
            print(f'respons: {res}')
            print(f'command: {com}')
        return res


@bot.slash_command(name='say', description='sayをしたい')
@commands.cooldown(rate=5, per=3)
@commands.has_role(879627587498938368)
async def say(ctx, string: Option(str, description='なんて送りますかね', default='おささってるｗｗおささってるｗｗｗｗ')):
    com = f'say {string}'
    res = await send_rcon(com, debug=True)
    await ctx.respond(f'respons: {res}\nsend command: {com}')


@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown) or isinstance(error, commands.MissingRole):
        await ctx.respond(error, ephemeral=True)
    else:
        await ctx.respond(error, ephemeral=True)

bot.run(TOKEN)
