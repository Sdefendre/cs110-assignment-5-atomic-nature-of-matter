from blob import Blob
from picture import Picture
import stdarray
import stdio
import sys

# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a
    # luminance threshold tau.
    def __init__(self, pic, tau):
        self._pic = pic
        self._tau = tau
        self._width = pic.width()
        self._height = pic.height()
        # Keep track of visited pixels
        self._visited = stdarray.create2D(self._width, self._height, False)
        self._blobs = []
        # Scan entire image for foreground pixels
        for j in range(self._height):
            for i in range(self._width):
                # Compute luminance (grayscale value)
                r = pic.getRed(i, j)
                g = pic.getGreen(i, j)
                b = pic.getBlue(i, j)
                luminance = 0.299 * r + 0.587 * g + 0.114 * b
                if luminance >= tau:
                    # Foreground pixel not yet visited -> start DFS
                    if not self._visited[i][j]:
                        blob = Blob()
                        self._findBlob(i, j, blob)
                        self._blobs.append(blob)

    # Depth-first search to identify a blob starting at pixel (i, j).
    def _findBlob(self, i, j, blob):
        # Check bounds
        if i < 0 or i >= self._width or j < 0 or j >= self._height:
            return
        # Check if already visited or not foreground
        if self._visited[i][j]:
            return
        # Compute luminance
        r = self._pic.getRed(i, j)
        g = self._pic.getGreen(i, j)
        b = self._pic.getBlue(i, j)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        if luminance < self._tau:
            return
        # Mark as visited and add to blob
        self._visited[i][j] = True
        blob.add(i, j)
        # Explore 4-connected neighbors
        self._findBlob(i + 1, j, blob)
        self._findBlob(i - 1, j, blob)
        self._findBlob(i, j + 1, blob)
        self._findBlob(i, j - 1, blob)

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        return [b for b in self._blobs if b.mass() >= pixels]

# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))

if __name__ == "__main__":
    _main()
