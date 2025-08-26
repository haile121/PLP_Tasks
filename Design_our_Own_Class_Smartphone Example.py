# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Inherited class – exploring polymorphism
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system  # extra attribute
    
    # Overriding method to show specialized behavior
    def info(self):
        super().info()
        print(f"Cooling System: {self.cooling_system}")

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Advanced Liquid Cooling")

# Call methods
phone1.info()
phone1.call("123-456-7890")

print()
phone2.info()
phone2.call("987-654-3210")
