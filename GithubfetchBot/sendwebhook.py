from discord import Webhook
import os
from dotenv import load_dotenv
import aiohttp
import time 
from typing import Final

load_dotenv()
WEBHOOK_URL:Final[str]=os.getenv('WEBHOOK_URL')


from discord import Webhook
import aiohttp

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(messages, username='Foo')
        time.sleep(3)
        
        return await foo()


async def main():
    await foo()


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())