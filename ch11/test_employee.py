import unittest

from employee_info import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests default raise of salary and customized raise"""
    def setUp(self):
        """create instance of an employee"""
        self.employeeInfo = Employee('octavio', 'sosa', 100000)

    def test_give_default_raise(self):
        """test default raise"""
        self.employeeInfo.give_raise()
        self.assertIn(str(105000), str(self.employeeInfo.salary))

    def test_give_custom_raise(self):
        """test custom raise"""
        self.employeeInfo.give_raise(25000)
        self.assertIn(str(125000), str(self.employeeInfo.salary))

unittest.main()
        
