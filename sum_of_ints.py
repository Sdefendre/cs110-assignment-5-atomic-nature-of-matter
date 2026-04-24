import stdio
import sys

# Entry point [DO NOT EDIT].
def main():
    n = int(sys.argv[1])
    stdio.writeln(_sumOfInts(n))

# Returns the sum 1 + 2 + ... + n, computed recursively.
def _sumOfInts(n):
    if n == 1:
        return 1
    return n + _sumOfInts(n - 1)

if __name__ == "__main__":
    main()
