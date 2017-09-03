class User():
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts += 1
        print('login attempts:',self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('login reset')
        print('login attempts:',self.login_attempts)

    def describe_user(self):
        print(self.first_name.title(),self.last_name.title(), 'is a',
              self.age.title(),'year old',self.gender, 'pothead.')

    def greet_user(self):
        print('Hello',self.first_name.title() + '!')

class Privileges():
    def __init__(self):
        self.privileges = ['adding posts','deleting posts','banning users']

    def show_privileges(self):
        print('An administrator\'s privileges include:')
        for i in range(len(self.privileges)):
            if self.privileges[i] == self.privileges[len(self.privileges) - 1]:
                print('and', self.privileges[i] + '.')
            else: print(self.privileges[i] + ',')

class Admin(User):
    def __init__(self, first_name, last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.myprivileges = Privileges()
        print(self.first_name.title(), self.last_name.title(), 'is an Admin.')
