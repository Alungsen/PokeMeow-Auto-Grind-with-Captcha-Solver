from lib.config import wildchannelid, api

async def captcha(message, client):
 channel = client.get_channel(wildchannelid)
 await message.attachments[0].save(fp=message.attachments[0].filename)
 await channel.trigger_typing()

 with open(message.attachments[0].filename, 'rb') as captcha_file:
   captcha = api.solve(captcha_file)
   await channel.send(str(captcha.await_result()))