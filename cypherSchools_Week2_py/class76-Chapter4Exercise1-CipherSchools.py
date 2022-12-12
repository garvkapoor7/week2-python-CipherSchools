class Phone:  #base class/ parent class\
    def __init__(self, brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

def full_name(self):
    return f"{self.brand} {self.model_name}"

def make_a_call(self, number):
    return f"calling {number}...."


class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory,rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memeory = internal_memory
        self.rear_camera = rear_camera


phone = Phone('nokia','1100',1000)
Smartphone = Smartphone('onePlus','5',30000,'6 GB','64 GB','20MP')
print(phone.full_name())
print(Smartphone.full_name()+f"and price is {Smartphone._price}")