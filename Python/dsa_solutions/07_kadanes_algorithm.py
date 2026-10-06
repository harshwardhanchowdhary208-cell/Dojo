import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data or data[0] == 0:
        print(0)
        return
    count = data[0]
    numbers = data[1:1 + count]
    current_sum = best_sum = numbers[0]
    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        best_sum = max(best_sum, current_sum)
    print(best_sum)


if __name__ == "__main__":
    main()
