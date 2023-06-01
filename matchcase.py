# x is variable to get matched
x=int(input("enter a number"))
match x:
    case 0:
        print("x is zero")
    case 10:
        print("x is ten ")
    case 100:
        print('x is hunderd')
    case _:
        print("chutiya")
            