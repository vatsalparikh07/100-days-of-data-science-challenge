# Data Wrangling in Julia : Analyzing Student Records 🎓📈

[![Julia](https://img.shields.io/badge/Julia-1.8.2+-blue?logo=julia&style=flat-square)](https://julialang.org/)
[![DataFrames.jl](https://img.shields.io/badge/DataFrames.jl-Core_Package-yellowgreen?style=flat-square)](https://dataframes.juliadata.org/stable/)
[![CSV.jl](https://img.shields.io/badge/CSV.jl-Data_Loading-orange?style=flat-square)](https://csv.juliadata.org/stable/)
[![PlotlyLight](https://img.shields.io/badge/PlotlyLight-Visualization-blueviolet?style=flat-square)](https://github.com/JuliaPlots/PlotlyLight.jl)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_83-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Mastering Data Manipulation with Julia

Welcome to Day 83 of my #100DaysOfDataScience challenge! Today, we explore the **Julia programming language** for data science, specifically focusing on its powerful **data wrangling capabilities** using the `DataFrames.jl` ecosystem. This project demonstrates how to perform common tasks like loading, cleaning, transforming, filtering, grouping, and summarizing data – skills directly transferable from environments like R's `dplyr` or Python's `pandas`, but leveraging Julia's unique features.

**The Mission:**
*   Process mock student enrollment and grade data, initially from inline strings and later from a larger downloaded CSV file.
*   Calculate key metrics like GPA and semesters attended per student.
*   Explore data distributions using filtering and contingency tables.
*   Showcase Julia's syntax, type system, multiple dispatch concepts, and performance potential in a practical data analysis context.

**Why Julia for Data Wrangling?**
*   **Performance:** Julia is designed for high performance, often matching C/Fortran speeds, potentially avoiding the "two-language problem".
*   **Expressive Syntax:** Combines familiar elements from R, Python, Matlab, and Lisp.
*   **Powerful Metaprogramming:** Enables libraries like `DataFrames.jl` to offer concise mini-languages and macros (`@chain`).
*   **Multiple Dispatch:** A different paradigm than object-orientation, allowing functions to specialize based on the *types* of multiple arguments.
*   **Growing Ecosystem:** Strong packages for data science (`DataFrames.jl`, `CSV.jl`, `StatsBase`, `FreqTables.jl`), numerical computing (`SciML`), and visualization.

---

## 🛠️ Tech Stack & Core Concepts

*   **Core Language:** Julia (v1.8.2+ used here)
*   **Data Structures:**
    *   `DataFrames.jl`: The primary tool for tabular data (`DataFrame`).
    *   Julia Base Types: `Int64`, `Float64`, `String`, `Symbol`, `Missing`, `Vector`, `Matrix`, `NamedTuple`, `Dict`.
*   **Data Loading:** `CSV.jl` (`CSV.read`).
*   **Data Manipulation:**
    *   `DataFrames.jl`: `select`, `filter`, `transform`/`transform!`, `combine`, `groupby`, `subset`, `vcat`, `unique`, `names`, `nrow`.
    *   **Mini-Language:** Using the `source => function => destination` syntax within `combine`, `transform`, etc. (e.g., `:Grade => gpa => :gpa`).
    *   `Chain.jl`: `@chain` macro for readable, sequential data transformations (piping).
*   **Analysis & Statistics:**
    *   `Statistics.jl`: `mean`.
    *   `FreqTables.jl`: `freqtable` for creating contingency tables.
    *   `CategoricalArrays.jl`: `cut` for binning numerical data into categories.
*   **Helper Functions:** Custom Julia functions (`grade_to_number`, `gpa`, `summarize_student`, `decode_semester`, `start_semester`) leveraging conditional logic, handling `missing` values (`ismissing`, `skipmissing`), and broadcasting (`.`).
*   **Visualization:** `PlotlyLight.jl` (a lightweight interface to PlotlyJS) for creating scatter plots.
*   **Environment:** Jupyter Notebook (`solution.ipynb`).

---

## 🗺️ The Analytical Workflow: From Raw Data to Insights

This project follows a typical data wrangling pipeline, executed within a Jupyter Notebook using Julia:

1.  **Setup & Data Loading:**
    *   Import necessary packages (`using CSV, DataFrames, Statistics, Chain, FreqTables, PlotlyLight, CategoricalArrays`).
    *   Load initial small dataset (`s11_data`) from a multi-line string using `CSV.read(IOBuffer(...), DataFrame)`.
    *   Load subsequent semester data (`f22_data`) similarly.
    *   Load a larger dataset (`d.csv`) from a URL using `CSV.read(download(url), DataFrame)`.

2.  **Basic Exploration & Access:**
    *   Inspecting data structure (`names`, `first`).
    *   Accessing data by row/column index (`df[row, col]`), column name (`df[row, :col_symbol]` or `df[!, :col_symbol]` for view/modification), or boolean indexing (`df[df.Name .== "...", :]`). Note the broadcasting `.` needed for element-wise comparison.

3.  **Combining Data:**
    *   Identifying common column names between datasets (`names(...) ∩ names(...)`).
    *   Vertically concatenating DataFrames using `vcat`, selecting only common columns (`df[:, common_names]`). Used `unique` on the newer data to handle duplicated rows resulting from class meeting schedules.

4.  **Split-Apply-Combine Strategy:**
    *   **Goal:** Calculate summary statistics (first term, last term, number of courses, GPA) for each unique student (`ID`).
    *   **Helper Functions:** Defined `grade_to_number` (mapping letter grades to points, handling `W` and `missing`), `gpa` (calculating mean grade points, carefully handling `missing` and empty lists using `skipmissing`), and `summarize_student` (applying `extrema` to `Term` and `gpa` function to `Grade`).
    *   **Grouping:** Used `groupby(studs, :ID)` to create a `GroupedDataFrame`.
    *   **Applying:** Applied `summarize_student` to each group using a comprehension `[summarize_student(student) for student in students]`.
    *   **Combining:** Converted the resulting array of `NamedTuple`s back into a `DataFrame`.
    *   **Mini-Language Alternative:** Demonstrated the more concise `combine(groupby(...), :SourceCol => function => :DestCol ...)` syntax for the same result.

5.  **Feature Engineering & Transformation:**
    *   Calculated `semesters` attended by decoding the custom `Term` format (`decode_semester` function) and applying the calculation using `transform!` with `ByRow` (or using broadcasting `.`) on the `:F` (first term) and `:L` (last term) columns.
    *   Created a categorical `status` column ('lo', 'medium', 'hi') based on GPA using `transform!` and `CategoricalArrays.cut`.

6.  **Filtering & Counting:**
    *   Filtered rows based on conditions using `filter(:Col => condition_function, df)` or `filter(row -> condition(row.Col), df)`. Demonstrated filtering by start term (`F`) and GPA.
    *   Calculated counts of students per semester or number of courses using `combine(groupby(...), nrow => :n)`.
    *   Created contingency tables using `FreqTables.freqtable(df.Col1, df.Col2)` to analyze relationships between categorical variables (e.g., starting term vs. semesters attended, starting term vs. GPA status).

7.  **Piping with `@chain`:**
    *   Introduced the `@chain` macro from `Chain.jl` to make multi-step data transformations more readable by implicitly passing the result of one line as the first argument (or specified by `_`) to the next line. Showcased converting nested filter/freqtable calls into a cleaner chain.

8.  **Visualization:**
    *   Used `PlotlyLight.jl` to generate a scatter plot (`Config(type="scatter", mode="lines+markers")`) visualizing the proportion of students remaining after each semester, faceted by their starting term (`F`). Demonstrated creating plot data within a loop over grouped data.

![Student Retention Plot](https://cdn.mathpix.com/cropped/2025_04_24_96fe9e8d33368da9a7ebg-27.jpg?height=490&width=1271&top_left_y=92&top_left_x=301)
*Plot showing retention curves for different starting cohorts.*

---

## 💡 Key Learnings & Julia Nuances

*   **`DataFrames.jl` Power:** It provides a robust and expressive API for common data manipulation tasks, feeling familiar to users of `pandas` or `dplyr`.
*   **Handling `missing`:** Explicitly handling `missing` values (Julia's equivalent of `NA` or `None` in this context) is crucial, often using functions like `ismissing` and `skipmissing`.
*   **Broadcasting (`.`):** Essential for applying functions element-wise to vectors or DataFrame columns (e.g., `grade_to_number.(grades)` vs `grade_to_number(grades)`).
*   **Mini-Language vs. Functions:** `DataFrames.jl` offers both concise mini-language syntax (`:Col => fun => :NewCol`) and the flexibility of passing custom functions, including anonymous ones (`row -> ...`).
*   **Piping (`@chain`):** Significantly improves readability for sequential transformations compared to nested function calls.
*   **Performance Potential:** While not benchmarked here, Julia's compiled nature promises significant speed advantages for computationally intensive tasks compared to standard Python/R interpreters.
*   **Types & Dispatch:** Though less visible in this specific workflow, Julia's strong type system and multiple dispatch underpin the design and performance of its libraries.

---

*Day 83 of #100DaysOfDataScience successfully navigated data wrangling challenges using Julia and `DataFrames.jl`. It's a powerful combination offering performance and expressive syntax for data analysis! - Vatsal Parikh*

