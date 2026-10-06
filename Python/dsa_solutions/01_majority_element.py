import sys


def main():
    values = list(map(int, sys.stdin.read().split()))
    if not values:
        return
    count = values[0]
    numbers = values[1:1 + count]
    candidate = None
    votes = 0
    for number in numbers:
        if votes == 0:
            candidate = number
        votes += 1 if number == candidate else -1
    print(candidate if numbers.count(candidate) > count // 2 else -1)


if __name__ == "__main__":
    main()
