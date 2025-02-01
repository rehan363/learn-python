class Car:
 def __init__(self, make, model, year):
 #"""Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

 def get_descriptive_name(self):
      details =(f"Car model is {self.model}. Car make is {self.make}. Car colour is {self.year}")
      return details.title()
    

 def read_odometer(self):
    #"""Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")
   
 def update_odometer(self,mileage):
   if mileage >= self.odometer_reading :
      self.odometer_reading = mileage
   else:
      print("meter cant be rolled back..")
    
class Electric_car(Car):
    def __init__ (self , make , model , year):
        super().__init__(make,model,year)
        self.battery_size = 2
    
    def battery_size(self):
        print(f"batter size of my car is {self.battery_size}")

my_new_car = Car("audi" , "a2" ,2022)
