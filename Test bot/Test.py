import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = "*")

@client.event
async def on_ready():
    print("Online!")

@client.command()
async def role(ctx, *, role: discord.Role):
    roles = discord.utils.get(ctx.guild.roles, name = f'{role}')
    author = ctx.message.author 
    await author.add_roles(roles)
    await author.send(f'{role} has been added.')

@client.command()
async def createarena(ctx, arenaID, Pass: int):
    author = ctx.message.author
    guild = ctx.message.guild
    if Pass >  100000000:
        msg = await ctx.channel.send("Arena password is invalid")
        await asyncio.sleep(10)
        await msg.delete()
    else:
         channel = await guild.create_text_channel(f'{author}s arena')
         await channel.send(f'__**{author} arena**__\nID = {arenaID} \nPassword = {Pass}')
    
    







@client.command()
async def unrole(ctx, *, role: discord.Role):
    roles = discord.utils.get(ctx.guild.roles, name = f'{role}')
    author = ctx.message.author
    await author.remove_roles(roles)
    await author.send(f'{role} has been successfully removed')
client.run("Insert token here")
    
