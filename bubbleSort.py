#bubble sort
from random import choice

def init(n):
    numbers = []
    for x in range(100 + 1):
        numbers.append(x)

    random = []

    for x in range(n):
        random.append(choice(numbers))
    
    return random

#bubble sort algorithm
def Bubble(NumList):
    length =  len(NumList)
    while True:
        correct = 0
        for x in range(length - 1):
            if(NumList[x] > NumList[x+1]):
                temp1, temp2 = NumList[x], NumList[x+1]
                NumList[x], NumList[x+1] = temp2, temp1
        for x in range(length - 1):
            if(NumList[x] <= NumList[x+1]):
                correct += 1
        
        if(correct+1 == length):
            return NumList



n = int(input("amount of numbers: "))

ToSort = init(n) # init x numbers from 0 to 100

print("\nUnsorted:", ToSort)
print("Sorted:", Bubble(ToSort))