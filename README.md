# 🚀 TimSort Sorting Visualization

![TimSort Performance](images/timsort_graph.png)

## 🔥 Overview

Dive into the world of **TimSort**, the super-efficient hybrid sorting algorithm used in Python and Java! This project showcases a **custom TimSort implementation** and visualizes its **time complexity** across different array sizes.

TimSort intelligently combines:

* **Insertion Sort** for small subarrays (runs)
* **Merge Sort** for merging runs efficiently

With this project, you can see how TimSort handles random arrays of various sizes and compare **actual execution times** with **theoretical O(n log n) growth**.

## ✨ Features

* ✅ Fully custom **TimSort** implementation from scratch
* ✅ Handles arrays of varying sizes and random values
* ✅ Visualizes **time complexity** with a sleek matplotlib graph
* ✅ Overlay of **O(n log n)** theoretical curve for comparison
* ✅ Highly commented, easy-to-understand code

## 🛠 Installation

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

## 🚀 Usage

1. Input the **maximum value** for array elements when prompted.
2. The program will automatically generate arrays of sizes `[10, 100, 500, 1000, 5000, 10000]`.
3. TimSort will sort each array and measure execution time.
4. A **dynamic graph** will display:

   * **Purple line:** Actual TimSort execution time
   * **Orange dashed line:** Theoretical O(n log n) growth

## 🎯 Example Output

```
Enter the maximum value for array elements: 1000
Array size: 10, Time taken: 0.000123 seconds
Array size: 100, Time taken: 0.000345 seconds
Array size: 500, Time taken: 0.001234 seconds
...
```

## 📂 Code Structure

* `calminimum(n)` : Calculates minimum run size
* `insertion_sort(arr, left, right)` : Sorts small runs
* `merge_sort(arr, left, mid, right)` : Merges sorted runs
* `tim_sort(arr)` : Main TimSort algorithm
* `Main Program` : Array generation, timing, and plotting

## 🌐 Technologies Used

* Python 3.x
* Matplotlib for plotting
* Random module for array generation
* Time module for performance measurement

## 🔮 Future Improvements

* Interactive **Plotly visualization** for better UI
* Support for **user-defined array sizes and dimensions**
* Automatic saving of generated plots in multiple formats
* Educational animations demonstrating **run splitting and merging**

## 📝 License

This project is licensed under the MIT License.

---

*Created for educational purposes to visualize TimSort performance and understand algorithmic complexity.*
