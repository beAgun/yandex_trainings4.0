def is_correct(s):

    stack = []

    for ch in s:
        if ch in ('(', '[', '{'):
            stack += [ch]

        if ch in (')', ']', '}'):
            if len(stack) == 0:
                return 'no'
            top = stack.pop()
            if (top == '(' and ch != ')' or
                top == '[' and ch != ']' or
                top == '{' and ch != '}'):
               return 'no'

    return 'no' if len(stack) else 'yes'


def test(f):
    import random
    import string
    import time

    assert f('[]') == 'yes'
    assert f('(){}') == 'yes'
    assert f('([])') == 'yes'
    assert f('(())') == 'yes'
    assert f('{[]}()') == 'yes'
    assert f('{') == 'no'
    assert f('123({[([{}])]}') == 'no'
    assert f('123({}') == 'no'
    assert f('{[}') == 'no'
    assert f('foo(bar);') == 'yes'
    assert f('foo(bar[i);') == 'no'

    n = 10 ** 5
    s = ''.join([random.choice(string.printable) for _ in range(n)])
    t0 = time.perf_counter()
    f(s)
    t1 = time.perf_counter()

    if t1 - t0 < 2:
        print(f'Everything is OK. Ex time:{t1 - t0}')


def main():
    s = input()

    print(is_correct(s))


if __name__ == '__main__':
    main()
    #test(is_correct)