import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Developer :: RGBSEVEN#8410")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!status"):
        await message.channel.send("`Bot is currently Online`")
    if message.content.startswith("!developer"):
        await message.channel.send("`RGBSEVEN#8410`")

    if message.content.startswith("/warn"):
        channel = message.content[6:24]
        msg = message.content[25:]
        await client.get_channel(int(channel)).send(msg)




access_token = os.environ("BOT_TOKEN")
client.run("BOT_TOKEN")
