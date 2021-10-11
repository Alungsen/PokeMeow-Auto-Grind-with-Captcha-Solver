from azcaptchaapi import AZCaptchaApi

username=("Jeff") #Put your Discord username here without tag

channelid_fish=000000000000 #Fishing channel id here
wildchannelid=000000000000 #Wild Channel here

hunt_cooldown=8.4 #;p cooldown | for random cooldown put (random.randint(minimum, maximum))
# random cooldown example:  hunt_cooldown=(random.randint(9, 10))

fish_cooldown=21.7 #;f cooldown | for random cooldown do the same as for hunt_cooldown

channelids=[str(channelid_fish), str(wildchannelid)]

fishing=False #Set it to True to enable Fishing

captcha_solver=False #Set it to False to diable captcha solver and set it to True to enable it

#List of cheap legies on which you would like to do prb or ub
#You can add or remove names from this list
cheap_legies=["Articuno", "Mew", "Jirachi", "Moltres", "Raikou", "Entei", "Suicune", "Ho-oh", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Deoxys", "Uxie", "Mesprit", "Azelf", "Heatran", "Regigigas", "Cresselia", "Cobalion", "Terrakion", "Virizion", "Tornadus", "Thundurus", "Landorus", "Xerneas", "Yveltal", "Celebi", "Zygarde"]

auto_buy_balls=True #Set it to False to diable auto buy balls and set it to True to enable it

common="pb"
uncommon="pb"
rare="gb"
super_rare="ub"
alolan="mb" #Which ball to use on Alolan Event Exclusive Pokemons
cheap_legie="prb" #Which ball to use on cheap legies
legie="mb" #Which ball to use on expensive legies
Shiny="mb" 
Shiny_Fullodds="prb"

azcaptcha_token = [''] #azcaptcha api token

api = AZCaptchaApi(azcaptcha_token)

#Discord Token
token=''

#How many balls to buy:-
pokeballs=100
greatballs=50
ultraballs=20
masterballs=1

#When to buy:-
pokeballs_left=20
greatballs_left=10
ultraballs_left=5
masterballs_left=0
