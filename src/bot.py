import discord
import responses

# save the previous code
lastCode = ""


async def send_response(message, user_message):
    try:
        response = responses.handle_response(user_message)
        if response != '':
            await message.channel.send(response)
            if len(response) == 6:
                global lastCode
                lastCode = response
    except Exception as e:
        print(e)


async def update_bot_status(client):
    if lastCode != "":
        await client.change_presence(activity=discord.Game(name=lastCode.upper()))
    else:
        await client.change_presence(activity=None)


def run_bot():
    token_path = "token.txt"
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

        if "join.btd6.com/coop/" or "join.btd6.com/boss/" in user_message.lower():
            await message.edit(suppress=True)
            await send_response(message, user_message)
            print(f"{username} said: '{user_message}' ({channel})")
            await update_bot_status(client)
        elif "!code" == user_message.lower():
            await send_response(message, user_message)
            print(f"{username} said: '{user_message}' ({channel})")

    client.run(token)


run_bot()
