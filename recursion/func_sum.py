def my_sum(arr):
    if arr == []:
        return 0
    
    return arr[0] + int(my_sum(arr[1:]))


lst = [1, 2, 3, 4, 7, -10]
print(my_sum(lst))    