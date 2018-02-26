import random
from task_1 import time_sum_items

def table_time_sum_items():
    alist = [0]
    n = random.randrange(2, 1024, 2)
    alist = alist*n
    for i in range(n):
        alist[i] = random.random()
    time_sum_items(alist)
    return


print(table_time_sum_items())





