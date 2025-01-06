def quicksort3(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quicksort3(left) + middle + quicksort3(right)
