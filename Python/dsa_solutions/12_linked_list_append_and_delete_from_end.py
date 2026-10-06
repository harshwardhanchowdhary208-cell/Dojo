import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    delete_count = data[1 + count]
    remaining = values[:max(0, count - delete_count)]
    print(*remaining)


if __name__ == "__main__":
    main()
