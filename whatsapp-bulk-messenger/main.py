import pandas as pd
import webbrowser
from pynput.keyboard import Key, Controller
import time




df = pd.read_excel('whatsapp_urls.xlsx') # Get all the urls from the excel
mylist = df['urls'].tolist() #urls is the column name

# print(mylist) # will print all the urls

# now loop through each url & perform actions.
for url in mylist:
   webbrowser.open(url)
   time.sleep(5)
   webbrowser.open(url)
   keyboard = Controller()
   time.sleep(5)
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
