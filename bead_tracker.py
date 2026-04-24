from blob_finder import BlobFinder
from picture import Picture
import math
import stdio
import sys

# Entry point
def main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    filenames = sys.argv[4:]

    # Process consecutive pairs of frames
    for k in range(len(filenames) - 1):
        pic_prev = Picture(filenames[k])
        pic_curr = Picture(filenames[k + 1])
        bf_prev = BlobFinder(pic_prev, tau)
        bf_curr = BlobFinder(pic_curr, tau)
        beads_prev = bf_prev.getBeads(pixels)
        beads_curr = bf_curr.getBeads(pixels)

        # For each bead in current frame, find closest bead in previous frame
        for bead_curr in beads_curr:
            min_dist = float('inf')
            closest_bead = None
            for bead_prev in beads_prev:
                d = bead_curr.distanceTo(bead_prev)
                if d < min_dist:
                    min_dist = d
                    closest_bead = bead_prev
            # If closest bead is within delta, record radial displacement
            if closest_bead is not None and min_dist <= delta:
                # Compute Euclidean distance between centers of mass
                # Extract center coordinates from __str__ format or compute directly
                # distanceTo already gives us the Euclidean distance
                stdio.writef("%.4f\n", min_dist)

if __name__ == "__main__":
    main()
