import pandas as pd
import webbrowser
from pynput.keyboard import Key, Controller
import time
import os



df = pd.read_excel('whatsapp_urls.xlsx') # Get all the urls from the excel
mylist = df['urls'].tolist() #urls is the column name

# print(mylist) # will print all the urls

# now loop through each url & perform actions.
for idx, url in enumerate(mylist):
   webbrowser.open(url)
   keyboard = Controller()
   time.sleep(5)
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
   os.system("taskkill /im firefox.exe /f")