import stdio
import sys

# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))

# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and _isPalindrome(s[1:-1])

if __name__ == "__main__":
    main()
