import stdio
import sys

# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))

# Returns True if pwd is a valid password, and False otherwise.
# Requirements:
#   - At least 8 characters
#   - At least one digit
#   - At least one uppercase letter
#   - At least one lowercase letter
#   - At least one non-alphanumeric character
def _isValid(pwd):
    if len(pwd) < 8:
        return False
    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False
    for ch in pwd:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        else:
            has_special = True
    return has_digit and has_upper and has_lower and has_special

if __name__ == "__main__":
    main()
