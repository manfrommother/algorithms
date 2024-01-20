def smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        
    return smallest_index


def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = smallest_index(arr)
        new_arr.append(arr.pop(smallest))  

    return new_arr


arr = [1, 3, 6, 0, 12, 15]

print(selection_sort(arr))

# [0, 1, 3, 6, 12, 15]


