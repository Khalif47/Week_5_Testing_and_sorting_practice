#from task_3 import shakersort
import timeit


def time_sum_items(alist):
    start = timeit.default_timer()
    sum = 0
    for i in range(len(alist)):
        sum += alist[i]
    taken = timeit.default_timer() - start
    '''

    :param alist:
    :return: sum
    :Best case: O(1) an empty list
    :Worst case: O(n) normal lisst
    '''
    return taken




lista = []
print(time_sum_items(lista))

