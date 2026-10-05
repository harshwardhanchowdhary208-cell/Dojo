import sys


def are_isomorphic(first, second):
    if len(first) != len(second):
        return False
    forward = {}
    backward = {}
    for left, right in zip(first, second):
        if forward.get(left, right) != right or backward.get(right, left) != left:
            return False
        forward[left] = right
        backward[right] = left
    return True


def main():
    first, second = sys.stdin.read().split()
    print("true" if are_isomorphic(first, second) else "false")


if __name__ == "__main__":
    main()
