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

old_value = 0;
def update_clock():
    if Input.is_pressed('F9'):
        buttonHide();
    elif Input.is_pressed('F10'):
        buttonShow();
    currentTime = datetime.datetime.now();
    Hour = currentTime.hour;
    Minute = currentTime.minute;
    Second = currentTime.second;
    Shift = str(currentTime.strftime("%p"));
    RAM = psutil.virtual_memory().percent
    if Hour == 0:
        Hour = 12;
    if Hour > 12:
        Hour = Hour - 12;
    Hours.configure(text=str(Hour) + ":");
    Minutes.configure(text=str(Minute) + ":");
    Seconds.configure(text=Second);
    CPU = psutil.cpu_percent();
    CPU_Value.configure(text=CPU);
    RAMs.configure(text=RAM);
    interface.after(1000, update_clock)

def buttonHide():
    interface.withdraw()

def buttonShow():
    interface.deiconify()

def aaa():
    print("asas");

interface=t.Tk();
interface.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
interface.geometry('%dx%d+%d+%d' % (280, 200, 1600, 35));
interface.overrideredirect(1);


def desktop():
    os.system('explorer ');

def games():
    os.system('explorer E:\\january\\games\\');

def workspace():
    os.system("start cmd"); sleep(0.4);
    keyboard.type("Jv3.py"); keyboard.press(Key.enter); keyboard.release(Key.enter);
    sleep(3);

def recycle():
    os.system("start cmd"); sleep(0.4);
    keyboard.type("start shell:RecycleBinFolder"); keyboard.press(Key.enter); keyboard.release(Key.enter);
    sleep(3);

def browser():
    webbrowser.open_new("https://www.google.com/");


import tkinter as t;
explorer=t.Tk(); explorer.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
explorer.geometry('%dx%d+%d+%d' % (200, 111, 0.5, 295)); explorer.overrideredirect(1);
photoImage0 = t.PhotoImage(file="Memory/Icons/neon2.png", master=explorer);
BgImage0 = t.Label(explorer, image=photoImage0); BgImage0.pack();
Computer = t.Button(explorer,text="DESKTOP",bg="black",fg="#1CFDE4",font=("Agency FB bold", 15), width="10", height="1",borderwidth=0, command=desktop);
Computer.place(relx="0.320", rely="0.02");

explorer2=t.Tk(); explorer2.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
explorer2.geometry('%dx%d+%d+%d' % (200, 111, 0.5, 495)); explorer2.overrideredirect(1);
photoImage2 = t.PhotoImage(file="Memory/Icons/neon2.png", master=explorer2);
BgImage2 = t.Label(explorer2, image=photoImage2);
BgImage2.pack();
Computer = t.Button(explorer2,text="GAMES",bg="black",fg="#1CFDE4",font=("Agency FB bold", 15), width="10", height="1",borderwidth=0, command=games);
Computer.place(relx="0.320", rely="0.02");

explorer3=t.Tk();
explorer3.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
explorer3.geometry('%dx%d+%d+%d' % (200, 111, 0.5, 695));
explorer3.overrideredirect(1);
photoImage3 = t.PhotoImage(file="Memory/Icons/neon2.png", master=explorer3);
BgImage3 = t.Label(explorer3, image=photoImage3);
BgImage3.pack();
Computer = t.Button(explorer3,text="JANUARY",bg="black",fg="#1CFDE4",font=("Agency FB bold", 15), width="10", height="1",borderwidth=0, command=workspace);
Computer.place(relx="0.320", rely="0.02");

explorer4=t.Tk();
explorer4.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
explorer4.geometry('%dx%d+%d+%d' % (200, 111, 1730, 495));
explorer4.overrideredirect(1);
photoImage4 = t.PhotoImage(file="Memory/Icons/neon2.png", master=explorer4);
BgImage4 = t.Label(explorer4, image=photoImage4);
BgImage4.pack();
Computer = t.Button(explorer4,text="RECYCLE BIN",bg="black",fg="#1CFDE4",font=("Agency FB bold", 15), width="15", height="1",borderwidth=0, command=recycle);
Computer.place(relx="0.250", rely="0.02");

explorer5=t.Tk();
explorer5.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
explorer5.geometry('%dx%d+%d+%d' % (200, 111, 1730, 695));
explorer5.overrideredirect(1);
photoImage5 = t.PhotoImage(file="Memory/Icons/neon2.png", master=explorer5);
BgImage5 = t.Label(explorer5, image=photoImage5);
BgImage5.pack();
Computer = t.Button(explorer5,text="TERMINATE",bg="black",fg="#1CFDE4",font=("Agency FB bold", 15), width="15", height="1",borderwidth=0, command=quit);
Computer.place(relx="0.250", rely="0.02");

explorer6=t.Tk();
explorer6.title("January Alarm Notification v 1.0");
#root.geometry("920x180");
explorer6.geometry('%dx%d+%d+%d' % (200, 111, 1730, 295));
explorer6.overrideredirect(1);
photoImage6 = t.PhotoImage(file="Memory/Icons/neon2.png", master=explorer6);
BgImage6 = t.Label(explorer6, image=photoImage6);
BgImage6.pack();
Computer = t.Button(explorer6,text="BROWSER",bg="black",fg="#1CFDE4",font=("Agency FB bold", 15), width="15", height="1",borderwidth=0, command=browser);
Computer.place(relx="0.250", rely="0.02");



photoImage = t.PhotoImage(file="Memory/Alarm/Backgrounds/#7s.png", master=interface);
BgImage = t.Label(interface, image=photoImage);
BgImage.pack();
CPU_Title = t.Label(interface,text="CPU",bg="#050737",fg="#1CFDE4",font=("Agency FB bold", 15), width="3", height="1");
CPU_Title.place(relx="0.52", rely="0.32");
CPU_Value = t.Label(interface,text="",bg="#050737",fg="#1CFDE4",font=("Agency FB bold", 25), width="4", height="1");
CPU_Value.place(relx="0.49", rely="0.44");

Time_Title = t.Label(interface,text="TIME",bg="black",fg="#009CFF",font=("Agency FB bold", 13), width="4", height="1");
Time_Title.place(relx="0.14", rely="0.05");
Hours = t.Label(interface,text="",bg="black",fg="#009CFF",font=("Agency FB bold", 24), width="2", height="1")
Hours.place(relx="0.05", rely="0.15");
Minutes = t.Label(interface,text="",bg="black",fg="#009CFF",font=("Agency FB bold", 24), width="2", height="1");
Minutes.place(relx="0.15", rely="0.15");
Seconds = t.Label(interface,text="",bg="#040426",fg="#009CFF",font=("Agency FB bold", 24), width="2", height="1");
Seconds.place(relx="0.27", rely="0.15");

RAMs_Title = t.Label(interface,text="RAM USAGE",bg="black",fg="#009CFF",font=("Agency FB bold", 12), width="9", height="1");
RAMs_Title.place(relx="0.05", rely="0.60");
RAMs = t.Label(interface,text="",bg="black",fg="#009CFF",font=("Agency FB bold", 18), width="7", height="1");
RAMs.place(relx="0.03", rely="0.70");

interface.wm_attributes("-topmost", 1);
update_clock();explorer.mainloop();
#roots.mainloop();
interface.mainloop();