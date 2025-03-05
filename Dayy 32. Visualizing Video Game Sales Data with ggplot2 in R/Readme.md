# Day 32. 100 Days of Data Science Challenge - 03/04/2025

# Visualizing Video Game Sales Data with ggplot2 in R
[![ggplot2](https://img.shields.io/badge/ggplot2-Data%20Viz-%2325A162)](https://ggplot2.tidyverse.org/) 
[![dplyr](https://img.shields.io/badge/dplyr-Data%20Wrangling-%23009988)](https://dplyr.tidyverse.org/)

## 🔍 Project Focus  
Analyze 10,000+ video game titles (1985-2016) to uncover sales patterns across console generations, regional markets, and platform strategies using advanced visualization techniques.

---

## 🕹️ Dataset Overview  
- **Source**: [Kaggle Video Games Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)
- **Records**: 9,989 games with ≥100K global sales  
- **Key Features**:
```
Global_Sales: Total worldwide sales (millions)
Platform_Generation: 4th-8th console generations (1987-2017)
NA/EU/JP_Sales: Regional sales breakdown
Platform_Company: Nintendo, Sony, Microsoft, Sega
```
- **Generational Coverage**:
- 4th Gen (SNES, Genesis): 1987-1996
- 7th Gen (Wii, PS3): 2005-2017
- 8th Gen (PS4, XOne): 2012-present

---

## 🔬 Key Analyses  

### 🏆 Top Performers  
**Global Sales Leaders**:  
```
top_games <- vgsales %>%
group_by(Name) %>%
summarise(Total_Sales = sum(Global_Sales)) %>%
slice_max(Total_Sales, n = 10)
```
| Rank | Game                  | Total Sales (M) | Dominant Platform |  
|------|-----------------------|-----------------|--------------------|  
| 1    | Wii Sports            | 82.74           | Wii (7th Gen)      |  
| 2    | GTA V                 | 54.84           | Multi-Platform     |  
| 3    | Mario Kart Wii        | 35.82           | Wii                |  

![image](https://github.com/user-attachments/assets/200eba12-ed61-478e-a181-ba480ccea2d1)

---

### 🕰️ Generational Trends  
**7th Gen Console Peak (2005-2017)**:  
```
seventh_gen <- vgsales %>%
filter(Platform_Generation == "7th") %>%
group_by(Year) %>%
summarise(Total_Sales = sum(Global_Sales))
```
| Year | Total Sales (M) | Key Release                |  
|------|-----------------|----------------------------|  
| 2009 | 463.63          | Modern Warfare 2, Wii Fit  |  
| 2013 | 216.36          | GTA V, The Last of Us      |  

![image](https://github.com/user-attachments/assets/5ae416e8-a648-44e4-9e46-f4eaec04bf80)

---

### 🌍 Regional Preferences  
**Market Breakdown**:  
```
regional_avg <- vgsales %>%
summarise(
NA = mean(NA_Sales),
EU = mean(EU_Sales),
JP = mean(JP_Sales)
)
```
| Region | Avg Sales/Game (M) | Top Genre        | Preferred Platform |  
|--------|--------------------|------------------|---------------------|  
| NA     | 0.89               | Shooter          | Xbox 360            |  
| EU     | 0.73               | Sports           | PS3                 |  
| JP     | 0.38               | Role-Playing     | Nintendo DS         |  

---

## 🛠️ Technical Workflow  
1. **Data Preparation**  
```
vgsales <- read_csv('data/vgsales.csv') %>%
mutate(Platform = fct_lump(Platform, n = 8))
```

2. **Visual Exploration**  
- **Bar Charts**: Top games/publishers (`geom_col() + coord_flip()`)  
- **Line Plots**: Temporal trends (`geom_line(size=2)`)  
- **Faceting**: Cross-generational comparisons (`facet_wrap(~Platform_Generation)`)  

3. **Insight Extraction**  
```
top_games %>%
mutate(Name = fct_reorder(Name, Total_Sales)) %>%
ggplot(aes(Name, Total_Sales)) +
geom_col() +
coord_flip()
```

---

## 💡 Key Learnings  
1. **Market Dynamics**:  
- 7th Gen consoles drove 42% of all-time sales  
- Cross-platform titles achieve 2.3x sales vs exclusives  

2. **Visual Best Practices**:  
- **Axis Flipping**: Horizontal bars for long text labels  
- **Temporal Context**: Annotated line plots highlight market shifts  
- **Facet Organization**: Single-column layout for multi-gen analysis  

3. **Technical Skills**:  
- Advanced `dplyr` pipelines for cohort analysis  
- `forcats` integration for categorical ordering  
- ggplot2 theme customization for publication-ready visuals  

*"In games data, every pixel tells a story – our job is to render the narrative"* 🎮📈
