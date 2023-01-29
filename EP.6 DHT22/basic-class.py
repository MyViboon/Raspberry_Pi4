import random
import csv

def writeTocsv(data, filename='data'): # save ตามชื่อที่ใส่ใน filename
    with open('{}.csv'.format(filename),'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

class Sensor:
    """ Sensor Class for Iot"""
    def __init__(self, name='DF-101'):
        self.name = name
        self.type = 'DHT22'
    
    def get_temp_humid(self):
        t = random.uniform(25,39)
        t = round(t,2)
        h = random.uniform(40,90)
        h = round(h,2)
        return (t,h)
    
    def show_result(self,writecsv=False):
        temp, humid = self.get_temp_humid()
        print('Temperture: {:.2f}°C\nHumidity: {:.2f}%'.format(temp,humid))
        if writecsv == True:
            data = [temp, humid]
            writeTocsv(data,self.name)

sensor1 = Sensor('A-101')
sensor1.show_result(True)

sensor2 = Sensor('B-101')
sensor2.show_result(True)

sensor3 = Sensor('C-101')
sensor3.show_result(True)

# temp, humid = sensor1.get_temp_humid()
# print(temp,humid)
