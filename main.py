import discord                                             # Discord.py documentation : https://discordpy.readthedocs.io/
import openai                                              # OpenAI chat API documentation : https://platform.openai.com/docs/guides/chat

openai.api_key = 'OpenAI-API-KEY'                          # Insert your OpenAI API key here

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

messages = [{"role": "system", "content": "You are a intelligent assistant."}]


@client.event
async def on_ready():                                       # Prints a confirmation to the console
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:                       # Rules out its own messages as commands
        return

    if message.content.startswith('Hello there'):            # Hello There
        await message.channel.send('https://tenor.com/bWVjr.gif')

    if message.content.startswith('HEUSC'):                 # Basic prompt for the bot's persona
        msg = message.content.replace('HEUSC', 'You are H.E.U.S.C, an AI butler to the millionaire detective Night, your task is to help him in all his need and provide support where he wants.')
        if msg:
            messages.append({"role": "user", "content": msg}, )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

        reply = chat.choices[0].message.content
        await message.channel.send(reply)
        messages.append({"role": "assistant", "content": reply})



client.run('Discord-API-KEY')                               # Insert your Discord API key here

