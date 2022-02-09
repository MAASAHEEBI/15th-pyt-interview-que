#15)
def swapList():
 newList=[12, 35, 9, 56, 24]
 size = len(newList) 

# Swapping

 newList[0] , newList[size-1] =newList[size-1],newList[0]
 return newList 
print(swapList()) 
