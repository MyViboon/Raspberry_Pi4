from tkinter import *

GUI = Tk()
GUI.title("Temperature Monining")
GUI.geometry("500x500")

FONT1 = (None, 40)
FONT2 = (None, 60, "bold")

L = Label(GUI, text="Temperature", font=FONT1)
L.pack()

#Temparature
v_temparature = StringVar()
v_temparature.set("XX.YY°C")

L = Label(GUI, textvariable= v_temparature, font=FONT2,fg="blue")
L.pack()

temperature = 20

def AddTemp():
    global temperature
    temperature += 1
    print(temperature)
    v_temparature.set("{:.2f}°C".format(temperature))

B = Button(GUI, text="Update", command=AddTemp)
B.pack()

GUI.mainloop()