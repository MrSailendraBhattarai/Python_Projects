
# Download File

import requests

url=input('Enter Url : ')

response=requests.get(url)
with open('download.zip','wb') as f:
    f.write(response.content)