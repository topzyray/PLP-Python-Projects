def main():
    for animal in [Cat(), Dog()]:
        print(f"{animal.category}: {animal.sound()}")



class Cat:
    category = "Cat"

    def __init__(self) -> None:
        self.category

    def sound(self):
        return "Meow"



class Dog:
    category = "Dog"

    def __init__(self) -> None:
        self.category

    def sound(self):
        return "Bark"



if __name__ == "__main__":
    main()