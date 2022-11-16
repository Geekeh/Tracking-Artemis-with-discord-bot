import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    # https://www.youtube.com/watch?v=jh1CtQW4DTo&t=170s
    print("Bot online")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name = 'artemis', description='tracking info on artemis')
async def artemis(interaction: discord.Interaction):

    #get artemis info
    artemis_info = requests.get("https://s3.us-east-1.amazonaws.com/nasa-jsc-public/Orion/mission/Orion_flight104_mission.txt").json()

    #embed to send to discord
    em = discord.Embed(title='Artemis Info', color=0x0055ff)
    em.add_field(name='Velocity', value=artemis_info['Parameter_1']['Value'])
    em.add_field(name = 'Distance from earth', value=artemis_info['Parameter_3']['Value'])
    em.add_field(name = 'Distance to moon', value=artemis_info['Parameter_2']['Value'])

    batterie_info = str(artemis_info['Parameter_32']['Value']).split(":")
    em.add_field(name='Batteries', value=batterie_info[1])

    await interaction.response.send_message(embed=em)


bot.run("bot_token_here")
