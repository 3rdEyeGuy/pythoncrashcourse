#Class for Restaurant. __init__() method should have attributes: 
#restaurant_name and cuisine_type.
#Write a class called IceCreamStand that inherits from the Restaurant class.
#Add an atribute called Flavors that stores a list of ice cream flavors.
#Write a method displaying the flavors. Create an instance of IceCreamStand
#Call method.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def read_number_served(self):
        print('Customers served:',self.number_served)
        
    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,new_customers):
        self.number_served += new_customers

    def describe_restaurant(self):
        print(self.restaurant_name.title(), 'is a', self.cuisine_type.title(),
              'restaurant.')

    def open_restaurant(self):
        print(self.restaurant_name.title(), 'is now open!')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry']

    def disp_flavors(self):
        print('Our flavors include:')
        for i in range(len(self.flavors)):
            if self.flavors[i] == self.flavors[len(self.flavors) - 1]:
                print('and', self.flavors[i] + '.')
            else: print(self.flavors[i] + ', ')

toritoCreams = IceCreamStand('El_Torito_Nieveria','Mexican_Ice_Cream')
toritoCreams.describe_restaurant()
toritoCreams.open_restaurant()
toritoCreams.disp_flavors()

