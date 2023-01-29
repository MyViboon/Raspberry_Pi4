import random

def Hello():
    print('Hello world')

# Hello()
    
def random_tamperatuer():
    t = random.uniform(25,39)
    t = round(t,2)
    return t

def random_humidity():
    h = random.uniform(40,90)
    h = round(h,2)
    return h

def random_minx():
    t = random.uniform(25,39)
    t = round(t,2)
    h = random.uniform(40,90)
    h = round(h,2)
    return (t,h)

def random_minx_dict():
    t = random.uniform(25,39)
    t = round(t,2)
    h = random.uniform(40,90)
    h = round(h,2)
    return {"temperature": t, "humidity": h}

def check_temperature():
    # temp = random_tamperatuer()
    # humid = random_humidity()
    # temp, humid = random_minx()
    data = random_minx_dict()
    temp = data["temperature"]
    humid = data["humidity"]
    print('Temperature: {}'.format(temp))
    print('Humidity: {}'.format(humid))


check_temperature()