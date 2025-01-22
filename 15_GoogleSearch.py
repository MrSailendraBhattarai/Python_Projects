
from googlesearch import search

print("Welcome To Google Search")

user_input=input("Enter Thing to Search on Google : ")

for i in search(query=user_input,start=0,stop=6):
    print(i)