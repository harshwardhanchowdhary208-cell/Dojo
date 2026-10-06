import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count, position, value = data[:3]
    values = data[3:3 + count]
    values.insert(position, value)
    print(*values)


if __name__ == "__main__":
    main()
