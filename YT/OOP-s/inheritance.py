# # simple inheritance 


# # Base Class 

# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def speak(self):
#         print(f"{self.name} is an animal")

# # Derived Class 

# class Dog(Animal):
#     def __init__(self, val1):
#         self.behaviour = "Friendly"
#         self.name = val1

#     def speak(self):
#         print(f" {self.name} barks. He is very {self.behaviour}")

# # animal = Animal("Dog")        
# # animal.speak() 

# dog = Dog("Budddy!!!")
# dog.speak() 


# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")


# Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()      # Call the parent constructor
        self.breed = breed      # Additional attribute for Dog

    def speak(self):
        super().speak()         # Call the parent class method
        print(f"{self.name} barks. It is a {self.breed}.")


dog = Dog("Golden Retriever")
dog.speak() 