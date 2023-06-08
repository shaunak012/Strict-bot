import discord
import responces
import Token
async def send_message(message,user_message):
    try:
        responce=responces.handleresponces(user_message)
        if responce:
            await message.author.send("its NOT shaunak, its shaunak bhaia")
        else:
            return
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username=message.author
        user_message=message.content
        channel=message.channel

        await send_message(message,user_message)

    TOKEN = Token.TOKEN
    client.run(TOKEN)