import os
from playsound import playsound
import webbrowser
from random import randint
from time import sleep
from textblob import TextBlob;
import datetime;
import requests;
import csv;
import time;
from os import system;
import psutil;
import keyboard as Input;
#from tkinter import;
import tkinter as t;
#QUICK_LINK#1 : https://notevibes.com/
from pynput.keyboard import Key, Controller;
keyboard = Controller();
from pynput.mouse import Button, Controller;
mouse = Controller();

playsound("Voice/BgSound/ButtonClick1.wav");sleep(0.5);
playsound("Voice/BgSound/ButtonClick1.wav");

def startActivation():
    Activate = open("memory\logs\InSyncWithActivationFile.txt", "w");
    Activate.write("sync\n");
    Activate.write("1");
    Activate.close();

def continue_or_exit():
    with open("memory\logs\InSyncWithActivationFile.txt", mode="r") as csv_fileReader:
        csv_reader = csv.DictReader(csv_fileReader);
        #lines = 0;
        for row in csv_reader:
            x=row["sync"];
        if x=="0":
            quit();

def readReminderFile():
    global i;
    with open("memory\Reminders\ShortReminder.txt", mode="r") as csv_fileReader:
        csv_reader = csv.DictReader(csv_fileReader);
        for row in csv_reader:
            hour=row["hour"];
            minute=row["min"];
            reminder=row["reminder"];
    currentTime = datetime.datetime.now();
    if int(hour)!=int(currentTime.hour) or int(minute)!=int(currentTime.minute):
        i=0;
    if int(hour)==int(currentTime.hour) and int(minute)==int(currentTime.minute):
        i=i+1;
        if i<=1:
            playsound("Voice/BgSound/ButtonClick1.wav");
            playsound("Voice/BgSound/ButtonClick1.wav");
            playsound("Voice/Reminders/RemindYouAbout.mp3");
            if "coffee" in reminder:
                playsound("Voice/Reminders/ReminderCoffee.mp3");
            elif "tea" in reminder or "tee" in reminder:
                playsound("Voice/Reminders/ReminderTea.mp3");
            elif "breakfast" in reminder:
                playsound("Voice/Reminders/ReminderBreakfast.mp3");
            elif "lunch" in reminder:
                playsound("Voice/Reminders/ReminderLunch.mp3");
            elif "dinner" in reminder:
                playsound("Voice/Reminders/ReminderDinner.mp3");
            elif "sleep" in reminder or "rest" in reminder:
                playsound("Voice/Reminders/ReminderSleep.mp3");
            elif "shower" in reminder:
                playsound("Voice/Reminders/ReminderShower.mp3");
    if int(currentTime.hour)==7 and int(currentTime.minute)==00 and int(currentTime.second)>=1 and int(currentTime.second)<=4:
            playsound("Voice/Reminders/RemBreakfast1.mp3");
    elif int(currentTime.hour)==9 and int(currentTime.minute)==00 and int(currentTime.second)>=1 and int(currentTime.second)<=4:
            playsound("Voice/Reminders/RemBreakfast2.mp3");
    elif int(currentTime.hour)==13 and int(currentTime.minute)==00 and int(currentTime.second)>=1 and int(currentTime.second)<=4:
            playsound("Voice/Reminders/RemLunch1.mp3");
    elif int(currentTime.hour)==15 and int(currentTime.minute)==00 and int(currentTime.second)>=1 and int(currentTime.second)<=4:
            playsound("Voice/Reminders/RemLunch2.mp3");
    elif int(currentTime.hour) == 21 and int(currentTime.minute) == 00 and int(currentTime.second) >= 1 and int(currentTime.second) <= 4:
        playsound("Voice/Reminders/RemDinner1.mp3");
    elif int(currentTime.hour) == 23 and int(currentTime.minute) == 00 and int(currentTime.second) >= 1 and int(currentTime.second) <= 4:
        playsound("Voice/Reminders/RemDinner2.mp3");
    elif int(currentTime.hour) == 1 and int(currentTime.minute) == 00 and int(currentTime.second) >= 1 and int(currentTime.second) <= 4:
        playsound("Voice/Reminders/RemSleep1.mp3");
    elif int(currentTime.hour) == 3 and int(currentTime.minute) == 00 and int(currentTime.second) >= 1 and int(currentTime.second) <= 4:
        playsound("Voice/Reminders/RemSleep2.mp3");
    elif int(currentTime.hour) == 5 and int(currentTime.minute) == 00 and int(currentTime.second) >= 1 and int(currentTime.second) <= 4:
        playsound("Voice/Reminders/RemSleep3.mp3");

def destroy():
    #if Input.is_pressed('F12'): playsound("Voice/BgSound/ButtonClick1.wav");sleep(0.3);playsound("Voice/BgSound/ButtonClick1.wav");quit();
    continue_or_exit();
    readReminderFile();
    print("running")
    Activation.after(200, destroy);

#startActivation();
i=0;
Activation =t.Tk();
Activation.geometry('%dx%d+%d+%d' % (390, 80, 1490, 235)); Activation.overrideredirect(1);
photoImage = t.PhotoImage(file="memory/Alarm/Backgrounds/#8a.png", master=Activation);
BgImage = t.Label(Activation, image=photoImage);
BgImage.pack();
destroy();
Activation.mainloop();
playsound("Voice/BgSound/ButtonClick1.wav");sleep(0.5);
