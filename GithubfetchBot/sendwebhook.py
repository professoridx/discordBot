from discord import Webhook,Embed
import os
from dotenv import load_dotenv
import aiohttp
import time 
from typing import Final
from gitfunction import GetGitHub
import requests

load_dotenv()
WEBHOOK_URL:Final[str]=os.getenv('WEBHOOK_URL')


all_massage=GetGitHub.get_repo("python")




async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(WEBHOOK_URL, session=session)
        
        for item in all_massage["items"]:
            name = item["name"]
            owner = item["owner"]["login"]
            stars = item["stargazers_count"]
            language = item["language"]
            description = item["description"]
            link = item["html_url"]
            issue = item["open_issues"]
            ssh = item["ssh_url"]
            giturl = item["git_url"]
            icon=item["owner"]["avatar_url"]
            
            
            
            
            description=f"Name: {name}\nStars: {stars}\nLanguage: {language}\nDescription: {description}\nLink: {link}\n Open Issues: {issue}\nSSH URL: {ssh}\nGit URL: {giturl}"
            try:
                    
                    embed = Embed(title="Trending Python Repositories", color=0x00ffff,description=description)
                    embed.set_thumbnail(url=link)
                    embed.set_author(name=owner, icon_url=icon)
            except:
                   await webhook.send("end of erra")
            
    
            await webhook.send(embed=embed)
            
            time.sleep(6)
        
        
        # return await foo()


async def main():
    await foo()


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())