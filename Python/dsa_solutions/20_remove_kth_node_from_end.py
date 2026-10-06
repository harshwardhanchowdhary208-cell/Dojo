import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    position_from_end = data[1 + count]
    del values[count - position_from_end]
    print(" -> ".join(map(str, values)) + " -> nullptr")


if __name__ == "__main__":
    main()
