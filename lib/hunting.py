import random
import asyncio
from lib.config import wildchannelid, cheap_legies, cheap_legie_ball
from lib.variables import Encounters, Catches, GoodPoke
from lib.logger import log

async def hunt(rarity, name, description, client):
        global GoodPoke, Encounters
        await log(Encounters, Catches)
        await asyncio.sleep(0.3)
        GoodPoke=0
        Encounters += 1
        channel = client.get_channel(wildchannelid)
        
        await channel.trigger_typing()
        
        if (rarity('Common') != -1):
                await channel.send("gb")
         
        elif (rarity('Uncommon') != -1):
                await channel.send("gb")
         
        elif (rarity('Super Rare') != -1):
            
            if (name('Alolan-Geodude') != -1):
                await channel.send("mb")
                GoodPoke += 1
            else:
                await channel.send("ub")
         
        elif (rarity('Rare') != -1):
                await channel.send("gb")

        elif (rarity('Shiny (Full-odds') != -1):
          await channel.send("prb")
          GoodPoke += 1
            
        elif (rarity('Shiny') != -1):
          await channel.send("mb")
          GoodPoke += 1
         
        elif (rarity('Legendary') != -1):
            await channel.trigger_typing()
            
            if any(word in description for word in cheap_legies):
                await channel.send(cheap_legie_ball)

            else:
                await channel.send("mb")
                GoodPoke += 1

async def hunt_edit(status, client):
  global Catches
  if (status('You caught a') != -1):

            channel = client.get_channel(wildchannelid)
            Catches += 1
            await log(Encounters, Catches)
        
            if GoodPoke == 1:
             await channel.trigger_typing()
             await asyncio.sleep(0.125)
             happy = ["gg", "nice", "that's nice", "ooh yeah", "pog", "poggers"]
             await channel.send(random.choice(happy))

            await asyncio.sleep(8.5)
            await channel.trigger_typing()
            await channel.send(";p")
  
  elif (status('broke') != -1):
            await log(Encounters, Catches)
            channel = client.get_channel(wildchannelid)
            await asyncio.sleep(8.5)
            await channel.trigger_typing()
            await channel.send(";p")
