import discord, requests, sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

client = discord.Client()
token = '토큰'

@client.event
async def on_connect():
    print("ONLINE")

@client.event
async def on_message(message):
    if message.content.startswith("!웹훅삭제"):
        try:
            webhook = message.content.split(" ")[1]
        except:
            await message.channel.send("웹훅이 지정되지 않았습니다")

        if not "api/webhooks" in webhook or not "https://" in webhook:
            await message.channel.send("잘못된 웹훅입니다")
            return

        try:
            r = requests.get(webhook, verify=False)
        except:
            await message.channel.send("잘못된 웹훅입니다")
            return

        if not r.status_code == 200:
            await message.channel.send("잘못된 웹훅입니다")
            return
        elif r.status_code == 200:
            requests.delete(webhook)

        r = requests.get(webhook, verify=False)
        if r.status_code == 404:
            await message.channel.send(f"{message.author.mention} 웹훅 삭제를 성공하였습니다")
        else:
            await message.channel.send(f"{message.author.mention} 웹훅 삭제를 실패하였습니다")

client.run(token)
