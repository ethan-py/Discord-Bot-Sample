import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

#ALL REQUIRED MODULES ^^


#INITIALIZE AND SET THAT THE BOT'S COMMAND PREFIX IS .
bot = commands.Bot(command_prefix='.')

#DEFINE THAT BOT IS STARTING, UNDER THIS PUT WHATEVER YOUR BOT SHOULD DO UPON STARTUP
@bot.event
async def on_ready():
    print("Bot is starting!")
    
    
#CREATE A COMMAND, "commandnamehere" is the name of the command you want to be called. after ctx are variables that anyone says, so if someone types .commandnamehere HI, HI will be variable1
@bot.command(pass_context=True)
async def commandnamehere(ctx, variable1):
  await bot.say("hi") #bot says hi
  await bot.say(variable1) #bot says whatever the person put after .commandnamehere
  
  #creates a demo embed and sends it out
  em_main = discord.Embed(colour=6547380)
  em_main.set_author(name='Embed')
  em_main.set_footer(text='made by with love <3 | @cookgroups',icon_url='https://pbs.twimg.com/profile_images/956753895417499648/XeA2zLgk_400x400.jpg')
  em_main.add_field(name='Hey', value="hola",inline=False)
  em_main.set_thumbnail(url='https://pbs.twimg.com/profile_images/956753895417499648/XeA2zLgk_400x400.jpg')
  await bot.say(embed=em_main)
  

#CREATE A BOT THROUGH DISCORD DEV TOOLS AND GET TOKEN. RUN BOT WITH TOKEN

bot.run("TOKENHERE")
