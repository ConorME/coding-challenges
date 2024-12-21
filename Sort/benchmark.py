import time
from quicksort import quicksort
from quicksort2 import quicksort2
from quicksort_golf import q
from selectionsort import selectionsort
from selectionsort_2 import selectionsort_2
import random

def benchmark(sorting_algorithms, test_data):
    results = []
    for name, func in sorting_algorithms:
        data = test_data[:] 
        start_time = time.time()
        func(data) 
        end_time = time.time()
        results.append((name, end_time - start_time))
    return results

if __name__ == "__main__":
    sorting_algorithms = [
        ("Quicksort", quicksort),
        ("Quicksort2", quicksort2),
        ("Quicksort_golf", q),
        ("Selectionsort", selectionsort),
        ("Selectionsort_2", selectionsort_2),
    ]

    test_data = [random.randint(0, 10000) for _ in range(1000)]  

    results = benchmark(sorting_algorithms, test_data)

    print("Sorting Algorithm Performance:")
    for name, time_taken in results:
        print(f"{name}: {time_taken:.6f} seconds")

