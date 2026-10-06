import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    numbers = data[1:1 + count]
    target = data[1 + count]
    left = 0
    current_sum = 0
    best_length = count + 1
    for right, number in enumerate(numbers):
        current_sum += number
        while current_sum >= target:
            best_length = min(best_length, right - left + 1)
            current_sum -= numbers[left]
            left += 1
    print(0 if best_length == count + 1 else best_length)


if __name__ == "__main__":
    main()
