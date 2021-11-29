class Instructors:
    companyName = "Bluelime"

    def __init__(self, course, duration):
        self.course = course
        self.duration = duration

    def printInfo(self):
        print("My Company name is ", self.companyName)


eLearning = Instructors("Python for beginners ..!", 7)
bls = Instructors("Django for beginners ..!", 8)
bls.course = "HTML"

bls.printInfo()
print(bls.course)
del bls.duration
print(bls.duration)
