import random
import timeit


def bubblesort(alist):
    n = len(alist)
    for point in range(n - 1, 0, -1):
        swapped = False
        for j in range(point):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = True
        if not swapped:
            break
    return alist


def shakersort(alist):
    n = len(alist)
    for point in range(n - 1, 0, -1):
        swapped = False
        if point % 2 == 0:
            for j in range(point):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
                    swapped = True
        else:
            for j in range(point, 0, -1):
                if alist[j] < alist[j - 1]:
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]
                    swapped = True
        if not swapped:
            break
    return alist

def time_shakersort(alist):
    start = timeit.default_timer()
    shakersort(alist)
    taken = timeit.default_timer() - start
    '''

    :param alist:
    :return: sum
    :Best case: O(1) an empty list
    :Worst case: O(n) normal lisst
    '''
    return taken


def table_time_shakersort():
    tablelength = [0]*100
    tabletime = [0]*100
    sum = 0
    for t in range(100):
        alist = [0]
        n = random.randrange(2, 1024, 2)
        alist = alist * n
        for i in range(n):
            alist[i] = random.random()
        tablelength[t] = n
        tabletime[t] = time_shakersort(alist)
        sum += tabletime[t]
    finaltable = [tablelength, tabletime]
    average = sum/100
    print(average)

    return finaltable


print(table_time_shakersort())