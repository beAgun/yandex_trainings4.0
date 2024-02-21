def f(n, a):

    res = []
    for i in range(n):
        res += [sum(a) - a[0] * n if not i else res[i - 1] + (n - 2 * i) * (a[i - 1] - a[i])]

    return res


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    print(*f(n, arr))

if __name__ == '__main__':
    main()

'''
5
3 7 8 10 15

3 : 7-3  + 8-3  + 10-3 + 15-3 
s + a[i-1]*3 - a[i]*3

7 : 7-3  + 8-7  + 10-7 + 15-7 
s + a[i-1]*(2 - 1) - a[i]*(2 - 1)

8 : 8-3  + 8-7  + 10-8 + 15-8
s + a[i-1]*(1 - 2) - a[i]*(1 - 2)

10: 10-3 + 10-7 + 10-8 + 15-10
s + a[i-1]*(-3) - a[i]*(-3)

15: 15-3 + 15-7 + 15-8 + 15-10

s_next = s_prev +
         + a[i-1]*(right_num - left_num) -
	 - a[i]*(right_num - left_num) =

       = s_prev +
 	 + a[i-1]*(n-1-i - (i-1)) -
	 - a[i]*(n-1-i - i+1) =

       = s_prev + (n - 2 * i) * (a[i - 1] - a[i])
'''