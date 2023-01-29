from tkinter import *

##################### Temperature ##############################

import random
import csv
import Adafruit_DHT
import time
from datetime import datetime
import threading

def writeTocsv(data, filename='data'): # save ตามชื่อที่ใส่ใน filename
    with open('{}.csv'.format(filename),'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

class Sensor:
    """ Sensor Class for Iot"""
    def __init__(self, name='DF-101'):
        self.name = name
        self.type = 'DHT22'
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 2
    
    def get_temp_humid(self):
        h, t = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        return (round(t,2),round(h,2))
    
    def show_result(self,writecsv=False):
        temp, humid = self.get_temp_humid()
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        text = " | ผลลัพท์ที่ได้ | "
        print(current_date_time)
        print('Temperture: {:.2f}°C\nHumidity: {:.2f}%'.format(temp,humid))
        
        if writecsv == True:
            data = [current_date_time,text,temp, humid]
            writeTocsv(data,self.name)

#########################################################################

GUI = Tk()
GUI.title("Temperature Monining")
GUI.geometry("500x500")
GUI.attributes("-fullscreen", True)

GUI.bind("<F1>",lambda x: GUI.attributes("-fullscreen", False))
GUI.bind("<F2>",lambda x: GUI.attributes("-fullscreen", True))

FONT1 = (None, 40)
FONT2 = (None, 80, "bold")

L = Label(GUI, text="Temperature", font=FONT1)
L.pack(pady=40)

#Temparature
v_temparature = StringVar()
v_temparature.set("XX.YY°C")

L = Label(GUI, textvariable= v_temparature, font=FONT2,fg="blue")
L.pack(pady=30)

temperature = 20

def AddTemp():
    global temperature
    temperature += 1
    #print(temperature)
    v_temparature.set("{:.2f} °C".format(temperature))

def UpdateTemp():
    global temperature
    sensor = Sensor()
    t,h = sensor.get_temp_humid()
    temperature = t
    v_temparature.set("{:.2f}°C".format(temperature))
    #print("updated")

def RunUpdateTemp():
    while True:
        try:
            UpdateTemp()
        except:
            v_temparature.set("ERROR")
        time.sleep(10)

B = Button(GUI, text="Update", command=UpdateTemp)
B.pack()

task = threading.Thread(target=RunUpdateTemp)
task.start()


GUI.mainloop()
