
global alldata
alldata = []
class Safegitdata:
   def formatingdata(text):
    
    for item in text["items"]:
        listgit=[
        f"Name: {item['name']}",
        f"Owner: {item['owner']['login']}",
        f"Stars: {item['stargazers_count']}",
        f"Language: {item['language']}",
        f"Description: {item['description']}",
        f"Link: {item['html_url']}"
     ]
        alldata.append(listgit)
        
    return alldata

