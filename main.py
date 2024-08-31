import os
import discord
from discord.ext import commands
from discord import app_commands
from myserver import server_on 

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


TOKEN = 'MTI2NDk1NTI3NjMxNDkzOTQ5NA.GrRkK6.dc6_PdsDSSpH83UW6gFxsbjF4f7S2DTcN13tBE'


# คำสั่งBot พร้อมใช้งาน


@bot.event
async def on_ready():
    print("BOT Online!")

#แจ้งคนเข้าออก
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1272601097412018187)
    text = f"{member.name} ออกจากเชิฟเวอร์แล้ว!"

    emmbed = discord.embed (title = 'ออกจากเชิฟเวอร์แล้ว',description = 'โชคดีแล้วพบกันใหม่นั้มม')
    await channel.send(embed = emmbed)
    await channel.send(text)
    
server_on()

bot.run(TOKEN)
    