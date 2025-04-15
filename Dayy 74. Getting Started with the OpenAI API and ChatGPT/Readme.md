# Day 74. 100 Days of Data Science Challenge - 04/15/2025

# 🤖 Talking to ChatGPT with Code - OpenAI API Mastery 🐍

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org)
[![OpenAI API](https://img.shields.io/badge/OpenAI-API_Used-brightgreen?logo=openai&style=flat-square)](https://platform.openai.com/docs)
[![YFinance](https://img.shields.io/badge/yfinance-Integration-yellow?style=flat-square)](https://pypi.org/project/yfinance/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOf-DataScience-orange?style=flat-square)](https://www.100daysofcode.com/)


## 🌟 Project Goal: Beyond the Chat Window - Automating AI Interaction

We all know ChatGPT through its web interface, but the real power for developers and data scientists lies in its **API**. This project dives into using the `openai` Python library to programmatically interact with `gpt-3.5-turbo`, moving beyond simple chat to **automate tasks, generate structured data, maintain conversational context, and even mashup AI insights with external data sources** (like real-time stock prices!).

For Day 74 of my #100DaysOfDataScience challenge, the focus was on mastering the fundamentals of the OpenAI Chat API for practical data science workflows.

---

## ✨ What I Built & Explored: Key Capabilities

This project demonstrates several core techniques for leveraging the OpenAI API:

1.  **Structured Data Generation:** Prompting the AI to generate not just text, but specific outputs like **Python code** to create a Pandas DataFrame and the resulting data formatted as a **Markdown table**. This shows how to use AI for controlled, structured content creation.
2.  **Conversational Context:** Implementing multi-turn conversations by correctly structuring the `messages` array (`system`, `user`, `assistant` roles) to maintain context. We used the AI's previously generated dataset to ask follow-up questions (like calculating the mean height).
3.  **API Mashups:** Combining the power of different APIs! We used the `yfinance` library to fetch **real-time stock data** (Silicon Valley Bank - SIVB during a critical period) and then passed this data *into* an OpenAI prompt, asking the AI to perform analysis (find highs/lows/biggest change) and generate a concise financial report.
4.  **Prompt Engineering Basics:** Utilizing the `system` message to guide the AI's persona and behavior ("helpful data science assistant," "terse financial expert").
5.  **Robust API Interaction:** Implementing checks for successful API responses (`finish_reason == "stop"`) and creating a helper function (`chat`) to streamline repetitive API call boilerplate code.

---

## 🛠️ Tech Stack & Core Concepts

*   **Core Language:** **Python 3.8+**
*   **AI Engine:** **OpenAI API** (`openai` library) using the `gpt-3.5-turbo` model.
*   **Key API Object:** `openai.ChatCompletion.create`
*   **Message Structure:** Understanding and manipulating the list of dictionaries with `role` (`system`, `user`, `assistant`) and `content`.
*   **External Data Integration:** **`yfinance` library** for fetching financial market data.
*   **Data Handling:** **Pandas** DataFrames (implied for data generation and stock data handling).
*   **Output Formatting:** **`IPython.display` (`display`, `Markdown`)** for rendering AI-generated Markdown nicely in notebooks.
*   **Environment Management:** Using `os.environ` for secure API key handling.

---

## 🗺️ The Journey: From Single Prompt to API Symphony

Let's walk through the key steps and discoveries:

### Act 1: The First Request - Can AI Make Data? 📊

*   **Objective:** Get `gpt-3.5-turbo` to generate Python code for a small dataset and display the dataset itself as Markdown.
*   **Method:** Crafted a detailed `user` message specifying the desired columns (`name`, `height_cm`, `eye_color`), rows (5), data types, and output formats. Used a `system` message to set the "data science assistant" persona.
*   **Key Learning:** The API requires a structured list of `messages`. The AI *can* generate both code and formatted text output in a single response if prompted correctly. Parsing the nested JSON response (`response["choices"][0]["message"]["content"]`) is essential.


### Act 2: Keeping the Thread - Multi-Turn Conversation 💬

*   **Objective:** Use the dataset generated in Act 1 to perform a calculation (mean height).
*   **Method:** Captured the AI's previous response (`assistant_msg`) and constructed a *new* API call including the *entire history*: `[user_msg1, assistant_msg1, user_msg2]`.
*   **Key Learning:** Maintaining context is crucial. The API is stateless; you must explicitly pass the relevant conversation history back in the `messages` array for the AI to understand follow-up requests. Our `chat` helper function abstracted this logic.


### Act 3: The Mashup - Stocks + AI Analysis 📈🤖

*   **Objective:** Get real-time stock data and have the AI analyze it and write a report.
*   **Method:**
    1.  Used `yfinance.Ticker("SIVB").history(period="1mo")` to grab recent Silicon Valley Bank closing prices.
    2.  Converted the relevant Pandas Series (`sivb_close`) to a string using `.to_string()`.
    3.  Embedded this string *directly into the `user` prompt*, clearly instructing the AI what analysis to perform (highest/lowest price dates, largest change date) and asking for both the Python code and a summary report.
    4.  Used a specific `system` message: "You are a financial data expert who writes tersely."
*   **Key Learning:** This showcases the real power of the API – programmatically fetching live data from one source and piping it into another service (OpenAI) for sophisticated analysis and summarization, automating tasks that would be tedious manually. Prompt clarity is vital when including external data.

---

## 💡 Why This Matters & Key Takeaways

*   **Automation Powerhouse:** The API unlocks ChatGPT's abilities for automated scripts, data pipelines, report generation, and integration into other applications.
*   **Structured Output is Possible:** With careful prompting, you can guide the AI to produce code, tables, JSON, or other formats, not just free-form text.
*   **Context is King (and Your Responsibility):** The API doesn't remember past interactions; you must manage and resend the conversation history.
*   **Combining APIs = Superpowers:** Integrating OpenAI with other data sources (like `yfinance` or databases) opens up endless possibilities for dynamic, data-driven AI applications.
*   **Prompt Engineering Matters:** The `system` message significantly shapes the AI's tone and capabilities. Being specific in `user` prompts yields better results. Cost-saving tricks like asking for terse output are useful.

---

*Day 74 of #100DaysOfDataScience complete! This project demystified the OpenAI API, showing how to wield ChatGPT programmatically for powerful data science automation and integration tasks. Created by Vatsal Parikh.*
