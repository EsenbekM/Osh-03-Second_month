def pair_sum(a, b):  # O(1)
    return a + b


def pair_sum_sequence(n):  # O(N)
    result = 0
    for i in range(n):
        result += i
    return result


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def ex_1():
    c = 0
    a = (len(arr1), len(arr2))
    print(a)
    for i in arr1:
        c += 1
        print(i)
    for j in arr2:
        c += 1
        print(j)
    print(c)


def ex_2():
    c = 0
    a = (len(arr1), len(arr2))
    print(a)
    for i in arr1:
        for j in arr2:
            c += 1
            print(i, j)
    print(c)


# ex_1()
ex_2()
