import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    numbers = data[1:1 + count]
    best_pair = (numbers[0], numbers[1])
    best_distance = abs(sum(best_pair))
    for left in range(count - 1):
        for right in range(left + 1, count):
            distance = abs(numbers[left] + numbers[right])
            if distance < best_distance:
                best_distance = distance
                best_pair = (numbers[left], numbers[right])
    print(*best_pair)


if __name__ == "__main__":
    main()
