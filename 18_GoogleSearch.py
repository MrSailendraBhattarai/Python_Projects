# pip install google
from googlesearch import search

ask=input('Ask Anything : ')

for url in search(ask):
    print(url)