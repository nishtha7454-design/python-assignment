class Box:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w

obj = Box(8, 4)
print("Area:", obj.calculate_area())
