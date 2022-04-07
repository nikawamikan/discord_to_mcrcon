import threading
import discord
from dotenv import load_dotenv
from mcrcon import MCRcon
import os

load_dotenv()


class Rcon:
    def __init__(self, mcr, debug) -> None:
        self.mcr = mcr
        self.debug = debug

    async def send_command(self, com):
        res = self.mcr.command(com)

        if self.debug:
            print(res)
            print(com)
        return res


rcon = None


TOKEN = os.getenv('TOKEN')
GUILD_IDS = [int(os.getenv('GUILDID'))]

bot = discord.Bot(description='これはテスト用ニートです')


@bot.slash_command(name='say', description='sayをしたい')
async def say(ctx):
    com = 'say test'
    res = await rcon.send_command(com)
    await ctx.respond(f'response: {res}\nsend command: {com}')


HOST = os.getenv('HOST')
PASSWD = os.getenv('PASSWD')
PORT = int(os.getenv('PORT'))

with MCRcon(HOST, PASSWD, PORT) as mcr:
    rcon = Rcon(mcr, True)
    bot.run(TOKEN)
