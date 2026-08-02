
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

   
    def fare(self):
        return self.seating_capacity * 100



class Bus(Vehicle):

   
    def fare(self):
        normal_fare = super().fare()
        total_fare = normal_fare + (normal_fare * 0.10)
        return total_fare



bus = Bus(50)

print("Total Bus Fare:", bus.fare())