class Employee():
    instances = []

    def __init__(self, name="", language=""):
        self.name = name
        self.language = language

        self.instances.append(self)

    @classmethod
    def count(cls):
        return len(cls.instances)

if __name__ == '__main__':
    john = Employee("John Doe", "English")
    print(vars(john))
    jane = Employee("Jane Doe", "Korean")
    print("We have {} employees.".format(Employee.count()))
    print("Employees:")
    for item in Employee.instances:
        print("    {name}".format(**vars(item)))
