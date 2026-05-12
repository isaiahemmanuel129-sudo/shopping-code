# string
# number
# list
# dictionary

# {} []

myList = [6,7,2, "str", "Peter", [4,6,8]] # #4
# newList = myList[5]
# retep

# print(f"{myList[5][0]}")
print(f"this is the {max(myList[5])}")
# print(newList[0])

# name = "Blessing"
# print(name[::-1])

name = (myList[4])
# print(name.split(""))

nameHolder = []
for i in name:
    (nameHolder.append(i))

(nameHolder.reverse())
print("".join(nameHolder).lower())

myNewList = [6,7,2, "str", "Godswill", [4,6,8]] 

newName = myNewList[4]
# newName = myNewList[4:5]

newList = []
for i in newName:
    (newList.append(i))

(newList.reverse())
print("".join(newList))

x = ["3","5","7"]
print("".join(x))

newNumber = 473 #374
# convert to str == int("5")
convertToString = str(newNumber)

freshList = []
for i in convertToString:
    freshList.append(i)

(freshList.reverse())
print(int("".join(freshList)))

dict = {"name": "Peter", "status": True, "score": 57}

# print(dict["status"])

studentData = [
    {"name": "Peter", "status": True, "score": 27},
    {"name": "Blessing", "status": True, "score": 59},
    {"name": "Richard", "status": True, "score": 45},
    {"name": "Jessica", "status": True, "score": 73},
]
print("")
data = ["Peter", "Blessing", "Richard", "Jessica"]
# print(max(data))
# print(max(studentData))

result = []
for i in studentData:
    result.append(i["score"])

# print(max(result))

highestScore = studentData[0]

print(highestScore["score"])
print(f"this is where we started from: {highestScore}")
for i in studentData:
    # print(i["score"])
    if i["score"] > highestScore["score"]:
        highestScore = i

print(highestScore)

print(f"The person with the highest score is '{highestScore["name"]}', with the score of {highestScore['score']}")

print("")
print("")
print("")

def division():
    try: 
        inputValue = int(input("Enter the value: "))
        7/inputValue
        raise ValueError("Please enter a Number")
    
    except:
        print("")

print(division())

try:
    raise ValueError("Your value should be a Number")
except ValueError as e:
    print(e)