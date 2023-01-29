import time
import threading

def Shower():
    for i in range(10):
        print("กำลังอาบน้ำ", i)
        time.sleep(0.5)

def Toothbrust():
    for i in range(10):
        print("แปรงฟัน", i)
        time.sleep(0.2)

task1 = threading.Thread(target=Toothbrust)
task2 = threading.Thread(target=Shower)

t1 = time.time()
task1.start()
task2.start()

task1.join()
task2.join()
# Toothbrust()
# Shower()
t2 = time.time()
print("Time",t2 - t1)