class Human:
    def work(self):
        pass

class Teacher(Human):
    def work(self):
        print("I love teaching")

class Driver(Human):
    def work(self):
        print("I love driving")

teacher = Teacher()
driver = Driver()

humans = [teacher, driver]
for human in humans:
    human.work()

