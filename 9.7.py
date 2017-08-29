#Write class called 'Admin' that inherits the User class.
#Add an attribute, 'privileges', that stores a list of strngs.
#Write a method called 'show_priveleges()' that lists the
#admin's set of privileges.
#Create an instance and call method.

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

class Admin(User):
    def __init__(self, first_name, last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = ['adding posts','deleting posts','banning users']

    def show_privileges(self):
        print(self.first_name.title(), self.last_name.title(), 'is an administrator whose privileges include:')
        for i in range(len(self.privileges)):
            if self.privileges[i] == self.privileges[len(self.privileges) - 1]:
                print('and', self.privileges[i] + '.')
            else: print(self.privileges[i] + ',')

myself = Admin('octavio', 'sosa', '23', 'cis-male-trans')
myself.describe_user()
myself.show_privileges()
