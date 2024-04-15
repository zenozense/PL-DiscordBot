from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import re

# LOAD TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# BOT SETUP, Able to Read-Message-Intents
intents = Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

# HANDLING THE STARTUP FOR BOT
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

# HANDLE INCOMING MESSAGES
allowed = ["youtube.com", "facebook.com", "instagram.com", "email.com", "github.com"]
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
      
    user_message: str = message.content

    # Using regular expression to find links in the message Include: https://, http://, www., non-www.
    links = re.findall(r'(https?://\S+)', user_message)

    # If any links are found
    if links:
        url_parts = user_message.split("//")[-1].split("/")
        if len(url_parts) >= 2:
            domain = url_parts[0]
            if domain.startswith("www."):
                domain = domain.split("www.")[-1]
            if domain not in allowed:
                print("Detected! Deleting message...")
                await message.channel.send(f'"{user_message}" was deleted from the server!')
                await message.delete()
                return
    else:
        return
      
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()