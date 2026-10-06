import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    target = data[1 + count]
    print("true" if target in values else "false")


if __name__ == "__main__":
    main()
