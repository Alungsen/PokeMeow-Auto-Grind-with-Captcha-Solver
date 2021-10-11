import discord
import asyncio
from lib.captcha import captcha
from lib.config import username, channelid_fish, wildchannelid, channelids, token, fishing, captcha_solver
from lib.variables import Catches, Fish_Catches, GoodPoke
from lib.hunting import hunt, hunt_edit
if fishing == True:
 from lib.fishing import fish, fish_edit
from lib.logger import log_start

class MyClient(discord.Client):
    async def on_ready(self):
     await log_start()

    async def on_message(self, message):

     if (message.channel.id == wildchannelid):
         if message.author != self.user:
            if message.author.id != 664508672713424926: #Whitelist Pokemeow
                if message.author.id != 833428629705719828: #Whitelist Shadow Lugia
                    if message.author.id != 795050413279019028: #Whitelist Meow Helper
                        quit()

         if captcha_solver == True:
          if "incorrect response!" in message.content:
             return
            
          elif "captcha" in message.content:
             await captcha(message, client)

         if "continue hunting!" in message.content:
              channel = client.get_channel(wildchannelid)
              await channel.trigger_typing()
              await asyncio.sleep(0.2)
              await channel.send(";p")

         embeds = message.embeds
         for embed in embeds:
          footer=str(embed.footer)
          rarity=(footer.find)
          description=str(embed.description)
          name=(description.find)
          
          if (name("**"+ username + "** found a wild") != -1):
           await hunt(rarity, name, description, client, footer)

    async def on_message_edit(self, before, after):
     if any(word in str(after.channel.id) for word in channelids):
      embeds = after.embeds
      for embed in embeds:

       description=str(embed.description)
       status=(description.find)
       global GoodPoke, Fish_Catches, Catches
       fishchannel = client.get_channel(channelid_fish)

       if fishing == True:
        await fish(status, fishchannel, GoodPoke)
       
        if (after.channel.id == channelid_fish):
         await fish_edit(status, client)

       if (after.channel.id == wildchannelid):
        await hunt_edit(status, client)

client=MyClient()
client.run(token)
