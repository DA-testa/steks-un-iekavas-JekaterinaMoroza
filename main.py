#python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket (next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching (opening_brackets_stack.pop().char, next):
                return i + 1
    if opening_brackets_stack:
                return opening_brackets_stack[0].position + 1
            
    return "Success" 
    
def main():

    print("Izvēlies I vai F: ")
    text = input()

    if "I" in text:
        text=input()
        mismatch = find_mismatch(text)
        print(mismatch)

    elif "F" in text:
        mismatch = find_mismatch(text)

    else:
        print("Nepareiza izvēle!")

if __name__ == "__main__":
    main()
