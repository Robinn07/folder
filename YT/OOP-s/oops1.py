# Initaiate aa class 


class employee:
    # Special methodo

    def __init__ (self):
        print("Started Executing Attributes/Data")
        self.id = 123
        self.salary = 50000
        self.dessignation = "MLOps Engg."
        print("Ended Execution Of Attributes/Data")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# Create an object (instantiation)
emp1 = employee()

# Call a method on the object
emp1.travel("Bangalore")

