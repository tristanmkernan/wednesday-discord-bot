import discord
import os


class MyClient(discord.Client):
    def __init__(self):
        super(MyClient, self).__init__()
        self.times_called = 0

    async def on_ready(self):
        print(f"Logged on as {self.user}")
        await client.change_presence(activity=discord.Game(name="SKYNET"))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if "wednesday" in message.content.lower():
            self.times_called += 1

            if message.created_at.weekday() == 2:
                await message.channel.send(file=discord.File("frog.jpg"))
            else:
                await message.channel.send("Today is not Wednesday")

        if any(mention == client.user for mention in message.mentions):

            await message.channel.send(
                f"I have been called {self.times_called} times, my dudes!"
            )


client = MyClient()
client.run(os.environ.get("BOT_PASSWORD"))
