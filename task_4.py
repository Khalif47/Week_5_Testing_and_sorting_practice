# Selection sort algorithm
import random
import timeit


def selectionsort(alist):
    n = len(alist)
    for i in range(n):
        minimum_position = min_index(alist, i)
        # swap minimum with i
        alist[minimum_position], alist[i] = alist[i], alist[minimum_position]
    return alist


def min_index(alist, point):
    n = len(alist)
    minimum = point
    for i in range(point + 1, n):
        if alist[i] < alist[minimum]:
            minimum = i
    return minimum


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


def time_bubblesort(alist):
    start = timeit.default_timer()
    bubblesort(alist)
    taken = timeit.default_timer() - start
    '''

    :param alist:
    :return: sum
    :Best case: O(1) an empty list
    :Worst case: O(n) normal lisst
    '''
    return taken


def table_time_bubblesort():
    '''

    :return: finaltable
    complexity: worst case, best case O(n**2)
    '''
    tablelength = [0] * 100
    tabletime = [0] * 100
    sum = 0
    for t in range(100):
        alist = [0]
        n = random.randrange(2, 1024, 2)
        alist = alist * n
        for i in range(n):
            alist[i] = random.random()
        tablelength[t] = n
        tabletime[t] = time_bubblesort(alist)
        sum += tabletime[t]
    finaltable = [tablelength, tabletime]
    average = sum / 100
    print(average)

    return finaltable


def time_selection(alist):
    '''

    :param alist:
    :return: taken
    :complexity: best caee O(n) worst case O(n**2)
    '''
    start = timeit.default_timer()
    selectionsort(alist)
    taken = timeit.default_timer() - start
    '''

    :param alist:
    :return: sum
    :Best case: O(1) an empty list
    :Worst case: O(n) normal lisst
    '''
    return taken


def table_time_selectionsort():
    tablelength = [0] * 100
    tabletime = [0] * 100
    sum = 0
    for t in range(100):
        alist = [0]
        n = random.randrange(2, 1024, 2)
        alist = alist * n
        for i in range(n):
            alist[i] = random.random()
        tablelength[t] = n
        tabletime[t] = time_selection(alist)
        sum += tabletime[t]
    finaltable = [tablelength, tabletime]
    average = sum / 100
    print(average)

    return finaltable


print(table_time_selectionsort())
print(selectionsort([2, -1, 0, 5, 3, -1, 2]))
