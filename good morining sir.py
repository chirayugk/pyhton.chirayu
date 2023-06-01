import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
gante=int(time.strftime("%H")) 
print(gante)
if(gante>=6 and gante<11):
    print("good morinig sir")
elif(gante>=11 and gante<13):
    print("good afternoon sir")    
elif(gante>13 and gante<=20):
    print("GOOD EVENING SIR")
else:
    print("good night sir ")        