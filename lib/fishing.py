import asyncio
from lib.config import channelid_fish, fish_cooldown
from lib.variables import Fish_Catches
from lib.logger import log_fish
from lib.eggs import eggs

async def fish(status, fishchannel, GoodPoke):
    await fishchannel.trigger_typing()
    if (status('PULL') != -1):
            await fishchannel.send("pull")
            
    elif (status('Not even') != -1):
            await asyncio.sleep(fish_cooldown)
            await fishchannel.send(";f")

    elif (status('fished out') != -1):
            await asyncio.sleep(0.2)
            if (status('Golden') != -1):
                await fishchannel.send("mb")
                GoodPoke += 1

            elif (status('Shiny') != -1):
                await fishchannel.send("mb")
                GoodPoke += 1

            elif (status('Kyogre') != -1):
                await fishchannel.send("prb")

            elif (status('Suicune') != -1):
                await fishchannel.send("prb")

            else:
                await fishchannel.send("ub")

async def fish_edit(status, client):
    global Fish_Catches
    if (status('You caught a') != -1):
            fishchannel = client.get_channel(channelid_fish)
            Fish_Catches += 1
            await log_fish(Fish_Catches)
            await asyncio.sleep(fish_cooldown)
            await fishchannel.trigger_typing()
            await fishchannel.send(";f")

    elif (status('broke') != -1):
            fishchannel = client.get_channel(channelid_fish)
            await asyncio.sleep(fish_cooldown)
            await fishchannel.trigger_typing()
            await fishchannel.send(";f")
