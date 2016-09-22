class Employee():
    count = 0

    def __init__(self, name, language):
        self.name = name
        self.language = language

        self.__class__.count += 1

if __name__ == '__main__':
    john = Employee("John Doe", "English")
    jane = Employee("Jane Doe", "Korean")
    print("We have {} employees.".format(Employee.count))
