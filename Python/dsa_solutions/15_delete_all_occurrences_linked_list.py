import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    target = data[1 + count]
    print(*(value for value in values if value != target))


if __name__ == "__main__":
    main()
