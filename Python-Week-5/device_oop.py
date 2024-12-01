def main():
    print("Super class instantiation")
    phone1 = Device("Smartphone")
    phone1.displayInfo()

    print()

    print("Sub class instantiation")
    phone2 = Iphone("Smartphone", "Iphone", "Pro-Max")
    phone2.displayInfo()

# Base or super class
class Device:
    # Base class constructor
    def __init__(self, type = "SmartPhone"):
        self.type = type # Base class property

    # Base class method
    def displayInfo(self):
        print(f"Type: {self.type}")

# Sub or inherited class
class Iphone(Device):
    # Sub class constructor inheriting from the base class
    def __init__(self, type, product, brand):
        super().__init__(type)
        self.brand = brand
        self.product = product

    # Polymorphism: sub class method
    def displayInfo(self):
        print(f"Type: {self.type}")
        print(f"Product: {self.product}")
        print(f"Brand: {self.brand}")

if __name__ == "__main__":
    main()