## Visualizing Communication Patterns: Cell Phone Metadata Analysis in Tableau 📱

[![Tableau Public](https://img.shields.io/badge/Tool-Tableau_Public-blue?logo=tableau&style=flat-square)](https://public.tableau.com/)
[![Data Source](https://img.shields.io/badge/Data-CSV_Metadata-orange?style=flat-square)](./will-ockenden-metadata.csv) <!-- Assuming data file is local -->
[![Visualization](https://img.shields.io/badge/Focus-Data_Visualization-blueviolet?style=flat-square)](https://en.wikipedia.org/wiki/Data_visualization)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_91-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

![Screenshot 2025-05-02 221652](https://github.com/user-attachments/assets/696e4aa7-dd53-4fd6-8cff-212cc26b6064)
*Fig 1: Overview of the Tableau dashboard visualizing cell phone activity patterns.*

## 🎯 Project Goal: Illuminating Insights from Mobile Metadata with Tableau

Welcome to Day 91 of my #100DaysOfDataScience journey! Today's focus shifts to the art and science of **Data Visualization** using **Tableau Public**. This project takes anonymized cell phone communication metadata (`will-ockenden-metadata.csv`) and transforms it into an interactive dashboard, revealing patterns in usage, location, and communication frequency.

**The Mission:**
*   Leverage Tableau's capabilities to explore and visualize large amounts of timestamped, geolocated communication logs.
*   Identify key trends in communication activity based on time (hour, day of week, overall timeline), location, and communication type.
*   Analyze patterns related to communication partners (represented by identifiers).
*   Demonstrate the power of interactive dashboards for slicing, dicing, and understanding complex datasets without coding.

This project showcases how visual analytics can quickly surface insights from potentially overwhelming log data, providing a clear picture of usage patterns.

**✨ Explore the Live Interactive Dashboard! ✨**
**[➡️ Click Here to Launch on Tableau Public](https://public.tableau.com/views/ExploringCellPhoneData/DataGap)**

---

## 🤔 Key Questions Explored via Visualization

The dashboard is designed to answer fundamental questions about the communication patterns within the dataset:

*   **Temporal Peaks:** When is communication activity (Internet, Phone, SMS) highest during the day and across the week?
*   **Dominant Channels:** Which communication type (Internet, Phone, SMS) is used most frequently overall?
*   **Geographic Hotspots:** Where is the communication activity geographically concentrated? Which state/areas see the most records?
*   **Communication Network:** Who (represented by `Comm Identifier`) is being communicated with most frequently via Phone or SMS? Are there patterns in *when* certain identifiers are contacted?
*   **Long-Term Trends:** How does the volume of communication records change over the entire period covered by the data?

---

## 🗺️ The Data Landscape: Cell Phone Metadata (`will-ockenden-metadata.csv`)

Our dataset represents anonymized logs of cell phone activity. Key fields used in the analysis include:

*   `Comm Timedate String`: Timestamp for each communication record. Used for timeline, hour-of-day, and day-of-week analysis.
*   `latitude`, `longitude`: Geographic coordinates associated with the record (likely cell tower location).
*   `Cell Tower State`: The state where the activity was logged (e.g., NSW).
*   `Comm Type`: The type of communication (Internet, Phone, SMS).
*   `Comm Identifier`: An anonymized identifier representing the other party in Phone/SMS communications.
*   *(Other fields like User ID, Cell Tower ID, Date parts etc. are present but implicitly used)*

---

## 📊 Dashboard Features & Visualizations

The Tableau dashboard ([linked above](https://public.tableau.com/views/ExploringCellPhoneData/DataGap)) comprises several interactive views:

1.  **Main Activity Dashboard (Fig 1):**
    *   **Cell Tower Locations (Map):** Plots record locations, showing geographic density. Size of circles likely represents the number of records. Clearly shows concentration around Sydney.
    *   **Activity by Day of Week (Bar Chart):** Displays the total number of records for each day (Monday-Sunday), segmented by `Comm Type` (color-coded). Internet usage appears relatively consistent, while Phone/SMS might show slight variations.
    *   **Activity by Hour of Day (Bar Chart):** Shows record volume for each hour (0-23), also segmented by `Comm Type`. Reveals peak usage times, often in the afternoon and evening for Internet activity.
    *   **Timeline (Line Chart):** Plots the number of records over the entire date range of the dataset, highlighting periods of high/low activity or potential data gaps. Shows significant spikes around Dec '14 - Feb '15.

2.  **Communication Partner Analysis (Fig 2):**
    *   **"Who is Will communicating with?" (Bar Chart):** This unique view plots `Comm Identifier` on the y-axis and shows the number of records (count) across the days of the week (faceted columns). Bars are colored by `Comm Type` (Phone/SMS). This effectively highlights the most frequent contacts and potentially reveals weekly communication patterns with specific identifiers.

![Screenshot 2025-05-02 221703](https://github.com/user-attachments/assets/99c15268-34e0-4bad-9185-b8b3e6b4c659)
*Fig 2: Analyzing frequency and timing of communications with specific identifiers.*

3.  **Geographic Focus (Fig 3):**
    *   **"Activity by State" (Map):** A chloropleth map clearly showing the overwhelming dominance of activity within **NSW (New South Wales)**, accounting for ~71.76% of the records, compared to much smaller percentages in Victoria and Tasmania.

![Screenshot 2025-05-02 221555](https://github.com/user-attachments/assets/250620f1-4952-4f46-94c2-2edaa2dd5bfa)
*Fig 3: Geographic distribution highlighting NSW as the primary location.*

*(Note: Other tabs like "Data Gap", "Comms Type", etc., might exist in the live dashboard offering further specific views).*

---

## 💡 Key Insights Gleaned from the Dashboard

Visualizing this data in Tableau rapidly surfaces several key patterns:

*   **Internet Dominance:** The 'Internet' `Comm Type` constitutes the vast majority of records across most time periods. Phone and SMS usage is comparatively low in this dataset.
*   **Peak Hours:** Activity, primarily driven by Internet usage, tends to peak in the **afternoon and evening hours** (roughly 15:00 - 21:00). There's a noticeable dip during typical nighttime sleeping hours.
*   **Weekly Rhythm:** While Internet usage seems relatively stable across the week, there might be subtle variations. Weekend activity doesn't show a dramatic drop compared to weekdays in the overall record count.
*   **Geographic Concentration:** The activity is overwhelmingly concentrated in **NSW**, particularly in urban areas like **Sydney**, as seen on the location map.
*   **Key Communicators:** The "Who is Will communicating with?" chart allows for quick identification of the most frequently contacted identifiers via Phone/SMS and potential patterns (e.g., certain contacts primarily reached on weekdays vs. weekends).
*   **Temporal Spikes:** The timeline reveals specific periods (late 2014 / early 2015) with significantly higher activity than others, warranting further investigation if this were a real analysis.

---

## 🛠️ Tech Stack & Concepts Applied

*   **Core Tool:** **Tableau Public** (Desktop for building, Public for hosting/sharing).
*   **Data Source:** CSV file (`will-ockenden-metadata.csv`).
*   **Key Tableau Features Used:**
    *   Connecting to Text Files.
    *   Calculated Fields (for extracting date parts like Hour, Day).
    *   Geographic Roles (State, potentially Lat/Lon for maps).
    *   Chart Types: Bar Charts, Line Charts, Maps (Symbol Map, Chloropleth Map).
    *   Marks Card: Color, Size, Tooltip customization.
    *   Filters & Interactivity (implied by dashboard structure).
    *   Dashboards: Combining multiple worksheets into a cohesive view.
*   **Analytical Concepts:** Temporal Analysis, Frequency Analysis, Geospatial Visualization, Categorical Analysis.

---

## 🚀 Potential Next Steps & Further Analysis

This dashboard provides a great foundation. Further exploration could involve:

*   **Adding Interactivity:** Implementing more filters, parameters, and dashboard actions to allow deeper user-driven exploration (e.g., filter by Comm Identifier, select date ranges).
*   **Calculating Metrics:** Creating calculated fields for things like session duration (if start/end times were available), average time between communications, etc.
*   **Advanced Mapping:** Using density maps or analyzing proximity to specific points of interest.
*   **Statistical Analysis:** Integrating statistical functions or trend lines within Tableau.
*   **Network Graph (External Tool):** Exporting communication pairs (`User ID` to `Comm Identifier`) to visualize the communication network using tools like Gephi or Python libraries (NetworkX).

---

*Day 91 of #100DaysOfDataScience focused on harnessing the power of Tableau Public for visual exploration of cell phone metadata. A clear demonstration of how visualization transforms raw logs into understandable patterns! - Vatsal Parikh*
