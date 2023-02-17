from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    a = opening_brackets_stack.pop()
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1

            if not are_matching(a.char, next):
                return i + 1

    if opening_brackets_stack:
        return a
    return "Code is correct."
    

def main():
    check = input("I or F: ")
    if check == "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch is None:
            print("Code is correct.")
        else:
            print(mismatch)
    
    elif check == "F":
        path = input()
        with open (path, mode = "r") as testfile:
            text = testfile.read()
            mismatch = find_mismatch()
            print(mismatch)

if __name__ == "__main__":
    main()
