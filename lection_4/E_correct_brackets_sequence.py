import sys
input = sys.stdin.readline


def correct_brackets_sequences(n):
    if n % 2 != 0:
        return ''

    res = []
    def rec(cur_str='', cnt=0, stack=None):
        if stack is None:
            stack = []

        nonlocal  res
        if len(cur_str) == n:
            res += [cur_str]

        for ch in ['(', '[', ')', ']']:
            if ch in ['(', '['] and cnt < n / 2:
                ans = rec(cur_str + ch, cnt + 1, stack + [ch])
            if ch == ')' and len(stack) != 0 and stack[-1] == '(':
                new_stack = stack.copy()
                new_stack.pop()
                ans = rec(cur_str + ch, cnt, new_stack)
            if ch == ']' and len(stack) != 0 and stack[-1] == '[':
                new_stack = stack.copy()
                new_stack.pop()
                ans = rec(cur_str + ch, cnt, new_stack)

    rec()
    return res


def main():
    n = int(input())
    print(*correct_brackets_sequences(n), sep='\n')


if __name__ == '__main__':
    main()