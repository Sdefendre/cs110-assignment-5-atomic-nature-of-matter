import stdio
import math

# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        self._pixels = []  # list of (x, y) pixel tuples
        self._sum_x = 0
        self._sum_y = 0

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):
        self._pixels.append((x, y))
        self._sum_x += x
        self._sum_y += y

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        return len(self._pixels)

    # Returns the Euclidean distance between the center of mass of this blob
    # and the center of mass of the other blob.
    def distanceTo(self, other):
        cx1 = self._sum_x / self.mass()
        cy1 = self._sum_y / self.mass()
        cx2 = other._sum_x / other.mass()
        cy2 = other._sum_y / other.mass()
        return math.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

    # Returns a string representation of this blob.
    def __str__(self):
        cx = self._sum_x / self.mass()
        cy = self._sum_y / self.mass()
        return "%d (%.4f, %.4f)" % (self.mass(), cx, cy)

# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln("a          = " + str(a))
    stdio.writeln("b          = " + str(b))
    stdio.writeln("dist(a, b) = " + str(a.distanceTo(b)))

if __name__ == "__main__":
    _main()
