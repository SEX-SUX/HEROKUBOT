import importlib
import asyncio
import os
from HEROKUHELP import app
from pyrogram import idle

async def main():
    print("Starting Bot.....")
    await app.start()
    print("Bot Started.....")

    for file in os.listdir("HEROKUHELP/plugins"):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            importlib.import_module(f"HEROKUHELP.plugins.{module_name}")

    await idle()
    print("Bot Stopped.....")
    


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
