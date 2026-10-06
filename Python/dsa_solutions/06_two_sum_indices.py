import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    numbers = data[1:1 + count]
    target = data[1 + count]
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            print(seen[needed], index)
            return
        seen[number] = index
    print(-1)


if __name__ == "__main__":
    main()
