import sys
from collections import deque


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    queue = deque(data[1:1 + count])
    output = []
    while queue:
        output.append(str(queue.popleft()))
    print("\n".join(output))


if __name__ == "__main__":
    main()
