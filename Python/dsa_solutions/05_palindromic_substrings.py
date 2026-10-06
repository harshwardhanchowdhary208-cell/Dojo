import sys


def main():
    text = sys.stdin.read().strip()
    palindromes = []
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            substring = text[start:end]
            if substring == substring[::-1]:
                palindromes.append(substring)
    print(" ".join(palindromes))
    print(len(palindromes))


if __name__ == "__main__":
    main()
