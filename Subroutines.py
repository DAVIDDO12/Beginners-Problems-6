def triangleTest(side1,side2,side3):
    triangle = side1 < side2 < side3
    if triangle and side1 + side2 > side3:
        return True
    else:
        return False

name = input("What's your name:")
morning = int(input("What's the time(24 hour time)"))
def time1(morning):
    if morning < 1200:
        print("Good morning", name)
        return True
    else:
        return False
time1(morning)
afternoon = int(input("What's the time(24 hour time)"))
def time2(afternoon):
    if afternoon < 1700:
        print("Good afternoon", name)
        return True
    else:
        return False
time2(afternoon)
evening = int(input("What's the time(24 hour time)"))
def time3(evening):
    if evening < 2300:
        print("Good evening", name)
        return True
    else:
        return False
time3(evening)

def getEven(integerList):
    evennumbers = []
    for integer in integerList:
        if integer % 2 == 0:
            evennumbers.append(integer)
    return evennumbers
print("Enter integers (type done when finished):")
integerList = []
while True:
    numbers = input()
    if numbers.lower() == "done":
        break
    else:
        integerList.append(int(numbers))
evens = getEven(integerList)
print("The even numbers are:", evens)
