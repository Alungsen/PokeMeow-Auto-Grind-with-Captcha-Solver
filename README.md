# PokeMeow Auto-Grind with Captcha Solver 🤖
This is an Auto-Grind Bot made for Pokemeow. This is an efficient and a feature-rich bot with a Captcha Solver built-in. This bot has many suspicion avoidance features which prevent you from getting caught. These suspicion avoidance features enable you to grind in clan channels too!

## Supported features
This bot can currently handle :
1. Captcha Solving (with the help of AzCaptcha)
- 60% Captcha solving accuracy.
- Automatically coninues grinding after doing the captcha.
- It will stop if it sends an Incorrect Response.
2. Fishing which can be enabled/disabled through `config.py`.
3. Throw Pokeballs depending on the rarity of the Pokemon.
- Throws prb on Full-Odds Shiny.
- Throws prb/ub (depending on the config) on Cheap Legendaries! (you can change the list of cheap legendaries in the config)

## Suspicion Avoidance Features
- Typing Triggers on each and every message.
- Automatic stop if anyone who isn't whitelisted messages in the channel. (Shadow Lugia and Meow helper already whitelisted)
- 0.2 to 0.3 seconds delay before sending any messages.
- Send messages like gg, nice, etc after catching a shiny or an expensive legendary. 


## Installating

### On your pc
1. Install your favorite version of python 3 and add it to PATH.
2. If not done already download this repo on your computer as zip and unzip it.
3. Inside of the repo type the following command `python -m pip install -r requirements.txt` (If your on a linux distribution or MacOS you got a specify the python version so it's `python3 ...`)
4. Make an account on AzCaptcha by going to https://azcaptcha.com/account/signup.
5. Copy and paste you AzCaptcha account token in `config.py`.
6. In `config.py` edit more variables like `username, token, wildchannelid, channelid_fish, cheap_legie_ball` according to your convenience.

### On your discord
7. Make sure that your Pokemeow name and Discord name are same.

## Launching 
1. Run `main.py`.
2. Make sure to buy balls before launching.
3. Start hunting by doing ;p in the channel you wish to hunt. (must be the same one put in the config)
4. Start fishing by doing ;f in the channel you wish to fish. (must be the same one put in the config in channelid_fish and fishing must be set to True in config)

## Stoping
To stop the program simply close the command prompt.

## Disclamer ⚠️
- We're of course not responsible for any ban you recieve for using this bot.
- The captcha solver accuracy is only around 60% so please keep an eye on the bot.
- DO NOT run fishing and hunting in the same servers.
- Can run multiple accounts in the same channel (hunting and fishing in different servers) but all accounts must be whitelisted.
- You can only solve around 50 captchas (around 2 hours of grinding) until your AzCaptcha balance runs out! After that create a new AzCaptcha account and update the AzCaptcha Token in the config.