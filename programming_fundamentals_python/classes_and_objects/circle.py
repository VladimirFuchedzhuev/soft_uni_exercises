class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.radius

    def calculate_area(self):
        return Circle.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle.__pi * self.radius ** 2


circle = Circle(45)

print(circle.calculate_circumference())
