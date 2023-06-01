print("welcome to kaun banega crorepati")
print("who is the prime minister of India")
list1=["modi","rahul gandhi","kejriuddin","siddramullah khan"]
print(list1)
x=input("enter the correct answer:")
match x:
    case "modi":
        print("you get 1000 rs and move to next question")
    case "rahul gandhi":
        print("nikal laude")
    case "kejriuddin":
        print("nikal laude")    
    case "siddramullah khan":
        print("nikal laude")
print("software capital of India")
list2=["Bengaluru","mumbai","bangalore","delhi"]
print(list2)
y=input("enter the correct answer:")
match y:
    case "Bengaluru":
        print("you get 1000+1000 rs and move to next question")
    case "mumbai":
        print("sorry you get only 1000 rs and nikal laude")
    case "bangalore":
        print("nikal laude first kannada kali laude")    
    case "delhi":
        print("sorry you get only 1000 rs and nikal laude")       