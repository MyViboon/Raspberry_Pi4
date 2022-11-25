import csv

def writeTocsv(data):
    # data = [25.55,50.55]
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

writeTocsv([20,55])