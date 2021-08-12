#This script was created for the automatization of dowloads of berserk from Mangakalot

from selenium import webdriver
from time import sleep
import os
#rom win32com.client import Dispatch

from shutil import copyfile
from pynput.keyboard import Key
from myScrapper import *



PATH = r"C:\Program Files (x86)\chromedriver.exe"
SAVEPATH = r"C:\Users\HP\Downloads"
PLAYLIST = r"C:\Users\HP\Downloads\Playlist"
browser = webdriver.Chrome(PATH)

start, end = 329, 345


def saveMany(browser,start,end):
    filesNum = len(os.listdir(SAVEPATH))
    for i in range(start, end+1):
        savePageSelenium(browser,"https://readmanganato.com/manga-ma952557/chapter-" +str(i))
        while (len(os.listdir(SAVEPATH)) != filesNum +2):
            pass
        else: filesNum +=2
        sleep(0.2)




def specialSort(lis):
    for i in range(len(lis)-1):
        if ".jpg" in lis[i]:
            num = lis[i].split(".")[0]
            if num.isdigit():
                num = int(num)
                temp = i
                for j in range(i+1, len(lis)-1):
                    if ".jpg" in lis[i]:
                        num1 = (lis[j].split(".")[0])
                        if num1.isdigit():
                            num1 = int(num1)
                            if num1 < int(lis[temp].split(".")[0]): temp = j
                lis[i],lis[temp] = lis[temp],lis[i]
                

def createPlaylist(path):
    order = 1
    #shell = Dispatch("WScript.Shell") As you will see after I first attempted to create shortcuts in the playlist folder but a shortcut in it's definition lead you to the file in it's the original directory which I don't want 
    allFolders = os.listdir(SAVEPATH)
    for folder in allFolders:
        if  os.path.isdir(os.path.join(SAVEPATH,folder)):
            newGlobalPath = os.path.join(SAVEPATH, folder)
            allImages = os.listdir(newGlobalPath)
            specialSort(allImages)
            for image in allImages:
                if ((".jpg" in image) or (".png" in image)) and image.split(".")[0].isdigit():
                        # shortCut = shell.CreateShortcut(os.path.join(os.path.join(SAVEPATH, "Playlist"),str(order) + ".lnk"))
                        # shortCut.Targetpath = os.path.join(newGlobalPath, image)
                        # shortCut.IconLocation = os.path.join(newGlobalPath, image)
                        # shortCut.save()
                        src = os.path.join(newGlobalPath, image)
                        copyfile(src, os.path.join(PLAYLIST,str(order) + ".jpg"))
                        order += 1
    print("PLAYLIST CREATED SUCCESSFULLY, ENJOY!")
            

createPlaylist(PLAYLIST)