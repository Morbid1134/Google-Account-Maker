import pyautogui as py
import webbrowser as wb
import time as t
import random
import os
import pyperclip

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s --incognito'


#end Chrome.exe
os.system("TASKKILL /F /IM chrome.exe")

#get First Name
choicefile=open("input\First.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
FirstName=random.choice(linelist)

#get Last Name
choicefile=open("input\Last.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
LastName=random.choice(linelist)

#get Password
choicefile=open("input\passwords.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
Password=random.choice(linelist)

#get Year 
Year = random.randint(1995,2004)

#get Month
choicefile=open("input\month.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
Month=random.choice(linelist)

#get Day
Day = random.randint(1,28)




#execute all to make email
wb.open('https://temp-mail.org/en/')
t.sleep(2)
py.hotkey("win", "up")
t.sleep(4)
py.click(x=1100, y=525)
t.sleep(7)
py.click(x=1040, y=280)
t.sleep(2)
py.hotkey("win", "right")
t.sleep(2)

Email = (pyperclip.paste())


py.hotkey("ctrl", "shift", "n")
t.sleep(2)
py.typewrite('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')
py.press('Enter')
t.sleep(8)
py.hotkey("win", "left")
py.click(x=300, y=440)
t.sleep(3)
py.typewrite(FirstName)
py.typewrite(LastName)
py.typewrite(Email)
py.press("tab")
py.press("tab")
t.sleep(3)
py.typewrite(Password)
py.typewrite(Password)
py.press("Enter")
py.click(x=1040, y=280)
py.hotkey("win", "up")
t.sleep(8)
py.click(x=860, y=810)
t.sleep(5)
py.scroll(-800)  
t.sleep(4)
py.doubleClick(x=850, y=550)
py.hotkey("ctrl", "c")
py.hotkey("win", "right")
py.click(x=1040, y=280)
py.click(x=350, y=550)
t.sleep(4)
py.click(x=350, y=550)
py.hotkey("ctrl", "v")
py.press('Enter')

# Runs ino Phone Issues
# must hve different phone number everytime
# or Phone number used in too many google accounts
# phone number may be suspended in google account creation



#Log All Bot Info
with open("BotInfo.txt", "a") as f:
  f.write("%s --- %s" %(Email, Password))
  f.close
  
