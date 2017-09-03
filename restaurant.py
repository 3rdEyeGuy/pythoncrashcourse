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
        print(self.restaurant_name.title(), 'is a', self.cuisine_type,
              'restaurant.')

    def open_restaurant(self):
        print(self.restaurant_name.title(), 'is now open!')
