import discord
import asyncio

token = "" #discord token

client = discord.Client()

message = "" #define different messages
message2 = ""


async def sendmsg():
    channel1 = discord.utils.get(client.get_all_channels(), name="")  #you can use channel ids instead but channel ids will often change for various reasons
    channel2 = discord.utils.get(client.get_all_channels(), name="")  #if you have 2 channels with the same name you have to use ids to differentiate them

    await channel1.send(message)
    await asyncio.sleep(1) #adjust delay / add channels here
    await channel2.send(message2)


@client.event
async def on_connect():
    print(f"Connected: {client.user.name}")
    while True:
        await sendmsg()
        await asyncio.sleep(1)


client.run(token, bot=False)
