import os
from playsound import playsound
import webbrowser
from random import randint
from time import sleep
from textblob import TextBlob;
import datetime;
import requests;
import csv;
import psutil;
import time;
from os import system
import keyboard as Input;
from tkinter import *;
#QUICK_LINK#1 : https://notevibes.com/
from pynput.keyboard import Key, Controller;
keyboard = Controller();
from pynput.mouse import Button, Controller;
mouse = Controller();
import speech_recognition as sr;
r = sr.Recognizer();
from random import randint;

class January:
    Unrecognized=0;
    def __init__(self):
        print("January Activated (Version 3.0.1)");
        self.Greetings = ["hi", "hello", "hey"];
        self.Intro = ["who are you", "introduce yourself", "what's your name", "what are you"];
        self.Status = ["how are you", "your status", "you alright"]

    def januaryActivated(self):
        #os.system('explorer C\\Users\\USER\\PycharmProjects\\January\\');
        os.system("start cmd");sleep(0.3);
        keyboard.type("Activation.pyw");sleep(0.1);
        keyboard.press(Key.enter);keyboard.release(Key.enter);sleep(0.3);
        keyboard.press(Key.alt);keyboard.press(Key.f4);keyboard.release(Key.alt);keyboard.release(Key.f4);

    def CurrentTimeIs(self):
        FixedPath="Voice/Time/"; Extension=".mp3";
        currentTime = datetime.datetime.now();
        Hour = currentTime.hour;  Minute = currentTime.minute; Shift = str(currentTime.strftime("%p"));
        if Hour==0 :
            Hour=12;
        if Hour > 12:
            Hour=Hour-12;
        playsound(FixedPath+"CurrentTime"+Extension);  playsound(FixedPath+str(Hour)+Extension);
        if Minute!=0:
            playsound(FixedPath+str(Minute)+Extension);
        elif Minute ==0:
            playsound(FixedPath +"Oclock"+ Extension);
        if Shift=="AM":
            playsound(FixedPath+"am"+Extension);
        elif Shift=="PM":
            playsound(FixedPath+"pm"+Extension);
    def CurrentWeatherIs(self):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=14008bd96f0536a2856b5ba6e5e9a350&q=';
        city = "dhaka";
        url = api_address + city;
        json_data = requests.get(url).json();
        weather = json_data['weather'][0]['description'].lower();
        temperature = json_data['main']['temp']
        kelvinToCelcius = int(temperature - 273.15);
        # For Bangladesh Estimation Only:
        if kelvinToCelcius <= 21:
            kelvinToCelcius = 21;
            actualTemp = str(kelvinToCelcius);
        elif kelvinToCelcius >= 34:
            kelvinToCelcius = 34;
            actualTemp = str(kelvinToCelcius);
        else:
            actualTemp = str(kelvinToCelcius);

        pcDirectory = "Voice/Weathers/";
        extensions = ".mp3";
        weatherFilePath = pcDirectory + weather + extensions;
        TempFilePath = pcDirectory + actualTemp + extensions;
        playsound("Voice/Weathers/CurrentWeather.mp3");
        playsound(weatherFilePath);
        playsound("Voice/Weathers/TemperatureIs.mp3");
        if actualTemp > "40":
            playsound("Voice/Weathers/over40.mp3");
        playsound(TempFilePath);
        playsound("Voice/Weathers/DegreeCelsius.mp3");
    def CurrentDateIs(self):
        global Day, WeekDay, Month, Year;
        currentDT = datetime.datetime.now();
        Day = str(currentDT.day);
        Month = str(currentDT.month);
        Year = str(currentDT.year)[2:4];
        WeekDay = str(datetime.datetime.today().weekday());
        Extensions = ".mp3"
        playsound("Voice/Time/CurrentDateIs" + Extensions);
        playsound("Voice/Time/" + Day + Extensions);
        playsound("Voice/Time/" + "M" + Month + Extensions);
        playsound("Voice/Time/2000" + Extensions);
        playsound("Voice/Time/" + Year + Extensions);
        playsound("Voice/Time/TodayIs" + Extensions);
        playsound("Voice/Time/" + "D" + WeekDay + Extensions);
    def getCurrentTime(self):
        GetCurrentTime = datetime.datetime.now();
        return GetCurrentTime;
    def AnalyzeSentiment(self):
        global Polarity;
        Polarity=0;
        Analysis = TextBlob(SpokenWords);
        Polarity += Analysis.sentiment.polarity;
        print(Polarity);

    def replyGreet(self):
        randNum = str(randint(1, 14));
        filePath = "Voice/Greetings/";
        fileType = "Hello"
        extensions = ".mp3";
        playsound(filePath + fileType + randNum + extensions);
    def replyIntro(self):
        playsound("Voice/Introduction.mp3");
    def replyStatus(self):
            randNum = str(randint(1, 4));
            filePath = "Voice/";
            fileType = "Status"
            extentions = ".mp3";
            playsound(filePath + fileType + randNum + extentions);

    def feeling(self):
        global SpokenWords; SpokenWords=SpokenWords.lower();
        if "not" in SpokenWords and "good" in SpokenWords or "not" in SpokenWords and "well" in SpokenWords or "not" in SpokenWords and "ok" in SpokenWords \
                or "not" in SpokenWords and "okay" in SpokenWords or "not" in SpokenWords and "alright" in SpokenWords:
            playsound("Voice/Feel-2.mp3");
        elif "don't" in SpokenWords and "good" in SpokenWords or "don't" in SpokenWords and "well" in SpokenWords or "don't" in SpokenWords and "ok" in SpokenWords \
                or "don't" in SpokenWords and "okay" in SpokenWords or "don't" in SpokenWords and "alright" in SpokenWords:
            playsound("Voice/Feel-2.mp3");
        # NOT BAD+VERY BAD
        elif "not" in SpokenWords and "bad" in SpokenWords or "not" in SpokenWords and "depressed" in SpokenWords or "not" in SpokenWords and "dull" in SpokenWords \
                or "not" in SpokenWords and "worse" in SpokenWords or "not" in SpokenWords and "worst" in SpokenWords\
                or "not" in SpokenWords and "sad" in SpokenWords:
            playsound("Voice/Feel0.mp3");
        elif "don't" in SpokenWords and "bad" in SpokenWords or "don't" in SpokenWords and "depressed" in SpokenWords or "don't" in SpokenWords and "dull" in SpokenWords \
                or "don't" in SpokenWords and "worse" in SpokenWords or "don't" in SpokenWords and "worst" in SpokenWords\
                or "don't" in SpokenWords and "sad" in SpokenWords:
            playsound("Voice/Feel0.mp3");
        # GOOD
        elif "good" in SpokenWords or "well" in SpokenWords or "ok" in SpokenWords or "okay" in SpokenWords or "alright" in SpokenWords:
            playsound("Voice/Feel+1.mp3");
        # BAD+VERY BAD
        elif "bad" in SpokenWords or "dull" in SpokenWords or "depressed" in SpokenWords or "worse" in SpokenWords\
                or "worst" in SpokenWords or "sad" in SpokenWords:
            playsound("Voice/Feel-3.mp3");
        # NOT GREAT
        elif "not" in SpokenWords and "great" in SpokenWords or "not" in SpokenWords and "perfect" in SpokenWords\
                or "not" in SpokenWords and "awesome" in SpokenWords or "not" in SpokenWords and "superb" in SpokenWords\
                or "not" in SpokenWords and "happy" in SpokenWords:
            playsound("Voice/Feel-2.mp3");
        elif "don't" in SpokenWords and "great" in SpokenWords or "don't" in SpokenWords and "perfect" in SpokenWords\
                or "don't" in SpokenWords and "awesome" in SpokenWords or "don't" in SpokenWords and "superb" in SpokenWords\
                or "don't" in SpokenWords and "happy" in SpokenWords:
            playsound("Voice/Feel-2.mp3");
        # GREAT
        elif "great" in SpokenWords or "perfect" in SpokenWords or "awesome" in SpokenWords or "superb" in SpokenWords or "happy" in SpokenWords:
            playsound("Voice/Feel+2.mp3");

    def replythanks(self):
        randNum = str(randint(1, 3));
        filePath = "Voice/";
        fileType = "ThanksReply"
        extensions = ".mp3";
        playsound(filePath+fileType+randNum+extensions);

    def replysorry(self):
        randNum = str(randint(1, 3));
        filePath = "Voice/";
        fileType = "SorryReply"
        extensions = ".mp3";
        playsound(filePath+fileType+randNum+extensions);

    def replypresence(self):
        randNum = str(randint(1, 3));
        filePath = "Voice/";
        fileType = "UThereReply"
        extensions = ".mp3";
        playsound(filePath+fileType+randNum+extensions);

    def maintainence_LogInTimestamps(self):
        with open('memory/logs/logIn_Timestamps.txt', mode='r') as csv_fileReader:
            csv_reader = csv.DictReader(csv_fileReader); lines=0;
            for row in csv_reader:
                lines=lines+1;
        print(lines);
        if lines >=10:
            with open("memory/logs/logIn_Timestamps.txt", mode="w") as csv_fileWriter:
                csv_fileWriter.write("logIn_Timestamps"+"\n");
        with open("memory/logs/logIn_Timestamps.txt", mode="a") as csv_fileAppend:
            csv_fileAppend.write(str(j.getCurrentTime())+"\n");

    def farewell(self):
        randNum = str(randint(1, 3));
        filePath = "Voice/";
        fileType = "GoodBye"
        extensions = ".mp3";
        playsound(filePath+fileType+randNum+extensions);
        j.maintainence_LogInTimestamps();
        if "computer" in SpokenWords or "pc" in SpokenWords:
            os.system("start cmd"); sleep(0.4);
            keyboard.type("shutdown /s /t 5");
            keyboard.press(Key.enter);
            keyboard.release(Key.enter);
        quit();

    def wait(self):
        randNum = str(randint(1, 4));
        filePath = "Voice/";
        fileType = "WaitReply"
        extensions = ".mp3";
        playsound(filePath+fileType+randNum+extensions);
        while 1:
                sleep(2);
                j.actionListener();
                if "start" in SpokenWords or "you there" in SpokenWords or "january" in SpokenWords:
                    playsound("Voice/ImBack.mp3");
                    break;

    def folderMode(self):
        randNum = str(randint(1, 4));
        filePath = "Voice/";
        fileType = "udosth"
        extensions = ".mp3";
        playsound(filePath+fileType+randNum+extensions);
        playsound("Voice/FolderModeOn.mp3");
        sleep(0.4);
        while 1:
            j.actionListener();
            if "write " in SpokenWords or "type " in SpokenWords:
                j.AI_Ok();
                playsound("Voice/LoopWriting.mp3");
                sleep(1);
                while 1:
                    j.actionListener();
                    if "stop" in SpokenWords:
                        j.AI_Ok();
                        break;
                    keyboard.type(SpokenWords);
                    keyboard.type(" ");
                playsound("Voice/FolderModeWaiting.mp3");
                sleep(0.4);
            elif "copy" in SpokenWords:
                playsound("Voice/Copy.mp3");
                keyboard.press(Key.ctrl); keyboard.press("c"); sleep(0.7);
                keyboard.release(Key.ctrl); keyboard.release("c");
                playsound("Voice/FolderModeWaiting.mp3");
                sleep(0.4);
            elif "paste" in SpokenWords or "hate" in SpokenWords or "face" in SpokenWords or "please" in SpokenWords \
                    or "haste" in SpokenWords or "taste" in SpokenWords:
                if SpokenWords == "":
                    playsound("Voice/PasteFailed.mp3");
                else:
                    playsound("Voice/Paste.mp3");
                    keyboard.press(Key.ctrl); keyboard.press("v");
                    keyboard.release(Key.ctrl); keyboard.release("v");
                playsound("Voice/FolderModeWaiting.mp3"); sleep(0.4);
            elif "create" in SpokenWords and "new" in SpokenWords and "folder" in SpokenWords:
                j.AI_Ok();
                keyboard.press(Key.ctrl); keyboard.press(Key.shift); keyboard.press("n");
                keyboard.release(Key.ctrl); keyboard.release(Key.shift); keyboard.release("n");
                sleep(0.3);
                fileType = "NewFolderName";
                extensions = ".mp3"
                filePath="Voice/";
                randNum = str(randint(1, 4));
                playsound(filePath + fileType + randNum + extensions);
                while 1:
                    j.actionListener();
                    if SpokenWords == "":
                        playsound("Voice/Error2.mp3");
                    elif "call it" in SpokenWords:
                        wordSplit = SpokenWords.split("call it ");
                        encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",","");
                        keyboard.type(encryptedSearch);
                        keyboard.press(Key.enter);
                        keyboard.release(Key.enter);
                        playsound("Voice/FolderCreated.mp3");
                        break;
                    elif "call this" in SpokenWords:
                        wordSplit = SpokenWords.split("call this ");
                        encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",","");
                        keyboard.type(encryptedSearch);
                        keyboard.press(Key.enter);
                        keyboard.release(Key.enter);
                        playsound("Voice/FolderCreated.mp3");
                        break;
                    else:
                        keyboard.type(SpokenWords);
                        keyboard.press(Key.enter);
                        keyboard.release(Key.enter);
                        playsound("Voice/FolderCreated.mp3");
                        break;
                playsound("Voice/FolderModeWaiting.mp3");
                sleep(0.4);
            elif "delete" in SpokenWords:
                while 1 :
                    playsound("Voice/DelTempQuery.mp3");
                    j.actionListener();
                    if "yes" in SpokenWords or "do it" in SpokenWords or "delete" in SpokenWords:
                        keyboard.press(Key.delete);keyboard.release(Key.delete);
                        playsound("Voice/Del.mp3");
                        playsound("Voice/DelRecycleBinRem.mp3"); break;
                    elif "no" in SpokenWords or "cancel" in SpokenWords or "ignore" in SpokenWords or "sorry" in SpokenWords:
                        j.AI_Ok();
                        break;
            elif "search" in SpokenWords:
                keyboard.press(Key.f3); keyboard.release(Key.f3);
                if "search for" in SpokenWords:
                    wordSplit = SpokenWords.split("search for ");
                    encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",", "");
                    keyboard.type(encryptedSearch);
                elif "search" in SpokenWords:
                    wordSplit = SpokenWords.split("search ");
                    encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",", "");
                    keyboard.type(encryptedSearch);

            elif "deactivate folder mode" in SpokenWords:
                j.AI_Ok();
                playsound("Voice/FolderModeOff.mp3");
                break;

            elif Unrecognized == 1:
                randNum = str(randint(1, 9));
                filePath = "Voice/";
                fileType = "Error";
                extensions = ".mp3"
                playsound(filePath + fileType + randNum + extensions);

    def programLauncher(self):
        if "firefox" in SpokenWords or "Firefox" in SpokenWords:
            j.AI_Ok();
            webbrowser.open_new("https://www.google.com/");
        elif "new tab" in SpokenWords or "a new tab" in SpokenWords or "app" in SpokenWords:
            j.AI_Ok();
            keyboard.press(Key.ctrl); keyboard.press("t");
            keyboard.release("t");keyboard.release(Key.ctrl);
        elif "google" in SpokenWords or "Google" in SpokenWords:
            playsound("Voice/StartGgL.mp3");
            webbrowser.open_new("https://www.google.com/");sleep(0.7);
            playsound("Voice/SearchWeb.mp3");
            j.actionListener();
            if "search for" in SpokenWords:
                wordSplit = SpokenWords.split("search for ");
                encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",", "");
                keyboard.type(encryptedSearch);
                keyboard.press(Key.enter);
                keyboard.release(Key.enter);
            elif "search" in SpokenWords:
                wordSplit = SpokenWords.split("search ");
                encryptedSearch = str(wordSplit).replace("[", "").replace("]", "").replace("'", "").replace(",", "");
                keyboard.type(encryptedSearch);
                keyboard.press(Key.enter);
                keyboard.release(Key.enter);
            elif "no" in SpokenWords or "I'm good" in SpokenWords:
                playsound("Voice/ok5.mp3");
            else :
                encryptedSearch=SpokenWords;
                keyboard.type(encryptedSearch);
                keyboard.press(Key.enter);keyboard.release(Key.enter);
        elif "Facebook" in SpokenWords or "facebook" in SpokenWords:
            playsound("Voice/StartFB.mp3");
            webbrowser.open_new("https://www.facebook.com/");
            sleep(0.7);
            playsound("Voice/Suggestions/FacebookLogInConfirmation.mp3");
            j.actionListener();
            if "authorization" in SpokenWords or "authorisation" in SpokenWords or "566" in SpokenWords:
                playsound("Voice/Suggestions/LogginInFB.mp3");i=0;
                while i < 4 :
                    keyboard.press(Key.shift);keyboard.press(Key.tab);
                    keyboard.release(Key.shift);keyboard.release(Key.tab);
                    i+=1;

                OpenCredentials = open('Memory/Others/Details/facebook.txt', 'r');
                with OpenCredentials as csv_file:
                    csv_reader = csv.DictReader(csv_file);
                    iteration = 0; username=""; password="";
                    for row in csv_reader:
                        username= row['user'];password=row['pass'];iteration += 1;
                    OpenCredentials.close();
                keyboard.type(username); keyboard.press(Key.tab);keyboard.release(Key.tab);
                keyboard.type(password); keyboard.press(Key.enter);keyboard.release(Key.enter);
            else:
                playsound("Voice/Suggestions/CantAccess.mp3");
                keyboard.press(Key.ctrl);keyboard.press('w');keyboard.release('w');keyboard.release(Key.ctrl);
        elif "twitter" in SpokenWords or "Twitter" in SpokenWords:
            playsound("Voice/StartTwt.mp3");
            webbrowser.open_new("https://www.twitter.com/");
            sleep(0.7);
            playsound("Voice/Suggestions/TwitterLogInConfirmation.mp3");
            j.actionListener();
            if "authorization" in SpokenWords or "authorisation" in SpokenWords or "566" in SpokenWords:
                playsound("Voice/Suggestions/LogginInTwitter.mp3");
                OpenCredentials = open('Memory/Others/Details/twitter.txt', 'r');
                with OpenCredentials as csv_file:
                    csv_reader = csv.DictReader(csv_file);
                    iteration = 0; username=""; password="";
                    for row in csv_reader:
                        username= row['user'];password=row['pass'];iteration += 1;
                    OpenCredentials.close();
                mouse.position = (1335, 128); mouse.press(Button.left); mouse.release(Button.left); sleep(0.8);
                keyboard.press(Key.ctrl); keyboard.press("a");  keyboard.release(Key.ctrl); keyboard.release("a"); sleep(0.4)
                keyboard.type(username);  mouse.position = (1561, 121); mouse.press(Button.left); mouse.release(Button.left); sleep(0.4)
                keyboard.type(password); mouse.position = (1720, 128); mouse.press(Button.left); mouse.release(Button.left);
        elif "proxy" in SpokenWords or "Proxy" in SpokenWords:
            playsound("Voice/StartProxy.mp3");
            webbrowser.open_new("https://www.proxysite.com/");
        elif "piratebay" in SpokenWords or "pirate bay" in SpokenWords:
            playsound("Voice/StartPirateBay.mp3");
            webbrowser.open_new("https://www.thepiratebay.org/");
        elif "gmail" in SpokenWords or "Gmail" in SpokenWords:
            playsound("Voice/StartGmail.mp3");
            webbrowser.open_new("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin");
            sleep(0.8);
            playsound("Voice/Suggestions/MailLogInConfirmation.mp3");
            j.actionListener();
            if "authorization" in SpokenWords or "authorisation" in SpokenWords or "566" in SpokenWords:
                playsound("Voice/Suggestions/LogginInMail.mp3");
                OpenCredentials = open('Memory/Others/Details/Gmail.txt', 'r');
                with OpenCredentials as csv_file:
                    csv_reader = csv.DictReader(csv_file);
                    iteration = 0; username=""; password="";
                    for row in csv_reader:
                        username= row['user'];password=row['pass'];iteration += 1;
                    OpenCredentials.close();
                keyboard.type(username);
                keyboard.press(Key.enter);keyboard.release(Key.enter); sleep(1.5);
                keyboard.type(password); keyboard.press(Key.enter);keyboard.release(Key.enter);
            else:
                playsound("Voice/Suggestions/CantAccess.mp3");
                keyboard.press(Key.ctrl);keyboard.press('w');keyboard.release('w');keyboard.release(Key.ctrl);
        elif "Yahoo Mail" in SpokenWords or "yahoo mail" in SpokenWords:
            playsound("Voice/StartYahoo.mp3");
            webbrowser.open_new("https://login.yahoo.com/"); sleep(0.8);
            playsound("Voice/Suggestions/MailLogInConfirmation.mp3");
            j.actionListener();
            if "authorization" in SpokenWords or "authorisation" in SpokenWords or "566" in SpokenWords:
                playsound("Voice/Suggestions/LogginInMail.mp3");
                OpenCredentials = open('Memory/Others/Details/YahooMail.txt', 'r');
                with OpenCredentials as csv_file:
                    csv_reader = csv.DictReader(csv_file);
                    iteration = 0;  username = "";  password = "";
                    for row in csv_reader:
                        username = row['user'];password = row['pass'];iteration += 1;
                    OpenCredentials.close();
                keyboard.type(username);
                keyboard.press(Key.enter);keyboard.release(Key.enter); sleep(1.5);
                keyboard.type(password);keyboard.press(Key.enter); keyboard.release(Key.enter);
            else:
                playsound("Voice/Suggestions/CantAccess.mp3");
                keyboard.press(Key.ctrl);
                keyboard.press('w');keyboard.release('w');
                keyboard.release(Key.ctrl);
        elif "microsoft mail" in SpokenWords or "Live mail" in SpokenWords or "live account" in SpokenWords \
                or "Microsoft account" in SpokenWords or "Outlook" in SpokenWords or "Microsoft mail" in SpokenWords:
            playsound("Voice/StartOutlook.mp3");
            webbrowser.open_new("https://login.live.com/"); sleep(0.8);
            playsound("Voice/Suggestions/MailLogInConfirmation.mp3");
            j.actionListener();
            if "authorization" in SpokenWords or "authorisation" in SpokenWords or "566" in SpokenWords:
                playsound("Voice/Suggestions/LogginInMail.mp3");
                OpenCredentials = open('Memory/Others/Details/LiveMail.txt', 'r');
                with OpenCredentials as csv_file:
                    csv_reader = csv.DictReader(csv_file);
                    iteration = 0;  username = "";  password = "";
                    for row in csv_reader:
                        username = row['user'];password = row['pass'];iteration += 1;
                    OpenCredentials.close();
                keyboard.type(username);
                keyboard.press(Key.enter);keyboard.release(Key.enter); sleep(1.4);
                keyboard.type(password);keyboard.press(Key.enter); keyboard.release(Key.enter);
            else:
                playsound("Voice/Suggestions/CantAccess.mp3");
                keyboard.press(Key.ctrl);
                keyboard.press('w');keyboard.release('w');
                keyboard.release(Key.ctrl);
        elif "Amazon" in SpokenWords or "amazon" in SpokenWords:
            playsound("Voice/StartAmZ.mp3")
            webbrowser.open_new("https://www.amazon.com/");
        elif "instagram" in SpokenWords or "Instagram" in SpokenWords:
            playsound("Voice/StartInsT.mp3");
            webbrowser.open_new("https://www.instagram.com/");
        else :
            j.AI_Ok();
            os.system('explorer E:\\"{}"'.format(SpokenWords.replace('open ', '').replace('launch ', '')));

    def programClose(self):
        if "tab" in SpokenWords or "app" in SpokenWords:
            FileType="Close"; FileExtension=".mp3"
            from random import randint; number = str(randint(1, 6));
            FilePath=FileType+number+FileExtension;
            playsound("Voice/"+FilePath);
            keyboard.press(Key.ctrl); keyboard.press('w');
            keyboard.release('w'); keyboard.release(Key.ctrl);
        elif "window" in SpokenWords or "Window" in SpokenWords or "folder" in SpokenWords or "file" in SpokenWords:
            FileType = "Close"; FileExtension = ".mp3"
            from random import randint; number = str(randint(1, 6));
            FilePath = FileType + number + FileExtension;
            playsound("Voice/" + FilePath);
            keyboard.press(Key.alt);keyboard.press(Key.f4);
            keyboard.release(Key.f4); keyboard.release(Key.alt);

    def programMinimize(self):
        keyboard.press(Key.alt); keyboard.press(Key.space); keyboard.press("n");
        keyboard.release(Key.alt); keyboard.release(Key.space); keyboard.release("n");
        sleep(0.3);
    def programRestoreWindow(self):
        keyboard.press(Key.alt); keyboard.press(Key.tab);
        keyboard.release(Key.alt); keyboard.release(Key.tab);
        sleep(0.3);
    def programViewAllRunningApp(self):
        j.AI_Ok();
        mouse.position = (416, 1058);
        sleep(0.3);
        mouse.press(Button.left); mouse.release(Button.left);
    def who_what_how_when(self):
        if "current" in SpokenWords and "time" in SpokenWords and "what" in SpokenWords:
            j.CurrentTimeIs();
        elif "now" in SpokenWords and "time" in SpokenWords and "what" in SpokenWords:
            j.getCurrentTime();
        elif "current" in SpokenWords and "weather" in SpokenWords and "what" in SpokenWords:
            j.CurrentWeatherIs();
        elif "current" in SpokenWords and "weather" in SpokenWords and "how" in SpokenWords:
            j.CurrentWeatherIs();
        elif "now" in SpokenWords and "weather" in SpokenWords and "how" in SpokenWords:
            j.CurrentWeatherIs();
        elif "current day" in SpokenWords or "what day is today" in SpokenWords or "current date" in SpokenWords:
            j.CurrentDateIs();
        elif "your mind" in SpokenWords:
            j.AI_Quotes();
        else :
            webbrowser.open_new("https://www.google.com/search?q={}".format(SpokenWords));
    def programLogout(self):
        if "facebook" in SpokenWords or "Facebook" in SpokenWords:
            j.AI_Ok();
            keyboard.press(Key.shift); keyboard.press(Key.tab); sleep(0.5);
            keyboard.release(Key.shift); keyboard.release(Key.tab); sleep(0.5);
            keyboard.press(Key.down); keyboard.release(Key.down); sleep(1.1);
            keyboard.press(Key.up); keyboard.release(Key.up);sleep(0.5);
            keyboard.press(Key.enter); keyboard.release(Key.enter); sleep(0.3);
        elif "twitter" in SpokenWords or "Twitter" in SpokenWords:
            j.AI_Ok();
            mouse.position = (1436, 91);  mouse.press(Button.left); mouse.release(Button.left); sleep(1);
            mouse.position = (1303, 515); mouse.press(Button.left); mouse.release(Button.left); sleep(0.3);
        elif "gmail" in SpokenWords or "Gmail" in SpokenWords:
            j.AI_Ok();
            mouse.position = (1888, 104); mouse.press(Button.left); mouse.release(Button.left); sleep(1);
            mouse.position = (1857, 298); mouse.press(Button.left); mouse.release(Button.left); sleep(0.8);
        ## "REMINDER" YAHOO LOGUT STILL NEEDED
        elif "microsoft mail" in SpokenWords or "live mail" in SpokenWords or "live account" in SpokenWords \
                or "microsoft account" in SpokenWords or "outlook mail" in SpokenWords:
            j.AI_Ok();
            mouse.position = (1886, 95); mouse.press(Button.left); mouse.release(Button.left); sleep(1);
            mouse.position = (1752, 299); mouse.press(Button.left); mouse.release(Button.left); sleep(0.8);

    def AI_Quotes(self):
        randNum = str(randint(1, 5));
        filePath = "Voice/Quotes/";
        fileType = "Quote";
        extensions = ".mp3"
        playsound(filePath + fileType + randNum + extensions);
    def commentOrCompliment(self):
        if "good work" in SpokenWords or "good job" in SpokenWords or "good idea" in SpokenWords:
            from random import randint;
            number = randint(0, 2);
            if number == 0:
                playsound("Voice/ThankU1.mp3");
            elif number == 1:
                playsound("Voice/ThankU2.mp3");
            elif number == 2:
                playsound("Voice/ThankU3.mp3");
        else:
            from random import randint
            number = randint(0, 3);
            if number == 0:
                playsound("Voice/Hmm1.mp3");
            elif number == 1:
                playsound("Voice/Hmm2.mp3");
            elif number == 2:
                playsound("Voice/Hmm3.mp3");
            elif number == 3:
                playsound("Voice/Hmm2.mp3");
    def randomTalks(self):
        if "need to update you" in SpokenWords or "need to modify you" in SpokenWords \
                or "you need more updates" in SpokenWords or "you could use some updates" in SpokenWords:
            playsound("Voice/Suggestions/SuggestCreateBackup.mp3");

    def AI_Ok(self):
        randNum = str(randint(1, 9));
        filePath = "Voice/";
        fileType = "ok";
        extensions = ".mp3"
        playsound(filePath + fileType + randNum + extensions); #playsound("Voice/Testing/AITestSuccessful.mp3");


    def exceptionHandler(self):
        with open("memory/logs/logs_report.txt", mode="a") as csv_file:
            csv_file.write("\n"+"*"+str(j.getCurrentTime())+"\n");
            csv_file.write(str(e));
        if "cannot find" and "file" in str(e):
            playsound("Voice/CatchErrorCause1.mp3");
        elif "can only concatenate" in str(e):
            playsound("Voice/CatchErrorCause2.mp3");
        elif "is not defined" in str(e):
            playsound("Voice/CatchErrorCause3.mp3");
        elif "as left operand" in str(e) or "requires string as left operand" in str(e):
            playsound("Voice/CatchErrorCause4.mp3");
        elif "No Default Input Device Available"  in SpokenWords or "Unanticipated host error" in SpokenWords or "Stream closed" in SpokenWords:
            playsound("Voice/CatchErrorCause5.mp3");

    def actionListener(self):
        global Unrecognized;
        global SpokenWords;
        SpokenWords = "";
        playsound("Voice/BgSound/ClickSound.mp3");
        with sr.Microphone() as source:
            audio = r.listen(source=source, phrase_time_limit=4);
            try:
                text = r.recognize_google(audio, language="en-US");
                #r.list
                SpokenWords = format(text);
                SpokenWords=SpokenWords.lower();
                print("You said : {}".format(text));
                Unrecognized = 1;
            except:
                print("Sorry could not recognize what you said");
                Unrecognized = 0;

