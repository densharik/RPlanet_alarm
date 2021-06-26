import pandas as pd
import json
from playsound import playsound
import time

html = pd.read_html('https://prospectors.online/alchemy/recipes.html')
html = html[0]
num = len(html)

def check():
    while True:
        html = pd.read_html('https://prospectors.online/alchemy/recipes.html')
        html = html[0]
        num1 = len(html)
        if(num1 == num):
            print(1)
            time.sleep(3)
        else: 
            print('INVENTED!!!!!!!!')
            playsound('sound.mp3')
            break
check()

#pyinstaller Inventor_allert1.py --onefile