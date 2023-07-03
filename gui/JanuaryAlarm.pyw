from tkinter import *
import tkinter as tkinter;
import csv;
import time;
from playsound import playsound
from time import *;
import time;

import keyboard as Input;
#print(time.strftime("%H:%M"))
import time
import datetime;
import os;

class JanuaryAlarm:
    def __init__(self):
        print("");

    def ShowAlarmWindow(self):
        self.GuiWindow = tkinter.Tk();
        self.GuiWindow.title("Alarm Menu"); self.GuiWindow.geometry("1920x1080");
        self.GuiWindow.state('zoomed');
        self.GuiWindow.overrideredirect(1);
        photoImages = tkinter.PhotoImage(file="memory\Alarm\Backgrounds\#9.png", master=self.GuiWindow);
        BgImages = tkinter.Label(self.GuiWindow, image=photoImages);
        self.TextReminder = tkinter.StringVar();
        self.TextHour = tkinter.StringVar();
        self.TextMin = tkinter.StringVar();
        self.TextFormat = tkinter.StringVar();
        ReminderLabel = tkinter.Label(self.GuiWindow,text="REMINDER",bg="#445B7B",fg="yellow",font=("Agency FB bold", 14), width="10", borderwidth="0")
        ReminderLabel.place(relx="0.4995", rely="0.370");
        Reminder = tkinter.Entry(self.GuiWindow, textvariable=self.TextReminder, bg="#445B7B", fg="yellow",font=("Agency FB bold", 25), width="15", borderwidth="0");
        Reminder.place(relx="0.4600", rely="0.4");
        HourLabel = tkinter.Label(self.GuiWindow, text="HOUR", bg="#445B7B", fg="yellow",font=("Agency FB bold", 14), width="10", borderwidth="0")
        HourLabel.place(relx="0.4250", rely="0.54");
        Hour = tkinter.Entry(self.GuiWindow, textvariable=self.TextHour, bg="#445B7B", fg="yellow",font=("Agency FB bold", 30),width="5", borderwidth="0");
        Hour.place(relx="0.4175", rely="0.57");
        MinLabel = tkinter.Label(self.GuiWindow, text="MINUTE", bg="#445B7B", fg="yellow", font=("Agency FB bold", 14),width="10", borderwidth="0")
        MinLabel.place(relx="0.4985", rely="0.54");
        Min = tkinter.Entry(self.GuiWindow, textvariable=self.TextMin, bg="#445B7B", fg="yellow", font=("Agency FB bold", 30),width="5", borderwidth="0");
        Min.place(relx="0.4895", rely="0.57");
        FormatLabel = tkinter.Label(self.GuiWindow, text="AM/PM", bg="#445B7B", fg="yellow", font=("Agency FB bold", 14),width="10", borderwidth="0")
        FormatLabel.place(relx="0.5700", rely="0.54");
        Format = tkinter.Entry(self.GuiWindow, textvariable=self.TextFormat, bg="#445B7B", fg="yellow",font=("Agency FB bold", 30),width="5", borderwidth="0");
        Format.place(relx="0.5615", rely="0.57");
        SaveButton = tkinter.Button(self.GuiWindow, width="16", text="SAVE", bg="#445B7B", fg="yellow",borderwidth="0",
                                    font=("Agency FB bold", 22), command=self.SaveAlarmTime);
        SaveButton.place(relx="0.470", rely="0.70");
        QuitButton=tkinter.Button(self.GuiWindow,bg="#445B7B",fg="yellow",text="CLOSE",font=("Agency FB bold", 15),width="8", height="1",borderwidth="0",command=quit);
        QuitButton.place(relx="0.502", rely="0.80");
        BgImages.pack();
        self.GuiWindow.mainloop();
    def SaveAlarmTime(self):
        Reminder=self.TextReminder.get();
        hour=self.TextHour.get();
        minute=self.TextMin.get();
        format=self.TextFormat.get();
        SaveTime = open("memory\Alarm\Alarm Time Save\Timer1.txt", mode="w");
        SaveTime.write("reminder,hour,minute,format\n");
        SaveTime.write(Reminder+","+hour+","+minute+","+format);
        SaveTime.close();
        self.GuiWindow.destroy();
    def MilitaryTimeConversion(self):
        with open("memory\Alarm\Alarm Time Save\Timer1.txt", mode="r") as csvReader:
            csvSearch=csv.DictReader(csvReader);
            for row in csvSearch:
                self.ExtractedReminder=row['reminder'];
                self.Extractedhour=row['hour'];
                self.Extractedminute=row['minute'];
                self.Extractedformat=row['format'];
            self.Extractedformat=self.Extractedformat.lower();
            if self.Extractedformat=="pm" and self.Extractedhour<"12":
                self.Extractedhour=int(self.Extractedhour)+12;
            if self.Extractedformat=="am" and self.Extractedhour=="12":
                self.Extractedhour=0;
                self.Extractedhour=int(self.Extractedhour);
    def RemindTheReminder(self):
        self.ExtractedReminder=self.ExtractedReminder.lower();
        if "coffee" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderCoffee.mp3");
        elif "tea" in self.ExtractedReminder or "tee" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderTea.mp3");
        elif "breakfast" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderBreakfast.mp3");
        elif "lunch" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderLunch.mp3");
        elif "dinner" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderDinner.mp3");
        elif "sleep" in self.ExtractedReminder or "rest" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderSleep.mp3");
        elif "shower" in self.ExtractedReminder:
            playsound("Voice/Reminders/ReminderShower.mp3");
    def InitiateAlarm(self):
        ShowTime = str(time.strftime("%H:%M:%S"));
        currentTime = datetime.datetime.now();
        Hour = currentTime.hour;
        Minute = currentTime.minute;
        AlarmLabel.configure(text=ShowTime);
        if int(Hour)==int(self.Extractedhour) and int(Minute)==int(self.Extractedminute):
            playsound("Voice\Reminders\AlarmAlarm.mp3"); j.RemindTheReminder();
            while 1:
                playsound("memory\Alarm\Tones\iClockBuzzer.mp3");
                if Input.is_pressed('F12'):
                    sleep(10);
                    quit();
        AlarmSystem.after(1000, j.InitiateAlarm);

