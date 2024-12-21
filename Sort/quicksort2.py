def quicksort2(s: list[int]):
    if len(s) <= 1:
        return s

    pivot = s[len(s) // 2]

    left   = [x for x in s if x < pivot]
    right  = [x for x in s if x > pivot]
    equals = [x for x in s if x == pivot]

    return quicksort2(left) + equals + quicksort2(right)



