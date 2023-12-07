# So inheritance is the backbone for reusability of the code

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# to inherit we use the syntax : class Child(Parent):
# and to use the constructor of superclass we use super()
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

    def breathe(self):
        super().breathe()
        print('doing this underwater')


nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"The number of eyes of our fish {nemo.num_eyes}")