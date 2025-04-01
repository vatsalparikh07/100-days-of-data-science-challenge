# Day 60. 100 Days of Data Science Challenge - 04/01/2025

## Black Myth: Wukong YouTube Comment Analysis

## Project Overview

This project explores the YouTube discourse surrounding the game *Black Myth: Wukong*. By analyzing user-generated comments, we uncover key themes, sentiment patterns, and community dynamics. Using advanced text analysis, network visualization, and semantic clustering, we provide actionable insights into how players and fans engage with the game.

---

## Technologies and Tools

This project employs a combination of tools and technologies for data analysis, visualization, and sentiment extraction:

- **Microsoft Excel**: For initial data cleaning and structuring.
- **Python**: Used for advanced data processing, tokenization, and sentiment analysis.
  - Libraries: `pandas`, `matplotlib`, `nltk`
- **NodeXL**: For network visualization and semantic tree generation.
- **Word Cloud Generators**: To highlight the most frequently used terms in the dataset.
- **Visualization Tools**: To create semantic trees and word-pair networks.

---

## Dataset Overview

The dataset consists of YouTube comments extracted from videos related to *Black Myth: Wukong*. It includes:
- **Edges Worksheet**: 23,257 records representing relationships between users or terms.
- **Vertices Worksheet**: 411 records representing individual nodes (e.g., commenters or words).

### Data Cleaning Process
- Removed non-English content (~34.6% of original dataset).
- Eliminated rows with non-alphabetic characters or special symbols.
- Final clean dataset: **15,191 records**.

---

## Key Findings

### Word Cloud Insights
A word cloud generated from the cleaned dataset highlights the most frequently discussed topics:
- **Prominent Terms**:
  - *game*: 2,359 occurrences
  - *wukong*: 1,502 occurrences
  - *chapter*: 1,265 occurrences
  - *boss*: 948 occurrences
- **Themes**:
  - Gameplay mechanics dominate discussions (e.g., boss fights and chapters).
  - Positive engagement is evident through terms like "thanks" and "appreciate."

### Sentiment Analysis
- **Positive Sentiment**: 9,171 words (3.6%)
- **Negative Sentiment**: 7,028 words (2.7%)
- The overall sentiment leans slightly positive, reflecting excitement about gameplay mechanics and appreciation for content creators.

---

## Network Visualizations

### Semantic Tree 

![Semantic Tree](https://github.com/user-attachments/assets/9adaad1c-c20b-4819-aa85-4f0b54cd8c60)

### Semantic Tree (Word Pair Count >10)

![Semantic Tree](https://pplx-res.cloudinary.com/image/upload/v1743525844/user_uploads/RdjbdaHnhodACgk/Semantic-Tree-WP-10.jpg)

This semantic tree groups related terms into clusters:
1. **G1 (Dark Blue)**: Focus on Chinese mythology and gameplay elements.
2. **G2 (Light Blue)**: Discussions about boss fights and game progression.
3. **G3 & G4 (Green)**: Conversations about monsters and mythology.
4. **G5 (Red)**: Community-focused terms like "thanks" and "commenting."

### Word-Pair Network Visualization

![Word Pair Network](https://pplx-res.cloudinary.com/image/upload/v1743525844/user_uploads/OiSLvKghSBTSEJo/Word-Pair-Network.jpg)

This network highlights relationships between key terms:
- Central nodes include "game," "bosses," "wukong," and "chapter."
- Dense connections show frequent co-occurrence of gameplay-related terms.

---

## Five Key Insights

1. **Gameplay Mechanics Are Central**  
   Discussions heavily revolve around gameplay elements such as boss fights, chapters, and combat strategies.

2. **Cultural Appreciation**  
   Players frequently reference Chinese mythology, indicating a strong interest in the game's cultural roots.

3. **Community Engagement**  
   Terms like "thanks" and "commenting" highlight active community interactions.

4. **Combat Strategy Focus**  
   Many conversations center on overcoming challenging bosses and sharing tactics.

5. **Narrative Integration**  
   Players connect narrative elements (e.g., Sun Wukong) with gameplay discussions, showing an appreciation for the game's storytelling.

---

## Repository Contents

### Files
1. `solution.docx`: Detailed methodology and analysis findings.
2. `Word-Pairs.xlsx`: Processed word-pair data for network visualizations.
3. `Semantic-Tree-WP-10.jpg`: Visualization of word relationships with pair counts >10.
4. `Word-Pair-Network.jpg`: Network visualization showing thematic connections between terms.


---

## Conclusion

The analysis reveals a highly engaged gaming community passionate about *Black Myth: Wukong*. Discussions are dominated by gameplay mechanics, cultural appreciation of Chinese mythology, and strong community interactions. These insights can inform content creation strategies or community engagement initiatives for similar projects.
