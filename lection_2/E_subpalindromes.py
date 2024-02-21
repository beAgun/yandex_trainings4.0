from sys import stdin
from math import floor


def f(s):

    n = len(s)
    p = 10 ** 9 + 7
    x_ = 263
    h = [0] * (n + 1)
    h_op = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        h_op[i] = (h_op[i - 1] * x_ + ord(s[-i])) % p
        x[i] = (x[i - 1] * x_) % p

    number_of_palindromes = [0] + [1] * n
    # 12 22 2 22 21
    for i in range(1, n): # 2
        l, r = 1, i - 1 # 1, 1
        max_length_of_palindrome = 0
        while l <= r:
            m = floor((r + l) / 2) # 1
            slen = i - m  # 1
            from1 = m
            from2 = n - i - slen + 1

            if ((h[from1 + slen - 1] + h_op[from2 - 1] * x[slen]) % p ==
                (h_op[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p):
                max_length_of_palindrome = max(max_length_of_palindrome, slen)
                r = m - 1
            else:
                l = m + 1
        number_of_palindromes[i] += max_length_of_palindrome
        #print(i, s[i], max_length_of_palindrome)

        # 12 12 11 21 23
        if s[i] == s[i + 1]:
            l, r = 1, i - 1  # 1, 1
            number_of_palindromes[i] += 1
            #print(i, s[i], 1)
            max_length_of_palindrome = 0
            while l <= r:
                m = floor((r + l) / 2) # 1
                slen = i - m  # 1
                from1 = m
                from2 = n - i - slen
                #slen += 1

                if ((h[from1 + slen - 1] + h_op[from2 - 1] * x[slen]) % p ==
                    (h_op[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p):
                    max_length_of_palindrome = max(max_length_of_palindrome, slen)
                    r = m - 1
                else:
                    l = m + 1
            number_of_palindromes[i] += max_length_of_palindrome
            #print(i, s[i], max_length_of_palindrome)

    return sum(number_of_palindromes)


def main():
    s = stdin.readline().rstrip()

    print(f(s))


if __name__ == '__main__':
    main()
    #test()

'''
121345121
9 + 2 = 11

12213451221
11 + 2 + 2 = 15

baaab
5 + 2 + 2 = 9

abaaaba
7 + 3 + 2 + 2 = 14

1111
4 + 2 + 2 + 2 = 10

aabdcaabdfsesrtreerty
21 + 2 + 1 + 3 + 1 = 28
'''