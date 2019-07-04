import discord
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if "wednesday" in message.content.lower():
            if message.created_at.weekday() == 2:
                await message.channel.send(file=discord.File("frog.jpg"))
            else:
                await message.channel.send("Today is not Wednesday")


client = MyClient()
client.run(os.environ.get("BOT_PASSWORD"))
