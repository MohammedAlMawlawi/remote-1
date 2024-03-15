'''This is a car class
'''
class car:
    _engine_types: dict = {1 : 'Petrol Engine',
                           2 : 'Hybrid Engine',
                           3 : 'Electric Motor',
                           4 : 'Deseil Engine',
                           5 : 'Liquid Gas Engine'
                           }

    def __init__(self):
        self._brand = self.set_brand()
        self._engine_type = self._engine_types[self.set_engine_type()]

    '''This function returns a str representing the brand name of the car
    '''
    def set_brand(self) -> str:
        brand = input("Enter the brand name of this car: ")
        while not brand.isalpha():
            brand = input("You must input the brand name as string without numbers")
        return brand

    '''This function returns a number that represents the type of engine
    '''
    def set_engine_type(self) -> int:
        engine_selections = [f'For {value} = {key}' for key,value in self._engine_types.items()]
        msg = "Select the number representing type of engine:\n"
        for i in engine_selections:
            print(i)
        engine_type = input(msg)
        while not engine_type.isnumeric():
            print(msg)
            for i in engine_selections:
                print(i)
            engine_type = input('Your selection: ')
        return int(engine_type)

    '''This function returns the brand name of the car
    '''
    def get_brand(self) -> str:
        return self._brand
    
    '''This function returns the engine type of the car
    '''
    def get_engine_type(self) -> int:
        return self._engine_type



if __name__ == "__main__":
    car1 = car()
    print(f'The details of this car:\n\t-Brand: {car1._brand}\n\t-Engine Type: {car1._engine_type}')
