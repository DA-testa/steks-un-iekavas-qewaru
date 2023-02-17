# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1

            a = opening_brackets_stack.pop()
            if not are_matching(a.char, next):
                return i + 1

    if opening_brackets_stack:
        a = opening_brackets_stack.pop()
        return a.position
    return "Success"
    

def main():
    check = input("I or F: ")
    if check == "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch is None:
            print("Success")
        else:
            print(mismatch)
    
    elif check == "F":
        file = input()
        path = "./test/" + file

        with open (path, "r") as testfile:
            text = testfile.read()
            mismatch = find_mismatch(text)
            print(mismatch)

if __name__ == "__main__":
    main()
