class Person:
    def __init__(self, name, age):  # self means = current instance of an object
        self.name = name            # Employee.name
        self.age = age              # Employee.age

    def displayinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employeeid):
        super().__init__(name, age)
        self.employeeid = employeeid

    def displayinfo(self):
        super().displayinfo()
        print(f"em id: {self.employeeid}")

class Manager(Employee):
    def __init__(self, name, age, employeeid, department):
        super().__init__(name, age, employeeid)
        self.department = department

    def displayinfo(self):
        super().displayinfo()
        print(f"Department: {self.department}")

employee = Employee("kok", 23, 4444)
employee.displayinfo()

manager = Manager("khan", 22, 2222, 3)
manager.displayinfo()

# isinstance testing
result = isinstance(manager, Person)
print(result)
