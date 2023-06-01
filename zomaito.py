fp=int(input("enter food price:"))
budget=1000
if(fp<=budget):
    print("alexa,ordering the food")
else:
    print("alexa,not ordering the food")    
# nested ifelse
num=20
if(num<0):
    print("number is negetive")
else:
    if(num<=10):
        print("number is single digit positive")
    else:
        print("number is positive double digit")            