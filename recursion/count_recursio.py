def my_count(arr):
    if arr == []:
        return 0
    
    return 1 + my_count(arr[1:])

lst = [1, 2, 3]

print(my_count(lst))