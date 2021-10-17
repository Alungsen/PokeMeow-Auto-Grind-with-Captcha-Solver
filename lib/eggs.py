import asyncio
import time 
from time import sleep
from lib.variables import EggsNum
from lib.config import egg_channel
from lib.config import auto_eggs
from lib.logger import log_eggs
async def eggs(message, client):
    if auto_eggs == True:
        import discord
        hatch = client.get_channel(egg_channel)
        await hatch.send(";egg hatch")
        global EggsNum
        EggsNum += 1
        await log_eggs(EggsNum)
        
        sleep(8)
        await hatch.send(";egg hold")
    else:
        return    