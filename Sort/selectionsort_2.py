def selectionsort_2(seq):
    n = len(seq)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq
