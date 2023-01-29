import random
import csv
import Adafruit_DHT
import time
from datetime import datetime

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
            
            
            
temp1 = Sensor('DHT22-101')

for i in range(30):
    temp1.show_result(True)
    time.sleep(2)
    print("------------------")