Polarity=0;
j=January(); system("title "+"January");
j.januaryActivated();
#SpokenWords ="wait for my command ";
#SpokenWords=SpokenWords.lower();
#playsound("Voice/Welcome.mp3"); j.CurrentTimeIs();
# playsound("Voice/Testing/AITestSuccessful.mp3");              #_test_purpose_Only!!!!!!!!!!!!!
while True:
    try:
        j.actionListener();
        if "hi " in SpokenWords or "hello" in SpokenWords or "hey" in SpokenWords:
            j.replyGreet();
        elif "who are you" in SpokenWords or "introduce yourself" in SpokenWords or "what's your name" in SpokenWords or "what are you" in SpokenWords:
            j.replyIntro();
        elif "how are you" in SpokenWords or "your status" in SpokenWords or "you alright" in SpokenWords:
            j.replyStatus();
        elif "feeling" in SpokenWords or "I feel" in SpokenWords or "I don't feel" in SpokenWords:
            j.feeling();
        elif "welcome" in SpokenWords:
            sleep(3);
        elif "thank you" in SpokenWords or "thanks" in SpokenWords:
            j.replythanks();
        elif "sorry" in SpokenWords:
            j.replysorry();
        elif "you there" in SpokenWords:
            j.replypresence();
        elif "goodbye " in SpokenWords or "goodbye" in SpokenWords or "goodbye january" in SpokenWords or "by january" in SpokenWords \
                or "bye" in SpokenWords or "bye january" in SpokenWords or "shutdown" in SpokenWords:
            j.farewell();
        elif "wait" in SpokenWords or "hang on" in SpokenWords:
            j.wait();
        elif "activate folder mode" in SpokenWords or "activate folder made" in SpokenWords:
            j.folderMode();
        elif "open" in SpokenWords or "launch" in SpokenWords:
            j.programLauncher()
        elif "close" in SpokenWords:
            j.programClose();
        elif "minimise" in SpokenWords or "minimize" in SpokenWords:
            j.programMinimize();
        elif "maximise" in SpokenWords and "window" in SpokenWords or "maximize" in SpokenWords and "window" in SpokenWords\
                or "restore" in SpokenWords and "window" in SpokenWords:
            j.programRestoreWindow();
        elif "view all" in SpokenWords and "windows" in SpokenWords or "view all" in SpokenWords and "programs" in SpokenWords\
                or "show all" in SpokenWords and "applications" in SpokenWords:
            j.programViewAllRunningApp();
        elif "who" in SpokenWords or "what" in SpokenWords or "why" in SpokenWords or "when" in SpokenWords or "how" in SpokenWords:
            j.who_what_how_when();
        elif "logout" in SpokenWords or "Logout" in SpokenWords or "lock out" in SpokenWords:
            j.programLogout();
        elif Unrecognized==1:
            if "good" in SpokenWords:
                j.commentOrCompliment();
            elif "january" in SpokenWords:
                j.replypresence();
            else:
                playsound("Voice/Error1.mp3");


    except Exception as e:
        playsound("Voice/CatchError.mp3");
        j.exceptionHandler();
        playsound("Voice/CatchErrorOperational.mp3");

sleep(5);
