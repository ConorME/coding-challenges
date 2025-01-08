import timeit
from partition import partition
from remove_kth import remove_kth
from remove_middle import remove_middle
from kth_last import kth_last_two_pointer, kth_last_length
from remove_duplicates import remove_duplicates_set, remove_duplicates_no_buffer
from linked_list import generate_linked_list

def benchmark_functions(test_size, k, iterations=1000):
    head = generate_linked_list(test_size)
    functions = {
        "Partition": lambda: partition(head, k),
        "Remove Middle": lambda: remove_middle(head),
        "Remove Kth": lambda: remove_kth(head, k),
        "Kth Last - Two Pointer": lambda: kth_last_two_pointer(head, k),
        "Kth Last - Length Based": lambda: kth_last_length(head, k),
        "Remove Duplicates - Set": lambda: remove_duplicates_set(head),
        "Remove Duplicates - No Buffer": lambda: remove_duplicates_no_buffer(head)
    }

    results = {}
    for name, func in functions.items():
        timer = timeit.timeit(func, number=iterations)
        results[name] = timer / iterations

    print(f"\nBenchmark Results (Size={test_size}, k={k}):")
    for name, result in results.items():
        print(f"{name}: {result:.6f} seconds per call")

if __name__ == "__main__":
    benchmark_functions(test_size=1000, k=100)

