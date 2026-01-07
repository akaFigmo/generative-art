from PIL import Image
import numpy as np
from primitives import Rectangle, Point

class Canvas:
    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y
        self.array = np.zeros((self.x, self.y, 4), dtype=np.uint8)
        self.primitives = []

    def render(self):
        for primitive in self.primitives:
            primitive.draw(self.array)
        img = Image.fromarray(self.array, mode="RGBA")
        img.show()

    def add(self, primitive):
        self.primitives.append(primitive)


def main():
    canvas = Canvas(500, 500)
    canvas.add(Rectangle(10, 20))
    canvas.add(Rectangle(50, 50, Point(275, 125)))
    canvas.add(Rectangle(250, 100, Point(50, 100), color=1))
    canvas.add(Rectangle(50, 400, Point(250, 0), color=2))
    canvas.render()

if __name__ == "__main__":
    main()
