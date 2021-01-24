class Dog:
    # class variable
    animal = "Dog"

    def __init__(self, breed, color):
        # instance variables
        self.breed = breed
        self.color = color


# objects of the Dog class
punto = Dog("Pug", "Brown")
prezzo = Dog("Bulldog", "Grey")

print("punto details")
print("punto is a", punto.animal)
print("punto breed is ", punto.breed)
print("punto's color is ", punto.color)

print("prezzo details")
print("prezzo is a", prezzo.animal)
print("prezzo breed is ", prezzo.breed)
print("prezzo's color is ", prezzo.color)