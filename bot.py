import discord
import responses

# save the previous code
lastCode = ""


async def send_response(message, user_message):
    try:
        response = responses.handle_response(user_message)
        if response != '':
            await message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot():
    token = 'MTE0NDExMDA2NDQxNjg3MDQzMg.G9VW8N.Dhc4y4vKZnKzqL0r29k1FPQNAqLImllYcL8Ico'
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if "join.btd6.com/coop/" in user_message.lower():
            await message.edit(suppress=True)

        await send_response(message, user_message)

    client.run(token)


run_bot()
