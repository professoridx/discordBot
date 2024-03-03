from discord import Webhook,Embed
import os
from dotenv import load_dotenv
import aiohttp
import time 
from typing import Final
from gitfunction import GetGitHub
import requests

python="https://download.logo.wine/logo/Python_(programming_language)/Python_(programming_language)-Logo.wine.png"
java="https://cdn-icons-png.flaticon.com/512/1183/1183618.png"
javascript="https://cdn-icons-png.flaticon.com/512/919/919828.png"
c="https://cdn-icons-png.flaticon.com/128/14865/14865856.png"
r="https://cdn-icons-png.flaticon.com/128/13527/13527880.png"
scala="https://cdn-icons-png.flaticon.com/128/6132/6132220.png"
c_plus="https://cdn-icons-png.flaticon.com/128/6132/6132222.png"
juputernotebook="https://cdn-icons-png.flaticon.com/128/14422/14422032.png"
html="https://cdn-icons-png.flaticon.com/128/919/919827.png"
css="https://cdn-icons-png.flaticon.com/128/919/919826.png"
php="https://cdn-icons-png.flaticon.com/128/919/919830.png"
sass="https://cdn-icons-png.flaticon.com/128/919/919831.png"
typescript="https://cdn-icons-png.flaticon.com/128/919/919832.png"
swift="https://cdn-icons-png.flaticon.com/128/919/919833.png"
kotlin="https://cdn-icons-png.flaticon.com/128/1892/1892569.png"
sql="https://cdn-icons-png.flaticon.com/128/2306/2306173.png"
mongodb="https://www.opc-router.de/wp-content/uploads/2021/03/mongodb_thumbnail.png"
postgresql="https://w7.pngwing.com/pngs/441/460/png-transparent-postgresql-plain-wordmark-logo-icon-thumbnail.png"
mariadb="https://cdn-icons-png.flaticon.com/128/5968/5968313.png"


load_dotenv()
WEBHOOK_URL:Final[str]=os.getenv('WEBHOOK_URL')


async def foo():
    
    all_massage=GetGitHub.get_repo("python")
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