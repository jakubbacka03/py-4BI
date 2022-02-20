import random
import time
import sorts

def r_list(length, max_cislo):
    t_list = list()
    for i in range(length):
        t_list.append(random.randint(0, max_cislo))
    return t_list

def test():
    uo_list = r_list(5000, 500)
    start = time.time()
    sorts.bubble_sort(list(uo_list))
    end = time.time()
    print("BubbleSort:", (end - start), "s")

    start = time.time()
    sorts.selection_sort(list(uo_list))
    end = time.time()
    print("SelectionSort:", (end - start), "s")

    start = time.time()
    sorts.insertion_sort(list(uo_list))
    end = time.time()
    print("InsertionSort:", (end - start), "s")

    start = time.time()
    sorts.quick_sort(list(uo_list))
    end = time.time()
    print("QuickSort:", (end - start), "s")

    start = time.time()
    sorts.merge_sort(list(uo_list))
    end = time.time()
    print("MergeSort:", (end - start), "s")

    start = time.time()
    sort_list = list(uo_list)
    sort_list.sort()
    end = time.time()
    print("PythonSort:", (end - start), "s")

test()