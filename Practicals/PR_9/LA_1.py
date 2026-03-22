class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def show_data(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass


# process 10 managers
for i in range(1, 11):
    print("\nEnter details of Manager", i)
    m = Manager()
    m.get_data()
    m.show_data()