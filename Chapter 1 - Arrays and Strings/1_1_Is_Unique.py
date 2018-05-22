"""Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?"""
def IsUnique (inputstring):
    inputstring = sorted(inputstring)
    prev = None
    for curr in inputstring:
        if (curr == prev):
            return False
        prev = curr
    return True

inputstring = input("type in a string to check uniqueness : ")
print(IsUnique(inputstring))
