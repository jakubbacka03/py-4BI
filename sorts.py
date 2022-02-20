#bubble
def bubble_sort(unordered_list):
    length = len(unordered_list)
    for i in range(1, length):
        for j in range(length - 1):
            if unordered_list[j] > unordered_list[j + 1]:
                unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]

#selection
def selection_sort(unordered_list):
    length = len(unordered_list)
    for j in range (length - 1):
        small = unordered_list[j]
        s_position = j
        for i in range((j + 1), length):
            if small > unordered_list[i]:
                small = unordered_list[i]
                s_pos = i

        if s_pos is not j:
            unordered_list[j], unordered_list[s_position] = unordered_list[s_position], unordered_list[j]

#insertion
def insertion_sort(unordered_list):
    length = len(unordered_list)
    for i in range(1, length):
        j = i
        while j > 0 and unordered_list[j - 1] > unordered_list[j]:
            unordered_list[j], unordered_list[j - 1] = unordered_list[j - 1], unordered_list[j]
            j = j - 1

#quick
def quicksort_part(unordered_list, low, high):
    i = low - 1
    pivot = unordered_list[high]
    for j in range(low, high):
        if unordered_list[j] <= pivot:
            i += 1
            unordered_list[j], unordered_list[i] = unordered_list[i], unordered_list[j]

    unordered_list[i + 1], unordered_list[high] = unordered_list[high], unordered_list[i + 1]
    return i + 1

def quicksort_s(unordered_list, low, high):
    if low < high:
        index = quicksort_part(unordered_list, low, high)
        quicksort_s(unordered_list, low, index - 1)
        quicksort_s(unordered_list, index + 1, high)

def quick_sort(unordered_list):
    length = len(unordered_list)
    quicksort_s(unordered_list, 0, length - 1)

#merge
def merge(list_one, list_two):
    sorted_list = list()
    while len(list_one) != 0 and len(list_two) != 0:
        if list_one[0] > list_two[0]:
            sorted_list.append(list_two[0])
            list_two.pop(0)
        else:
            sorted_list.append(list_one[0])
            list_one.pop(0)

    while len(list_one) != 0:
        sorted_list.append(list_one[0])
        list_one.pop(0)

    while len(list_two) != 0:
        sorted_list.append(list_two[0])
        list_two.pop(0)

    return sorted_list


def merge_sort(unordered_list):
    length = len(unordered_list)
    if length <= 1:
        return unordered_list

    list_one = unordered_list[0:int((length/2))]
    list_two = unordered_list[(int(length/2) + 1):-1]
    list_one = merge_sort(list(list_one))
    list_two = merge_sort(list(list_two))

    return merge(list_one, list_two)