j=JanuaryAlarm();
j.ShowAlarmWindow();
j.MilitaryTimeConversion();
AlarmSystem = tkinter.Tk();
AlarmSystem.title("Alarm Menu"); AlarmSystem.geometry("1920x1080");
AlarmSystem.state('zoomed');
AlarmSystem.overrideredirect(1);
photoImages = tkinter.PhotoImage(file="memory\Alarm\Backgrounds\#9.png", master=AlarmSystem);
BgImages = tkinter.Label(AlarmSystem, image=photoImages);
BgImages.pack();
QuitButton=tkinter.Button(AlarmSystem,bg="#445B7B",fg="yellow",text="CLOSE",font=("Agency FB bold", 15),width="8", height="1",borderwidth="0",command=quit);
QuitButton.place(relx="0.502", rely="0.80");
AlarmAt = Label(AlarmSystem,text="ALARM TIME:",bg="#000813",\
                 fg="yellow",font=("Agency FB bold", 20), width="12", height="1");
AlarmAt.place(relx="0.885", rely="0.85");
ShowInfo = Label(AlarmSystem,text=str(j.Extractedhour)+":"+str(j.Extractedminute)+" "+str(j.Extractedformat),bg="#000813",\
                 fg="yellow",font=("Agency FB bold", 20), width="10", height="1");
ShowInfo.place(relx="0.888", rely="0.90");
AlarmLabel = Label(AlarmSystem,text="",bg="#445B7B",fg="yellow",font=("Agency FB bold", 70), width="10", height="2");
AlarmLabel.place(relx="0.415", rely="0.380");
j.InitiateAlarm();
AlarmSystem.mainloop();