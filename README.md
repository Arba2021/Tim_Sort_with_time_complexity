# Dimensional TimSort Sorting Visualization

![TimSort Visualization](https://user-images.githubusercontent.com/yourusername/placeholder.png)

## Overview

This project implements a **custom TimSort algorithm** in Python and demonstrates its **time complexity** with both **actual measured times** and **theoretical O(n log n)** growth curves. TimSort is a hybrid sorting algorithm combining **insertion sort** and **merge sort**, widely used in Python's built-in `.sort()` and Java's `Arrays.sort()` for objects.

The project generates **random arrays of user-defined sizes and max values**, sorts them using the custom TimSort, measures execution time, and visualizes the results with matplotlib.

## Features

* Custom implementation of **TimSort** from scratch.
* Works efficiently for small and large arrays.
* Visualizes **time complexity** with a plot comparing **actual performance** and **O(n log n) theoretical growth**.
* Fully commented code for educational purposes.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/timsort-visualization.git
   cd timsort-visualization
   ```
2. Install dependencies:

   ```bash
   pip install matplotlib
   ```
3. Run the script:

   ```bash
   python timsort_visualization.py
   ```

## Usage

1. The program will prompt you for the **maximum value** of array elements.
2. It will then generate arrays of different sizes `[10, 100, 500, 1000, 5000, 10000]`.
3. TimSort will sort each array, and execution time will be measured.
4. A **line graph** will be displayed showing:

   * Purple line: Actual time taken by TimSort.
   * Orange dashed line: Theoretical O(n log n) growth.

## Example Output

```
Enter the maximum value for array elements: 1000
Array size: 10, Time taken: 0.000123 seconds
Array size: 100, Time taken: 0.000345 seconds
Array size: 500, Time taken: 0.001234 seconds
...
```

The plotted graph clearly shows how **TimSort scales with input size** and how it compares to **O(n log n)** complexity.

## Code Structure

* `calminimum(n)` : Calculates the minimum run size.
* `insertion_sort(arr, left, right)` : Sorts small subarrays using insertion sort.
* `merge_sort(arr, left, mid, right)` : Merges two sorted subarrays.
* `tim_sort(arr)` : Main TimSort algorithm combining insertion and merge sort.
* `Main Program` : Handles array generation, timing, and plotting.

## Technologies Used

* Python 3.x
* Matplotlib for plotting graphs
* Random module for array generation
* Time module for measuring performance

## Future Improvements

* Allow user to input **custom array sizes** instead of predefined ones.
* Support for **N-dimensional arrays**.
* Save the generated plot as an image automatically.
* Include interactive visualization using **Plotly** or **Matplotlib animations**.

## License

This project is licensed under the MIT License.

---

*Created for educational purposes to understand TimSort and its time complexity.*
