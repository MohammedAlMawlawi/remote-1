'''This is a car class
'''
from random import randint as rand
from time import sleep

class car:
    _engine_types: dict = {1 : 'Petrol Engine',
                           2 : 'Hybrid Engine',
                           3 : 'Electric Motor',
                           4 : 'Deseil Engine',
                           5 : 'Liquid Gas Engine'
                           }
    _body_shapes: dict = {1 : 'Sport',
                          2 : 'Sedan',
                          3 : 'SUV',
                          4 : 'Truck',
                          5 : 'Hatchback'
                          }
    _brand_names: list = ['Ferrari', 'Porsche', 'Mercedes', 'BMW']

    def __init__(self):
        print('Welcome to cars game\nYou will create your own car \U0001F600\
                \nThere are many brands you can choose wither from this list or from your mind')        
        self._print_brand()
        self._brand = self.set_brand()
        self._engine_type = self._engine_types[self.set_engine_type()]
        self._body_shape = self._body_shapes[self.set_body_shape()]

    '''This function randomly prints car brands
    '''
    def _print_brand(self):
        random_brand : list = []
        for i in self._brand_names:
            random_name = (self._brand_names[rand(1,self._brand_names.__len__() - 1)])
            if not random_name in random_brand:
                random_brand.append(random_name)
                print(random_name)
                sleep(2)

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

    '''This function returns a number that represents the body shape of the car
    '''
    def set_body_shape(self):
        body_shapes = [f'For {value} = {key}' for key,value in self._body_shapes.items()]
        msg = 'select the number representing the body shape:\n'
        for i in body_shapes:
            print(i)
        body_shape = input(msg)
        while not body_shape.isnumeric():
            for i in body_shapes:
                print(i)
            body_shape = input(msg)
        return int(body_shape)

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
    print(f'The details of this car:\n\t-Brand: {car1._brand}\n\t-Engine Type: {car1._engine_type}\
            \n\t-Body Shape: {car1._body_shape}')
