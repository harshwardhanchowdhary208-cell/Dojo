import sys


def main():
    text = sys.stdin.read().strip()
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character not in pairs or not stack or stack.pop() != pairs[character]:
            print("false")
            return
    print("true" if not stack else "false")


if __name__ == "__main__":
    main()
