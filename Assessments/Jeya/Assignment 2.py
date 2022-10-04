import random
def tempMonitor():
    min_temp=15
    max_temp=25
    min_hum=30
    max_hum=50
    temp = random.randint(14,26)
    humidity=random.randint(29,51)
    if((temp>=min_temp)and(temp<=max_temp)and(humidity>=min_hum)and(humidity<=max_hum)):
        print("Temperature and Humidity is optimum")
        tempMonitor()
    else:
        if(temp<min_temp):
            print("Temperature is too Cod:"+str(temp))
        if(humidity<min_hum):
            print("Humidity is too Low:"+str(humidity))
        if(temp>max_temp):
            print("ALERT: Temperature is too High:"+str(temp))
        if(humidity>max_hum):
            print("Humidity is too High:"+str(humidity))
    return
