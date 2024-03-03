
global alldata
alldata = {
   
}
class Safegitdata:
   def formatingdata(text):
    
    for item in text["items"]:
        listgit=f"'Name': {item['name']},
        'Owner': {item['owner']['login']}, 
        'Stars': {item['stargazers_count']}, 
        'Language': {item['language']}, 
        'Description': {item['description']}, 
        'Link': {item['html_url']}"
    
    alldata[item['name']]=listgit


