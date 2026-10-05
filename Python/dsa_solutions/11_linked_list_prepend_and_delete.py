import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    delete_count = data[1 + count]
    linked_list = list(reversed(values))
    print(*linked_list[delete_count:])


if __name__ == "__main__":
    main()
