# 1
'''class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print("Vehicle Info:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        super().display_info()
        print("Car Model:", self.model)

# Input
brand = "BMW"
model = "X5"

c = Car(brand, model)
c.display_info()
'''
#2
words = ["hello", "world"]
uppercase_words = list(map(lambda s: s.upper(), words))
print(uppercase_words)

def print_numbers(n):
    if n == 0:
        return
    print(n, end=" ")
    print_numbers(n - 1)


n = 5
print_numbers(n)
