def digit_sort(n, arr):

    print('Initial array:')
    print(*arr, sep=', ')

    m = len(arr[0])
    for phase in range(m):
        print('**********')
        print(f'Phase {phase + 1}')
        buckets = {i: [] for i in range(10)}
        for s in arr:
            buckets[int(s[-(phase + 1)])] += [s]
        new_arr = []
        for digit in sorted(buckets):
            print(f'Bucket {digit}: ', end='')
            print(*buckets[digit] if buckets[digit] else ['empty'], sep=', ')
            if buckets[digit]:
                new_arr += buckets[digit]
        arr = new_arr


    sorted_arr = []
    for digit in sorted(buckets):
        if buckets[digit]:
            sorted_arr += buckets[digit]

    print('**********')
    print('Sorted array:')
    print(*sorted_arr, sep=', ')


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr += [input()]

    digit_sort(n, arr)


if __name__ == '__main__':
    main()