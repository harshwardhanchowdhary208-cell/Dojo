import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    pivot = data[1 + count]
    partitioned = [value for value in values if value < pivot]
    partitioned.extend(value for value in values if value >= pivot)
    print(*partitioned)


if __name__ == "__main__":
    main()
