#Class for Restaurant. __init__() method should have attributes: 
#restaurant_name and cuisine_type.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title(), 'is a', self.cuisine_type.title())
        print('restaurant with in house butchers to customize your cuts')

    def open_restaurant(self):
        print(self.restaurant_name.title(), 'is now open!')

myFamilyRestaurant = Restaurant('El_Torito','mexican_as_fuck')
myFamilyRestaurant.describe_restaurant()
myFamilyRestaurant.open_restaurant()
