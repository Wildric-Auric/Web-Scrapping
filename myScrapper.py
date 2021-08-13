from time import sleep
from pynput.keyboard import Controller,Key
import win32clipboard as clip
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
keyboard = Controller()

def shortCut(holdArray, press, wait = 0.2, wait1 = 0.2,wait2 = 0):
    for hold in holdArray:
        keyboard.press(hold)
    sleep(wait)
    keyboard.press(press)
    sleep(wait1)
    keyboard.release(press)
    for hold in holdArray:
        keyboard.release(hold)
    sleep(wait2)
    
def pressRelease(key, wait = 0.1):
    keyboard.press(key)
    sleep(wait)
    keyboard.release(key)
    

def keyboardPrint(string, wait = 0):
    for i in string:
        pressRelease(i, wait = 0)
        sleep(wait)
        
def copyText(string):
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(string)
    clip.CloseClipboard()
    
def savePageSelenium(browser,adress,saveAs = ""):
    browser.get(adress)
    sleep(2)
    shortCut([Key.ctrl], 's')
    
    sleep(0.6)
    clip.OpenClipboard()
    if saveAs == "":
        shortCut([Key.ctrl], "s", wait2 = 0.4)
        pressRelease(Key.enter)
        saveAs = clip.GetClipboardData()
        clip.CloseClipboard()
        return saveAs
    clip.EmptyClipboard()
    clip.SetClipboardText(saveAs)
    shortCut([Key.ctrl], "v")
    pressRelease(Key.enter)
    clip.CloseClipboard()
    return saveAs

def savePage(saveAs = ""):
    shortCut([Key.ctrl], 's')    
    sleep(0.6)
    clip.OpenClipboard()
    if saveAs == "":
        shortCut([Key.ctrl], "s")
        pressRelease(Key.enter)
        saveAs = clip.GetClipboardData()
        clip.CloseClipboard()
        return saveAs
    clip.EmptyClipboard()
    clip.SetClipboardText(saveAs)
    clip.CloseClipboard()
    shortCut([Key.ctrl], "v")
    pressRelease(Key.enter)
    return saveAs
        
    
def clickOnElement(x,y):
    mouse.position = (x,y) #1480, 40, 1480, 120
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def getCurrentSrc():
    clickOnElement(1480, 40)
    sleep(0.1)
    clickOnElement(1480,120)
    sleep(2)
    shortCut([Key.ctrl], "a")
    sleep(1)
    shortCut([Key.ctrl], "c")
    sleep(0.3)
    clip.OpenClipboard()
    src = clip.GetClipboardData()
    clip.CloseClipboard()
    shortCut([Key.ctrl], "w")
    return src
    
def copyAll():
    try:
        shortCut([Key.ctrl], "a")
        sleep(1)
        shortCut([Key.ctrl], "c")
        clip.OpenClipboard()
        value = clip.GetClipboardData()
        clip.CloseClipboard()
    except: value = ""
    return value