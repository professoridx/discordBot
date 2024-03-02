import gitfunction 

class safegitdata:
  async def fromatingdata(text):
    for item in text["items"]:
        listgit=[
        f"Name: {item['name']}",
        f"Owner: {item['owner']['login']}",
        f"Stars: {item['stargazers_count']}",
        f"Language: {item['language']}",
        f"Description: {item['description']}",
        f"Link: {item['html_url']}"
     ]
        return listgit

