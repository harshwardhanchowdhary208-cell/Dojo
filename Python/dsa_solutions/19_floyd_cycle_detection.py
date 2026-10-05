import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    count = data[0]
    values = data[1:1 + count]
    position = data[1 + count]
    nodes = [Node(value) for value in values]
    for index in range(count - 1):
        nodes[index].next = nodes[index + 1]
    if count and position != -1:
        nodes[-1].next = nodes[position - 1]
    print("true" if has_cycle(nodes[0] if nodes else None) else "false")


if __name__ == "__main__":
    main()
