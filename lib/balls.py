import asyncio
from lib.config import pokeballs, greatballs, ultraballs, masterballs
from lib.config import pokeballs_left, greatballs_left, ultraballs_left, masterballs_left

def remove(string):
    return string.replace(",", "")

async def pokeball(footer, channel):
  x = footer.split("═════ Balls left ═════")
  y = x[1]
  z = y.split("\\n")
  abc = z[1]
  abcd = abc.split("|")
  h = abcd[0]
  afin = h.split(":")
  fin = afin[1]
  if (fin.find(',') != -1):
   gfin = int(remove(fin))
  else:
   gfin = int(fin)
  if gfin <= pokeballs_left: 
    await channel.trigger_typing()
    await asyncio.sleep(1)
    await channel.send(';s b 1 ' + str(pokeballs))

async def ultraball(footer, channel):
  x = footer.split("═════ Balls left ═════")
  y = x[1]
  z = y.split("\\n")
  abc = z[1]
  abcd = abc.split("|")
  h = abcd[1]
  afin = h.split(":")
  fin = afin[1]
  if (fin.find(',') != -1):
   gfin = int(remove(fin))
  else:
   gfin = int(fin)
  if gfin <= ultraballs_left: 
   await channel.trigger_typing()
   await asyncio.sleep(1)
   await channel.send(';s b 3 ' + str(ultraballs))

async def greatball(footer, channel):
  x = footer.split("═════ Balls left ═════")
  y = x[1]
  z = y.split("\\n")
  abc = z[2]
  abcd = abc.split("|")
  h = abcd[0]
  afin = h.split(":")
  fin = afin[1]
  if (fin.find(',') != -1):
   gfin = int(remove(fin))
  else:
   gfin = int(fin)
  if gfin <= greatballs_left: 
   await channel.trigger_typing()
   await asyncio.sleep(1)
   await channel.send(';s b 2 ' + str(greatballs))

async def masterball(footer, channel):
  x = footer.split("═════ Balls left ═════")
  y = x[1]
  z = y.split("\\n")
  abc = z[2]
  abcd = abc.split("|")
  h = abcd[1]
  afin = h.split(":")
  fin = afin[1]
  if (fin.find(',') != -1):
   gfin = int(remove(fin))
  else:
   gfin = int(fin)
  if gfin <= masterballs_left: 
   await channel.trigger_typing()
   await asyncio.sleep(1)
   await channel.send(';s b 4 ' + str(masterballs))
