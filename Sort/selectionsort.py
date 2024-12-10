def selectionsort (seq):
    for i in range(len(seq)):
        minimum = min(seq[i:])
        min_index = seq.index(minimum)

        seq[min_index] = seq[i]
        seq[i] = minimum

    return seq
