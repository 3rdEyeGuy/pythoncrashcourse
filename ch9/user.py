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
