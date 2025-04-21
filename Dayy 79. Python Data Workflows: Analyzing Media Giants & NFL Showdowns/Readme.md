# Day 79. 100 Days of Data Science Challenge - 04/20/2025

## 🐍 Python Data Workflows: Analyzing Media Giants & NFL Showdowns 🏈

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Wrangling-yellowgreen?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML_Parsing-orange?style=flat-square)](https://www.crummy.com/software/BeautifulSoup/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-blueviolet?style=flat-square)](https://matplotlib.org/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_79-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

## 🎯 Project Goal: Mastering Core Data Analysis Pipelines

Welcome to Day 79 of my #100DaysOfDataScience challenge! This project showcases two fundamental data analysis workflows using **Python**, tackling common real-world scenarios:

1.  **Excel Analysis:** Importing, analyzing, and exporting data about the **Highest Grossing Media Franchises** from an Excel spreadsheet (`.xlsx`).
2.  **Web Scraping & Cleaning:** Extracting structured data (NFL Week 8 scores) from a complex **HTML web page**, cleaning it, and performing basic analysis.

The focus is on demonstrating proficiency with core Python libraries like **Pandas** and **BeautifulSoup** to handle different data sources, perform essential transformations, and extract meaningful insights – skills vital for any data professional.

---

## ✨ What We Accomplished: Key Features & Skills

*   **Multi-Source Data Handling:** Processed data from both structured Excel files and semi-structured HTML.
*   **Excel File I/O:** Read data from specific sheets (`pd.read_excel`), including handling metadata rows (`skiprows`).
*   **Pandas Analysis:** Performed common data analysis tasks:
    *   Finding maximum values (`.max()`, `.idxmax()`).
    *   Counting occurrences (`.value_counts()`).
    *   Grouping and aggregating (`.groupby()`, `.mean()`).
    *   Filtering dataframes based on conditions (`df[df['column'] == value]`).
*   **Data Export:** Saved processed data to a CSV file (`.to_csv(index=False)`).
*   **Web Scraping:** Parsed complex HTML structure using **BeautifulSoup** (`select`, `find`, `find_all`, `.get_text()`).
*   **Data Extraction from HTML:** Navigated nested tags and extracted specific text and attribute values.
*   **Robust Data Cleaning:** Handled messy text data scraped from the web using string methods (`.splitlines()`) and regular expressions (`re.sub`) for consistent formatting.
*   **String Manipulation:** Split combined strings into multiple columns (`.str.split(expand=True)`).
*   **Basic Plotting:** Generated static bar charts using **Matplotlib** (after noting limitations with interactive plots like Plotly in certain environments).

---

## 🛠️ Tech Stack: The Tools for the Job

*   **Core Language:** Python 3.8+
*   **Data Manipulation & Analysis:** Pandas
*   **HTML Parsing:** BeautifulSoup4 (`bs4`)
*   **String Cleaning:** `re` (Regular Expressions)
*   **Plotting:** Matplotlib (`pyplot`) (also explored Plotly Express `px` conceptually)
*   **Environment:** Jupyter Notebook (`solution.ipynb`)
*   **Display:** `IPython.display` (`display`, `HTML`) for notebook rendering.

---

## 🗺️ The Project Journey: Two Data Adventures

This project involved two distinct mini-workflows:

### Part 1: Conquering the Media Franchise Excel 💰 (`Highest-Grossing-Media-Franchises.xlsx`)

*   **Objective:** Analyze revenue, ownership, and origins of top media franchises.
*   **Process:**
    1.  **Load:** Read both the `data` sheet and the `data dictionary` sheet using `pd.read_excel`, using `skiprows=2` for the dictionary to ignore header info.
    2.  **Analyze:** Used Pandas to answer key questions:
        *   Identified **Pokémon** as the highest revenue franchise ($88.0B).
        *   Found **The Walt Disney Company** owns the most franchises in this dataset (4).
        *   Calculated the mean revenue grouped by the `original_medium` (e.g., Video Games average $88B, Movies average ~$46B).
    3.  **Filter & Export:** Created a subset DataFrame containing only franchises owned by 'The Walt Disney Company' and saved it as `walt-disney-franchises.csv`.
    4.  **Visualize (Attempt & Pivot):** Attempted a Plotly Express bar chart (`px.bar`), noted potential display issues in some environments, then successfully generated a similar static chart using Matplotlib (`plt.bar`).


### Part 2: Scraping the Gridiron - NFL Scores 🏈 (`Latest-NFL-Scores-Pro-Football-Reference.com.html`)

*   **Objective:** Extract structured game results and key player stats from a notoriously tricky-to-scrape HTML page.
*   **Challenge:** The webpage uses multiple nested tables within divs for each game, lacking easily selectable classes for all desired data points.
*   **Process:**
    1.  **Parse HTML:** Loaded the saved HTML file and parsed it with `BeautifulSoup(..., 'html.parser')`.
    2.  **Select Game Summaries:** Used CSS selectors (`soup.select('#content .game_summaries .game_summary')`) to isolate each game's container.
    3.  **Iterate & Extract:** Looped through each game summary:
        *   Checked game status; skipped "Preview" games.
        *   Navigated nested `<table>` elements (`.find('table', class_='teams')`, `.find('table', class_='stats')`) to find specific data.
        *   Extracted game date, winning/losing teams and scores by finding specific table rows (`<tr>`) and cells (`<td>`), using `.get_text(strip=True)`.
        *   Extracted key player stats (PassYds, RushYds, RecYds) by iterating through the stats table rows, identifying the label (`<strong>`), player name (`<a>['title']`), and value (`.find('td', class_='right')`).
    4.  **Structure Data:** Appended extracted data for each game as a dictionary to a list (`records`).
    5.  **Create DataFrame:** Converted the list of dictionaries into a Pandas DataFrame (`pd.DataFrame(records)`).
    6.  **Cleanse the Data:** Addressed data quality issues revealed during analysis:
        *   Cleaned team names containing extra characters (like scores or newlines) using a function with `.splitlines()[0]` and `re.sub(r'[^A-Za-z0-9\s]+', '', name)`.
        *   Split combined player/team code strings (e.g., "Allen-BUF") into separate `_surname` and `_team_code` columns using `.str.split('-', n=1, expand=True)`.
        *   *Mapped* the extracted team code (or player surname in the provided solution's intermediate step) back to the full `winning_team` name (a simplification shown in the notebook - a more robust solution would use a proper mapping dictionary).
    7.  **Analyze:** Answered questions about the scraped data:
        *   Calculated point difference (`winning_score - losing_score`) to find the largest margin (Dallas Cowboys by 23).
        *   Found the top receiver (CeeDee Lamb - DAL).
        *   Calculated the average losing score (~17.6).


---
*Day 79 of #100DaysOfDataScience showcases foundational Python data analysis workflows, tackling both clean spreadsheet data and challenging web scraping scenarios. Practice makes perfect! - Vatsal Parikh*
