from collections import Counter


def is_anagram(str1, str2):
    return 'YES' if Counter(str1) == Counter(str2) else 'NO'


def main():
    str1 = input()
    str2 = input()

    print(is_anagram(str1, str2))


if __name__ == '__main__':
    main()