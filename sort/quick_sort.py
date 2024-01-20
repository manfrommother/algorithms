def quick_sort(arr):
    arr = list(arr)
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        bigger = [i for i in arr if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(bigger)



lst = [1, 4, 10, 8, 91, 1, 21]
print(quick_sort(lst))
