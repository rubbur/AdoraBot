import os
import discord
from src import responses

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
    token_path = os.path.join(os.path.dirname(__file__), "..", "Resources", "token.txt")
    with open(token_path, "r") as token_file:
        token = token_file.read().strip()

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
