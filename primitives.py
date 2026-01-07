class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# TODO: Rekajigger colors for RGB.
class Primitive:
    def __init__(self, origin: Point = Point(0, 0), color: int = 0):
        self.origin = origin
        self.color = color

    def draw(array):
        return array
    
    def set_color(self, color: int):
        self.color = color

class Rectangle(Primitive):
    """
    Rectangle where y is width and x is height.
    """
    def __init__(self, height, width, origin: Point = Point(0, 0), color=0):
        super().__init__(origin, color)
        self.height = height
        self.width = width

    def set_origin(self, point: Point):
        self.origin = point

    def draw(self, array):
        x0 = self.origin.x
        x1 = x0 + self.height
        y0 = self.origin.y
        y1 = y0 + self.width
        array[x0:x1:, y0:y1, self.color] = 255
        array[x0:x1:, y0:y1, 3] = 255
        return array
