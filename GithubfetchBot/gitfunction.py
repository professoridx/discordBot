import requests
import pprint
from dotenv import load_dotenv

import os 
load_dotenv()
token = os.getenv("GITHUB_TOKEN")


class GetGitHub:
   def get_repo(text):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/search/repositories?q=language:{text}&sort=stars"

    response = requests.get(url, headers=headers).json()
    
    return response


     
  # async def get_userall(text):
  #   headers = {"Authorization": f"token {token}"}
  #   url = f"https://api.github.com/users/{text}"

  #   response = requests.get(url, headers=headers).json()
    
  #   return response.json()
  
  

