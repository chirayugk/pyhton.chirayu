countris=("india","bharat","hindustan")
temp=list(countris)
temp.append("aryavarta")    #add item
temp.pop(2)          #remove item
temp[1]="bharatvarsha"  #change item
countris=tuple(temp)
print(countris)
# we can concatanate  tuples by + forming new tuple