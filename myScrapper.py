from time import sleep
from pynput.keyboard import Controller,Key
import win32clipboard as clip

keyboard = Controller()

def shortCut(hold, press, wait = 0.2, wait1 = 0.2,wait2 = 0):
    
    keyboard.press(hold)
    sleep(wait)
    keyboard.press(press)
    sleep(wait1)
    keyboard.release(hold)
    keyboard.release(press)
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
    shortCut(Key.ctrl, 's')
    
    sleep(0.6)
    clip.OpenClipboard()
    if saveAs == "":
        shortCut(Key.ctrl, "s")
        pressRelease(Key.enter)
        saveAs = clip.GetClipboardData()
        clip.CloseClipboard()
        return saveAs
    clip.EmptyClipboard()
    clip.SetClipboardText(saveAs)
    shortCut(Key.ctrl, "v")
    pressRelease(Key.enter)
    clip.CloseClipboard()
    return saveAs

def savePage(saveAs = ""):
    shortCut(Key.ctrl, 's')    
    sleep(0.6)
    clip.OpenClipboard()
    if saveAs == "":
        shortCut(Key.ctrl, "s")
        pressRelease(Key.enter)
        saveAs = clip.GetClipboardData()
        clip.CloseClipboard()
        return saveAs
    clip.EmptyClipboard()
    clip.SetClipboardText(saveAs)
    clip.CloseClipboard()
    shortCut(Key.ctrl, "v")
    pressRelease(Key.enter)
    return saveAs
        
    
    
    