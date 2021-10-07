from azcaptchaapi import AZCaptchaApi

username=("George") #Put your Discord username here without tag

channelid_fish=000000000 #Fishing channel id here
wildchannelid=000000000 #Wild Channel here

channelids=[str(channelid_fish), str(wildchannelid)]

fishing=False #Set it to True to enable Fishing

#List of cheap legies on which you would like to do prb or ub
#You can add or remove names from this list
cheap_legies=["Articuno", "Mew*", "Jirachi", "Moltres", 
              "Raikou", "Entei", "Suicune", "Ho-oh", 
              "Regirock", "Regice", "Registeel", 
              "Latias", "Latios", "Deoxys", "Uxie", 
              "Mesprit", "Azelf", "Heatran", "Regigigas", 
              "Cresselia", "Cobalion", "Terrakion", "Virizion", 
              "Tornadus", "Thundurus", "Landorus", "Xerneas", 
              "Yveltal", "Celebi", "Zygarde"]

cheap_legie_ball="prb" #Which ball to use on cheap legies

api = AZCaptchaApi('') #azcaptcha api key

#Discord Token
token=''
