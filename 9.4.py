#Class for Restaurant. __init__() method should have attributes: 
#restaurant_name and cuisine_type.

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
              'restaurant with in house butchers to customize your cuts.')

    def open_restaurant(self):
        print(self.restaurant_name.title(), 'is now open!')

myFamilyRestaurant = Restaurant('El_Torito','mexican_as_fuck')
myFamilyRestaurant.describe_restaurant()
myFamilyRestaurant.open_restaurant()

restaurant = Restaurant('Kin-Lin','ching-chong_chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_number_served()
restaurant.set_number_served(69)
restaurant.read_number_served()
restaurant.increment_number_served(3)
restaurant.read_number_served()

