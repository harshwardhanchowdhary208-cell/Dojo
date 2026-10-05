import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    numbers = data[1:1 + count]
    window_size = data[1 + count]
    window_sum = sum(numbers[:window_size])
    best_sum = window_sum
    for index in range(window_size, count):
        window_sum += numbers[index] - numbers[index - window_size]
        best_sum = max(best_sum, window_sum)
    print(best_sum)


if __name__ == "__main__":
    main()
