import sys


def partition(numbers, low, high):
    pivot = numbers[high]
    smaller = low
    for index in range(low, high):
        if numbers[index] <= pivot:
            numbers[smaller], numbers[index] = numbers[index], numbers[smaller]
            smaller += 1
    numbers[smaller], numbers[high] = numbers[high], numbers[smaller]
    return smaller


def quick_sort(numbers):
    stack = [(0, len(numbers) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot_index = partition(numbers, low, high)
        stack.append((low, pivot_index - 1))
        stack.append((pivot_index + 1, high))


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    numbers = data[1:1 + count]
    quick_sort(numbers)
    print(*numbers)


if __name__ == "__main__":
    main()
