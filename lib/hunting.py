import random
import asyncio
from lib.config import wildchannelid, cheap_legies, hunt_cooldown
from lib.config import auto_buy_balls, common, uncommon, rare, super_rare, alolan, cheap_legie, legie, Shiny, Shiny_Fullodds
from lib.variables import Encounters, Catches, GoodPoke, EggsNum
if auto_buy_balls == True:
 from lib.balls import pokeball, greatball, ultraball, masterball
from lib.logger import log

async def hunt(rarity, name, description, client, footer):
        global GoodPoke, Encounters
        channel = client.get_channel(wildchannelid)
        await channel.trigger_typing()
        await asyncio.sleep(0.2)
        GoodPoke=0
        Encounters += 1
        
        if (rarity('Common') != -1):
                await channel.send(common)
                ball_sent = common
         
        elif (rarity('Uncommon') != -1):
                await channel.send(uncommon)
                ball_sent = uncommon
         
        elif (rarity('Super Rare') != -1):
            
            if (name('Alolan') != -1):
                await channel.send(alolan)
                GoodPoke += 1
                ball_sent = alolan
            else:
                await channel.send(super_rare)
                ball_sent = super_rare
         
        elif (rarity('Rare') != -1):
                await channel.send(rare)
                ball_sent = rare

        elif (rarity('Shiny (Full-odds') != -1):
          await channel.send(Shiny_Fullodds)
          GoodPoke += 1
          ball_sent = Shiny_Fullodds
            
        elif (rarity('Shiny') != -1):
          await channel.send(Shiny)
          GoodPoke += 1
          ball_sent = Shiny
         
        elif (rarity('Legendary') != -1):
            await channel.trigger_typing()
            
            if any(word in description for word in cheap_legies):
                await channel.send(cheap_legie)
                ball_sent = cheap_legie
            else:
                await channel.send(legie)
                GoodPoke += 1
                ball_sent = legie

        if auto_buy_balls == True:
         if ball_sent == "pb":
          await pokeball(footer, channel)

         elif ball_sent == "gb":
          await greatball(footer, channel)

         elif ball_sent == "ub":
          await ultraball(footer, channel)

         elif ball_sent == "mb":
          await masterball(footer, channel)

async def hunt_edit(status, client):
  global Catches
  if (status('You caught a') != -1):

            channel = client.get_channel(wildchannelid)
            Catches += 1
            await log(Encounters, Catches, EggsNum)
        
            if GoodPoke == 1:
             await channel.trigger_typing()
             await asyncio.sleep(0.2)
             happy = ["gg", "nice", "that's nice", "ooh yeah", "pog", "poggers"]
             await channel.send(random.choice(happy))

            await asyncio.sleep(hunt_cooldown)
            await channel.trigger_typing()
            await channel.send(";p")
  
  elif (status('broke') != -1):
            await log(Encounters, Catches, EggsNum)
            channel = client.get_channel(wildchannelid)
            await asyncio.sleep(hunt_cooldown)
            await channel.trigger_typing()
            await channel.send(";p")