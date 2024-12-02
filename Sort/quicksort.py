def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Select a pivot
    pivot = arr[len(arr) // 2]
    
    # Partitiion the array
    # Values less than the pivot into the left side
    # Values greater than the pivot into the right side
    
    # Note: array slicing is kinda slow and space innefficient
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursive call on each portion of the array
    return quicksort(left) + middle + quicksort(right)

