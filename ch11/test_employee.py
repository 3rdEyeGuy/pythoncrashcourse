import unittest

from employee_info import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests default raise of salary and customized raise"""
    def setUp(self):
        """create instance of an employee"""
        employeeInfo = Employee('octavio', 'sosa', 100000)

    def test_give_default_raise(self):
        self.employeeInfo.give_raise()
        self.assertIn(105000, self.employeeInfo.salary)

    def test_give_custom_raise(self):
        self.employeeInfo.give_raise(25000)
        self.assertIn(125000, self.employeeInfo.salary)

unittest.main()
        
