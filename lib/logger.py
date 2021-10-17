import datetime
start_time=datetime.datetime.now().replace(microsecond=0)

fishes=0
Eggs = 0

async def log_start():
 print("Start date & time " + str(start_time))

async def log_fish(Fish_Catches):
    global fishes
    fishes += Fish_Catches

async def log_eggs(EggsNum):
    global Eggs
    Eggs += EggsNum

async def log(Encounters, Catches, EggsNum):
    global fishes
    current_time=datetime.datetime.now().replace(microsecond=0)
    time_elapsed=current_time - start_time
    print(("Time Elapsed : " + str(time_elapsed)) + " | Encounters : " + (str(Encounters)) + " | Catches : " + (str(Catches)) + " | Fish Catches : " + (str(fishes) + "| Eggs : " + (str(Eggs))))