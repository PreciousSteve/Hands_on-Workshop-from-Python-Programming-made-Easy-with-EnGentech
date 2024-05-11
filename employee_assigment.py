# Assignments
# 1.
# Define a class Employee representing employees in a company. Implement methods to calculate salary and provide a string representation of the employee.
# 2.
# Create a subclass Manager inheriting from Employee. Implement additional functionality specific to managers, such as bonus calculation.
class Employee:
    def __init__(self, employee_name, base_salary, benefit_percentage):
        self.employee_name = employee_name
        self.base_salary = base_salary
        self.benefit_percentage = benefit_percentage

    def salary(self):
        benefits = (self.base_salary * self.benefit_percentage) / 100
        return self.base_salary + benefits

    def __str__(self):
        return f"{self.employee_name} has a salary of ${self.salary()}"


# creating object with the class
employee1 = Employee("Mathew", 20000, 10)

print(employee1.salary())
print(employee1)


class Manager(Employee):
    def __init__(self, employee_name, base_salary, benefit_percentage, position):
        super().__init__(employee_name, base_salary, benefit_percentage)
        self.position = position

    def manager_salary(self):
        bonus = 0.10 * self.base_salary
        return self.salary() + bonus

    def __str__(self):
        return f"{self.employee_name} the {self.position} has a salary of ${self.manager_salary()}"


manager1 = Manager("Gerald", 20000, 10, "Manager")

print(manager1.manager_salary())
print(manager1)

