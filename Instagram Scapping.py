import myScrapper as scr
import os
from pynput.keyboard import Key
from time import sleep

PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
DOWNLOADPATH = r"C:\Users\HP\Downloads"
def openSession(path):
    os.startfile(path) #for now, it's just this

def research(link):
    scr.shortCut(Key.ctrl, "e", wait2 = 0.1)
    scr.copyText(link)
    scr.pressRelease(Key.backspace)
    scr.shortCut(Key.ctrl, "v", wait2 = 0.1)
    scr.pressRelease(Key.enter)

def downloadProfilePic(username):
    openSession(PATH)
    sleep(1)
    #research("www.instagram.com/{}".format(username))
    research("https://www.instagram.com/{}/".format(username))
    sleep(4)
    location = os.path.join(DOWNLOADPATH,scr.savePage("Instagram {} source code.txt".format(username)))
    print(location)
    sleep(3)
    with open(location,"r", encoding = "UTF-8") as src:
        code = src.read()
        searchedFor = "profile_pic_url_hd"
        startIndex = code.index(searchedFor) + len(searchedFor) + 3 #the 3 is for ":"
        profilePicUrl = code[startIndex:code.index('"', startIndex)].replace("\\u0026", "&")
        print("pic url: " + profilePicUrl)
        research(profilePicUrl)
        sleep(2)
        if "." in username: username = username.replace(".", "-")
        scr.savePage("{} profile pic.png".format(username))
        print("Pic donwloaded!")
        
    
downloadProfilePic("lyonnir")
