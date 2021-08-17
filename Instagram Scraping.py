import myScraper as scr
import os
from pynput.keyboard import Key, Controller
from time import sleep
from pyautogui import keyDown, keyUp #Could not get pynpyt hold key so I tried PyAutoGui but it does not work either

kb = Controller()
PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
DOWNLOADPATH = r"C:\Users\HP\Downloads"
def openSession(path, private = False, bigWindow = True):
    os.startfile(path) #for now, it's just this
    
    sleep(1)
    if bigWindow: 
        scr.shortCut([Key.cmd_l], Key.up)
        sleep(0.3)
    if private:
        scr.shortCut([Key.shift,Key.ctrl], "n")

def research(link):
    scr.shortCut([Key.ctrl], "e", wait2 = 0.1)
    scr.copyText(link)
    scr.pressRelease(Key.backspace)
    scr.shortCut([Key.ctrl], "v", wait2 = 0.1)
    scr.pressRelease(Key.enter)

def downloadProfilePic(username, private = True):
    openSession(PATH, private)
    sleep(1)
    #research("www.instagram.com/{}".format(username))
    research("https://www.instagram.com/{}/".format(username))
    sleep(4)
    scr.shortCut([Key.ctrl],"u")
    sleep(4)
    save = scr.savePage("Instagram {} source code.txt".format(username))
    location = os.path.join(DOWNLOADPATH,save)
    print(location)
    sleep(2)
    scr.shortCut([Key.ctrl],"w")
    with open(location,"r", encoding = "UTF-8") as src:
        code = src.read()
        searchedFor = "profile_pic_url_hd"
        count = code.count(searchedFor)
        if count == 1:
            startIndex = code.index(searchedFor) + len(searchedFor) + 3 #the 3 is for ":"
        elif count == 2:
            startIndex = code.index(searchedFor, code.index(searchedFor) + len(searchedFor)) + len(searchedFor) + 3
        else: 
            print("Can't detect the correct image")
            return
        profilePicUrl = code[startIndex:code.index('"', startIndex)].replace("\\u0026", "&")
        print("pic url: " + profilePicUrl)
        research(profilePicUrl)
        sleep(2)
        if "." in username: username = username.replace(".", "-")
        scr.savePage("{} profile pic.png".format(username))
        print("Pic donwloaded!")
        
def downloadAll(username, scrollTime = 2):
    count = 1
    imagesLinks = []
    framerate = 1/60
    global scroll 
    scroll = scrollTime
    openSession(PATH)
    research("https://instagram.com/{}".format(username))
    #research("https://www.onlinemictest.com/fr/keyboard-test/")
  
    sleep(5)
    print("Request done. Searching and parsing, please wait...")
    def scrollDown():
        global scroll
        while scroll > 0:
            scroll -= framerate
            keyDown("down")
        else: 
            scroll = scrollTime
            keyUp("down")
    padding = 0
    previous = -1
    #It would be easier with a do while loop but we're in Python
    a = scr.getCurrentSrc()
    while 1:
        index = a.find('srcset="')
        if index == -1: break
        index +=8
        end = a.find('"', index)
        link = a[index:end]
        if link not in imagesLinks:
            imagesLinks.append(link)
        a = a[end::]
    while padding != previous:
        previous = padding
        scrollDown()
        a = scr.getCurrentSrc()
        start = a.index("padding-top: "
                        )
        padding = int(a[start+13:a.index("px", start)])
        while 1:
            index = a.find('srcset="')
            if index == -1: break
            index +=8
            end = a.find('"', index)
            link = a[index:end]
            if link not in imagesLinks:
                imagesLinks.append(link)
            a = a[end::]
    print("donwloading, please wait...")
    for link in imagesLinks:
        fileList = os.listdir(DOWNLOADPATH)
        link = link.split(",")[-1]
        link = link[:link.index(" ")]
        research(link)
        sleep(0.5)
        info = scr.copyAll()
        if info != "":
            continue
        scr.savePage("{}.png".format(count))
        while os.listdir(DOWNLOADPATH) == fileList: pass
        count +=1
    print("{} pictures downloaded successfully".format(count-1)*(count>1) + "enable to download any photo..."*(count<2))

downloadAll("bestpixels")
#downloadProfilePic("_aero.art", False)

