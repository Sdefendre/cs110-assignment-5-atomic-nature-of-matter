# Atomic Nature of Matter

Estimates Avogadro's number from microscope video of beads in Brownian motion, repeating the experiment Jean Perrin used to confirm that atoms exist.

## What it does

1. **`blob.py`**: a `Blob` type, a connected group of pixels that tracks its mass and center of mass.
2. **`blob_finder.py`**: finds the beads in each frame. It marks pixels brighter than a threshold as foreground, groups them into connected components with depth-first search, and keeps blobs above a minimum size.
3. **`bead_tracker.py`**: compares each pair of consecutive frames, matches every bead to the nearest bead in the previous frame, and prints how far it moved.
4. **`avogadro.py`**: converts those distances from pixels to meters and applies the Einstein–Smoluchowski and Stokes–Einstein equations to estimate Boltzmann's constant, and from that Avogadro's number.

On the provided data it estimates **6.633 × 10²³**, which matches the reference value (the true constant is 6.022 × 10²³).

```sh
python3 bead_tracker.py 25 180.0 25.0 run_1/*.jpg | python3 avogadro.py
```

The image frames came with the course materials and aren't included here.

## Concepts

Object-oriented design, graph search (DFS flood fill), image processing, and applying physics formulas to real data.

Also included are warm-up exercises: `interval`, `rectangle`, `palindrome`, `password_checker` and `sum_of_ints`.

## Running it

These programs use the standard libraries from *Introduction to Programming in Python* (Sedgewick, Wayne & Dondero): `stdio`, `stdarray`, `stdrandom` and friends. Put those modules on your `PYTHONPATH`, then run the scripts with Python 3.

## Credit

Adapted from the Atomic Nature of Matter assignment developed at Princeton University by David Botstein, Tamara Broderick, Ed Davisson, Daniel Marlow, William Ryu and Kevin Wayne.

## Course

CS110 Introduction to Computing, UMass Boston, Spring 2026 (instructor: Swami Iyer). The instructor supplied the starter code and course libraries. My approach and notes for each problem are in [`notes.txt`](notes.txt).
