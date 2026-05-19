# listOfNames = []
# numbers = 3.

# # while numbers > 0 :
# # while numbers < 3 :
# # while len(listOfNames) < 3 :
# #     inputValue =input("Enter a Name: ")
# #     listOfNames.append(inputValue)
# #     numbers = numbers -1
# #     print(listOfNames, numbers)
# # print(listOfNames)


# for i in range(3):
#     # print("james")
#     ourValue = input("Enter your name: ")
#     listOfNames.append(ourValue)


# listOfNames.sort(key=len)
# print(listOfNames)

# # while x >= 9:
# #     print("BLOCK OF CODE")


# creatingList = []

# numberOfEntries = 4

# for i in range(4):
#     ourVlaue = input("Enter your name: ")
#     creatingList.append(ourVlaue)

# print(creatingList)


# practically= []

# numberOfEntires = 5

# for i in range(5):
#     ourValue= input("Enter your name: ")
#     practically.append(ourValue)

# practically.sort(key=len)
# print(practically)


# examList = []

# numbers =5

# for i in range(5):
#     ourValue= input("Enter your name: ")
#     examList.append(ourValue)

# examList.sort(key=len)
# print(examList)


# forList = []

# numbers = 5

# for i in range(5):
#     ourValue= input("Enter your nama: ")
#     forList.append(ourValue)

# forList.sort(key=len)
# print(forList)


emptyfOOD = []

numbersOfFood = 3

for i in range (3):
    ourValue = input("Enter full name: ")
    emptyfOOD.append


    # class Human:
#     def _init_(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def greet(self):
#         print(f"Good day {self.name}, so good to have you!")

#     def detail(self):
#         print(f"Good day Mr{"s" if self.gender == "female".lower() else ""}. {self.name}, so good to have you, your selected gender is {self.gender} and you are {self.age} years old!")

# human = Human("Helen", "female", 12)
# human1 = Human("Daniel", "Male", 17)


# # OOP

# class Married(Human):
#     def _init_(self,name, gender, age, status):
#         super()._init_(name, gender, age)
#         self.status = status

#     def readStatus(self):
#         print(f"{self.status}")

# human2 = Married("Emma", "Male", 12, "single")

# human2.detail()

# # class Married(Human):
# #     def _init_(self, name, gender, age, status):
# #         super()._init_(name, gender, age)
# #         self.status = status

# #     def readStatus(self):
# #         print(f"{self.}")



# # human.detail()
# # print()
# # hum

class Humans:
    def _init_(self, __name, age, height, gender):
        self.age = age
        self.height = height
        self.gender = gender
        self.__name = __name

    def __readName(self):
        print(f"{self.name}")

class Vote(Humans):
    def _init_(self,name, age, height, gender, pvc):
        super()._init_(name, age, height, gender)
        self.pvc = pvc


    def readNameNow(self):
        print(f"{self.name}")

    def VoteElligibility(self):
        if self.age >= 18:
            print(f"Qualified to Vote")
        else:
            print(f"Not elligible")


human1 = Vote("Petr",17, 7.5, "male", True)
human1.VoteElligibility()
human1.readNameNow()