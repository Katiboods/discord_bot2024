import os
import discord
from discord.ext import commands, tasks

from myserver import server_on

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())



@client.event
async def on_ready():
    print("bot is ready.")

@client.event
async def on_message(message):
    print(message)

@client.event
async def on_member_join(member):
    channel = client.get_channel(1290360345633886238)
    text = f"ยินดีต้อนรับนักผจญภัยทุกท่าน เข้าสู่เสิร์ฟเวอร์ของเรา!, {member.mention}!"

    emmbed = discord.Embed(title = 'ยินดีต้อนรับนักผจญภัยทุกท่าน!', description=text, color=0x435cb2,)


    await channel.send(text)
    await channel.send(embed = emmbed)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1290368848763162636)
    text = f"{member.name} ขอให้โชคดีกับการเดินทาง ลาก่อน!"
    await channel.send(text)

@client.event
async def on_message(message):
    mes = message.content
    if mes == 'สวัสดี':
        await message.channel.send("ไงพวก!")

server_on


client.run(os.getenv('TOKEN'))