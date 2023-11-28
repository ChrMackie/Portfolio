# define a class named 'car'
class car:
    #constructor method to initialize attributes
    def __init__(self, make, model, year):
        self.make = make #attribute
        self.model = model #attribute
        self.year = year #attribute

    # method to get car information
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    #method to start the car
    def_
