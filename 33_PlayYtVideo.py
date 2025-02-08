
# pip install pywhatkit
# Play Youtube video
import pywhatkit

try:
    song=input('Enter Song Name : ')
    pywhatkit.playonyt(song) # redirect to youtube and play song
    print("Successfully Played : ")

except:
    print('Unexpected Error ')