class Car:
    
    '''This function creates an instance of class Cars
        :param name: Is the name of the vehicle brand
        :param cylinders: Is the integer number representing the number cilendars
    '''
    def __init__(self):
        self.name : str = input("Enter the brand name: ")
        self.cylinders : int = self.get_number()


    def get_number(self) -> int:
        cylinders = input(f"Enter the number of cylinders for this {self.name} car: ")
        while not cylinders.isnumeric():
            cylinders = input("You must enter a number only for the cylinders: ")
        return int(cylinders)

    def printCarDetails(self):
        print(f"This car is {self.name} brand, and has {self.cylinders} cylinders.")

if __name__ == "__main__":
    car01 = Car()
    car01.printCarDetails()

