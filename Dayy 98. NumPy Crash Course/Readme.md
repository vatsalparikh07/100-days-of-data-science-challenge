# 💻 NumPy Fundamentals: Array Operations & Image Manipulation

[![NumPy](https://img.shields.io/badge/NumPy-Core_Library-blue?logo=numpy&style=flat-square)](https://numpy.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?logo=python&style=flat-square)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=flat-square)](https://matplotlib.org/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_98-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

![image](https://github.com/user-attachments/assets/413e3aae-d1d5-4417-82fb-76bf9e34775f)
*Fig 1: Conceptual representation of 1D, 2D, and 3D NumPy arrays*

## 🎯 Project Goal: Mastering NumPy for Scientific Computing

Welcome to Day 98 of my #100DaysOfDataScience challenge! This project is a "crash course" in **NumPy (Numerical Python)**, the foundational package for scientific computing in Python. We explore NumPy's core object, the **n-dimensional array (`ndarray`)**, and demonstrate its power and efficiency for numerical operations, particularly with a case study involving image data manipulation.

**The Mission:**
1.  Understand and create NumPy arrays from Python lists and ranges.
2.  Learn how to reshape arrays into different dimensions (1D, 2D, 3D).
3.  Recognize array limitations like the absence of column names and single data type enforcement (leading to type coercion).
4.  Master a powerful NumPy function: `np.where()` for conditional element replacement.
5.  Apply these concepts to a practical use case: manipulating RGB image data represented as a 3D NumPy array.

This project serves as a foundational step for anyone looking to delve into data science, machine learning, or any field requiring efficient numerical computation in Python, as many core libraries (like Pandas) are built on top of NumPy.

---

## ✨ Key Features & Concepts Mastered

*   **NumPy Array Creation:**
    *   From Python Lists: Using `np.array()` to create 1D (`np.array(list_1)`) and 2D arrays (`np.array((list_1, list_2))`).
    *   From Ranges: Using `np.arange(start, stop)` to create 1D arrays with a sequence of numbers.
*   **Array Reshaping:**
    *   Utilizing the `.reshape((dim1, dim2, ...))` method to change the dimensions of an array while preserving its data [1]. Demonstrated reshaping a 1D array into 2D (rows, columns) and 3D (num_2d_arrays, rows, columns).
*   **N-Dimensional Arrays:** Understanding the concept of arrays with any number of dimensions and how they can be structured (e.g., a 3D array as a list of 2D arrays).
*   **Array Limitations & Type Coercion:**
    *   Arrays store data of a **single type**. If created with mixed types, NumPy performs **type coercion** to ensure homogeneity.
    *   Examples:
        *   Integers + Boolean (`True` becomes `1`).
        *   Integers + String (all elements become strings).
    *   Arrays **do not have column names** like Pandas DataFrames.
*   **Conditional Element Manipulation (`np.where()`):**
    *   Using the powerful `np.where(condition, value_if_true, value_if_false)` function to efficiently modify array elements based on a condition.
    *   Example: Replacing all even numbers in an array with zeros (`np.where(array % 2 == 0, 0, array)`).
*   **NumPy for Image Data:**
    *   Understanding how **RGB image data** can be represented as a 3D NumPy array (Height x Width x Color Channels).
    *   Loading image data stored in `.npy` format using `np.load()`.
    *   Visualizing image arrays using `matplotlib.pyplot.imshow()`.
*   **Image Manipulation with `np.where()`:**
    *   **Case Study (DataCamp Logo):**
        *   Loaded a pre-existing NumPy array (`black_logo`) representing a green DataCamp logo on a black background.
        *   Changed black background to white: `np.where(black_logo == 0, 255, black_logo)` (assuming black is `[0,0,0]` and white is `[255,255,255]`).
        *   Changed green logo to pink on black background: `np.where(black_logo != [0,0,0], [255,110,169], black_logo)` (replacing non-black pixels with pink).

---

## 🛠️ Tech Stack & Core NumPy Functions

*   **Core Library:** NumPy (`import numpy as np`)
*   **Visualization:** Matplotlib (`matplotlib.pyplot as plt`)
*   **Key NumPy Functions & Methods:**
    *   `np.array()`: Create an array.
    *   `np.arange()`: Create an array with a range of values.
    *   `.reshape()`: Change the shape (dimensions) of an array.
    *   `np.where()`: Conditional element selection/replacement.
    *   `np.load()`: Load arrays from `.npy` files.
*   **Python Data Structures:** Lists, Tuples (used for creating arrays).
*   **Development Environment:** Jupyter Notebook (`solution.ipynb`).

---

## 🗺️ The Learning Workflow: Exploring NumPy Step-by-Step

The project (`solution.ipynb`) guides through NumPy fundamentals progressively:

1.  **Array Creation Fundamentals:**
    *   Creating 1D and 2D arrays directly from Python lists.
    *   Generating 1D arrays using `np.arange()`.

2.  **Understanding Dimensions & Reshaping:**
    *   Reshaping a 1D array (`array_from_arange`) into an 8x2 (2D) array.
    *   Further reshaping into a 4x2x2 (3D) array, conceptualized as a list of four 2x2 matrices.

![image](https://github.com/user-attachments/assets/fd47a4d8-3917-44bf-9f5e-e3b0ca5f8043)

*Fig 2: A 1D array of 16 elements reshaped into a 3D array (4x2x2).*

3.  **Type Coercion in Action:**
    *   Demonstrating how NumPy coerces mixed-type lists into single-type arrays.
        *   `[[1, 2, 3], [4, 5, True]]` results in `[[1, 2, 3], [4, 5, 1]]` (boolean to integer).
        *   `[[1, 2, 3], [4, 5, "Hello world!"]]` results in all elements becoming strings.

4.  **Practical Power: `np.where()`:**
    *   Introducing the `np.where()` syntax and its utility.
    *   Conditionally replacing even numbers in a sample array with `0` while keeping odd numbers as they are.

5.  **Case Study: RGB Image Manipulation 🖼️**
    *   **Conceptual RGB:** Explained how RGB colors are formed and can be represented in a 3D NumPy array (height, width, 3 color channels).
    *   **Visualizing a Simple RGB Array:** Manually created a small 3x3x3 array (`rgb_example`) and used `plt.imshow()` to visualize the resulting 3x3 colored image.

![image](https://github.com/user-attachments/assets/967d7005-5671-4fc3-b3ec-8acb9817952e)

*Fig 3: A 3x3 image generated by `plt.imshow()` from a 3x3x3 NumPy array defining RGB pixel values.*

  *   **Loading Real Image Data:** Loaded the DataCamp logo array (`dc_logo_rgb_array.npy`) using `np.load()`.
    *   **Manipulating the Logo:**
        *   **Black to White Background:** Used `np.where(black_logo == 0, 255, black_logo)` to change all black pixels (value 0) to white (value 255) across all channels, effectively inverting the background for the green logo.
        *   **Green to Pink Logo:** Used `np.where(black_logo != [0,0,0], [255,110,169], black_logo)` to change all non-black pixels (the green logo parts) to a specific pink RGB value, keeping the black background.

![image](https://github.com/user-attachments/assets/77088e84-23d8-4594-a7b8-832433a4aebd)

*Fig 4: The original DataCamp logo visualized from `black_logo` array*

![image](https://github.com/user-attachments/assets/85a5bc07-db29-4f5f-b777-330e8fee588a)

*Fig 5: Modified logo with a white background and green logo, after `np.where(black_logo == 0, 255, black_logo)`*

![image](https://github.com/user-attachments/assets/df127069-c24c-42b1-885d-df815e5fa65b)

*Fig 6: Modified logo with a pink logo on a black background, after `np.where(black_logo != [0,0,0], [255,110,169], black_logo)`*

---

## 💡 Key Benefits of NumPy & Why This Matters

*   **Efficiency:** NumPy arrays are more memory-efficient and provide faster numerical operations compared to standard Python lists, especially for large datasets.
*   **Foundation for Data Science:** Libraries like Pandas, Scikit-learn, SciPy, and even deep learning frameworks (TensorFlow, PyTorch) are built on or integrate deeply with NumPy. Understanding NumPy is crucial for advanced data science.
*   **Powerful Array Operations:** Provides a vast suite of functions for linear algebra, Fourier transforms, random number capabilities, and more.
*   **Vectorization:** Enables writing concise and fast code by applying operations to entire arrays rather than looping through elements (e.g., `array % 2 == 0` in `np.where`).
*   **Broad Applicability:** Essential for scientific computing, data analysis, machine learning, image processing, signal processing, and many other fields.

---

*Day 98 of #100DaysOfDataScience served as a foundational dive into NumPy, showcasing its core array object, powerful manipulation capabilities like `np.where()`, and practical application in image data processing. A crucial building block for any data scientist! - Vatsal Parikh*
