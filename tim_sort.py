import random
import time
import matplotlib.pyplot as plt
import math

# ------------------- Constants -------------------
merger = 32  # This is the threshold used in TimSort to determine the "minrun" size.
              # Smaller runs are sorted with insertion sort for efficiency.

# ------------------- Functions -------------------

def calminimum(n):
    """
    Calculate the minimum run size for TimSort based on the input array length.
    TimSort splits the array into "runs" of size at least 'minrun' for optimal performance.
    
    Args:
        n (int): Length of the array
    
    Returns:
        int: Calculated minimum run size
    """
    r = 0
    while n >= merger:
        r |= n & 1  # Keep track if n is odd
        n >>= 1     # Divide n by 2 (bit shift right)
    return n + r   # minrun = n + leftover bit

def insertion_sort(arr, left, right):
    """
    Standard insertion sort algorithm used to sort small subarrays (runs) in TimSort.
    
    Args:
        arr (list): The array to sort
        left (int): Starting index of the run
        right (int): Ending index of the run
    """
    for i in range(left + 1, right + 1):
        j = i
        # Compare element with previous elements in the run
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap if out of order
            j -= 1

def merge_sort(arr, left, mid, right):
    """
    Merge function used in TimSort, merges two sorted subarrays.
    
    Args:
        arr (list): The array to sort
        left (int): Left index of the first subarray
        mid (int): Right index of the first subarray
        right (int): Right index of the second subarray
    """
    # Lengths of the two subarrays
    low = mid - left + 1
    high = right - mid

    # Create temporary arrays for merging
    left_arr = [arr[i + left] for i in range(low)]
    right_arr = [arr[mid + 1 + i] for i in range(high)]

    i, j, k = 0, 0, left  # i = left_arr index, j = right_arr index, k = arr index

    # Merge the two arrays back into the original array
    while i < low and j < high:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_arr
    while i < low:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_arr
    while j < high:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr):
    """
    Custom implementation of TimSort.
    TimSort is a hybrid sorting algorithm combining insertion sort and merge sort.
    1. Small subarrays (runs) are sorted using insertion sort.
    2. Then, these runs are merged using merge sort to form a fully sorted array.
    
    Args:
        arr (list): The array to sort
    """
    n = len(arr)
    minrun = calminimum(n)  # Determine the minimum run size

    # Step 1: Sort small runs with insertion sort
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge runs using merge sort
    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge_sort(arr, left, mid, right)
        size *= 2  # Double the size of merged runs in each iteration

# ------------------- Main Program -------------------
if __name__ == "__main__":
    # Ask the user for the maximum value for random array elements
    max_value = int(input("Enter the maximum value for array elements: "))

    # Define the array sizes to test TimSort performance
    sizes = [10, 100, 500, 1000, 5000, 10000]
    times = []

    # Measure time taken for each array size
    for n in sizes:
        # Generate random array of size 'n' with elements between 0 and max_value
        arr = [random.randint(0, max_value) for _ in range(n)]

        # Start timing
        start = time.time()

        # Sort the array using custom TimSort
        tim_sort(arr)

        # End timing
        end = time.time()
        elapsed = end - start
        times.append(elapsed)

        print(f"Array size: {n}, Time taken: {round(elapsed, 6)} seconds")

    # ------------------- Plotting the Time Complexity -------------------
    plt.figure(figsize=(10, 6))

    # Actual measured time
    plt.plot(sizes, times, marker='o', color='purple', label='TimSort actual time')

    # Overlay theoretical O(n log n) curve for comparison
    onlogn = [n * math.log2(n) * times[0] / (sizes[0] * math.log2(sizes[0])) for n in sizes]
    plt.plot(sizes, onlogn, marker='x', linestyle='--', color='orange', label='O(n log n)')

    plt.title("Time Complexity of TimSort with Big O Overlay")
    plt.xlabel("Array Size")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
