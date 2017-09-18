class Employee():
    """Stores first and last names as well as the salary"""

    def __init__(self, first, last, salary):
        """initializes first, last and salary"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, salRaise = 5000):
        """default raise of $5000 but can be customized"""
        self.salary = self.salary + salRaise
