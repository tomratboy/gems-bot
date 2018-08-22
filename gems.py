import discord

TOKEN = 'NDgxODQ4NzA2NDgwNjAzMTM5.Dl8Uiw.ZvilHr8fCCMS2s422K56NSZnhHA'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "hope you had a good" in message.content.lower():
        msg = "Thanks".format(message)
        await message.channel.send(msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
