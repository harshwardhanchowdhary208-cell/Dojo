import sys


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    operation_count, capacity = map(int, lines[0].split())
    stack = []
    output = []
    for line in lines[1:1 + operation_count]:
        operation = line.split()
        if operation[0] == "push":
            if len(stack) == capacity:
                output.append("stack overflow")
            else:
                stack.append(int(operation[1]))
        elif operation[0] == "pop":
            output.append(str(stack.pop()) if stack else "stack underflow")
        elif operation[0] == "top":
            output.append(str(stack[-1]) if stack else "stack underflow")
    print("\n".join(output))


if __name__ == "__main__":
    main()
