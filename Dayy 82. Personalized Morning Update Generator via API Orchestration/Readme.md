# Personalized Morning Update Generator via API Orchestration ☀️📰

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-HTTP_Client-yellowgreen?style=flat-square)](https://requests.readthedocs.io/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-Chat_&_TTS-brightgreen?logo=openai&style=flat-square)](https://platform.openai.com/docs)
[![External APIs](https://img.shields.io/badge/APIs-NewsAPI,_Meteosource-orange?style=flat-square)](https://newsapi.org/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_82-purple?style=flat-square)](https://www.100daysofcode.com/)

https://github.com/user-attachments/assets/2691e681-afb5-4483-b92c-90bd50ecca4d

![code-along-schema](https://github.com/user-attachments/assets/3f16a4e4-7cf3-4944-91dd-21ee6689500c)

## 🎯 Project Goal: Building Your Automated Morning Briefing

Imagine waking up not just to an alarm, but to a personalized audio update featuring today's weather forecast and the latest news headlines, delivered in a specific tone (maybe even a funny one!). That's exactly what this Day 82 project for my #100DaysOfDataScience challenge achieves!

We built a Python script that acts as a **digital personal assistant**, orchestrating multiple **REST APIs** to:

1.  **Fetch Real-time Data:** Grab the top US news headlines from **NewsAPI** and the local weather forecast for Bloomington, Indiana from **Meteosource**.
2.  **Synthesize a Narrative:** Use **OpenAI's Chat Completions API** (`gpt-4o-mini`) to creatively weave the fetched news and weather into an engaging "Morning Update" monologue, following a specific structure and tone (like funny!).
3.  **Generate Audio:** Convert the AI-generated text into a natural-sounding audio file using **OpenAI's Text-to-Speech (TTS) API** (`tts-1` model with 'fable' voice).
4.  **Save the Result:** Output the final briefing as an `morningupdate.mp3` file, ready to listen to!

This project demonstrates practical **API integration**, **data handling**, **prompt engineering**, and **workflow automation** using core Python libraries.

---

## ✨ Key Features & Concepts Mastered

*   **Multi-API Orchestration:** Successfully integrated four distinct APIs (NewsAPI, Meteosource [find_places & point], OpenAI Chat, OpenAI TTS) in a sequential workflow.
*   **REST API Fundamentals:** Applied core concepts:
    *   **HTTP Verbs:** Used `GET` (for NewsAPI, Meteosource) and `POST` (for OpenAI APIs).
    *   **Authentication:** Implemented different methods:
        *   API Key via URL Parameters (`apiKey` for NewsAPI).
        *   API Key via Headers (`X-API-Key` for Meteosource).
        *   Bearer Token via Headers (`Authorization: Bearer ...` for OpenAI).
    *   **Request Payloads:** Constructed JSON payloads (`json` parameter in `requests.post`) for OpenAI API calls.
    *   **Response Handling:** Parsed JSON responses (`.json()`) and binary audio content (`.content`). Checked status codes (`response.status_code == 200`) for success/failure.
*   **Data Extraction & Formatting:** Pulled specific data fields (headlines, descriptions, forecast summary, `place_id`) from API responses. Formatted data (news list, weather string) for injection into AI prompts using f-strings.
*   **AI Prompt Engineering:** Crafted distinct `system` (defining persona, structure, constraints) and `user` (providing the specific request and dynamic data) messages for the OpenAI Chat API to generate a tailored monologue.
*   **Text-to-Speech Conversion:** Leveraged OpenAI's TTS API to convert the generated text into an MP3 audio file, handling the binary response data.
*   **Secure API Key Management:** Used environment variables (`os.environ`) to securely manage sensitive API keys, avoiding hardcoding them in the script.
*   **Basic File I/O:** Wrote the generated audio data to a local `.mp3` file using Python's built-in file handling (`open` with `'wb'` mode).

![request-response-cycle](https://github.com/user-attachments/assets/77ccf486-4f7b-4c40-9ec7-337c0c94dd35)

---

## 🛠️ Tech Stack: The Building Blocks

*   **Core Language:** Python 3.8+
*   **HTTP Client:** `requests` library (for making all API calls).
*   **Environment Variables:** `os` library (for secure API key access).
*   **APIs Consumed:**
    *   NewsAPI (`v2/top-headlines`)
    *   Meteosource (`v1/free/find_places`, `v1/free/point`)
    *   OpenAI (`v1/chat/completions` with `gpt-4o-mini`)
    *   OpenAI (`v1/audio/speech` with `tts-1` model, `fable` voice)
*   **Data Formats:** JSON (requests & responses), MP3 (output).
*   **Development Environment:** Jupyter Notebook (`solution.ipynb`).

---

## 🗺️ The Workflow: From APIs to Audio

Here's a step-by-step breakdown of how the script orchestrates the "Morning Update":

1.  **Setup (`Task 0: Preparing your workbook`):**
    *   Import `os` and `requests`.
    *   Securely load API keys (NewsAPI, Meteosource, OpenAI) from pre-configured environment variables into Python variables. This is crucial for security.

2.  **Fetch News (`Task 1: Getting the latest news headlines`):**
    *   Define `newsapi_url_parameters` dictionary including `country='us'` and the `apiKey`.
    *   Send a `GET` request to `https://newsapi.org/v2/top-headlines` using `requests.get(..., params=...)`.
    *   Check for a `200 OK` status code.
    *   Parse the JSON response, extracting `title` and `description` for the top articles (filtering out "[removed]" titles) into the `headline_articles` list.

3.  **Fetch Weather (`Task 2: Fetch the weather forecast from meteosource`):**
    *   **Step 3a (Find Location ID):**
        *   Define `meteosource_headers` with `X-API-Key`.
        *   Define `meteosource_findplaces_url_parameters` with `text='Bloomington, Indiana'`.
        *   Send `GET` request to `/find_places` API using `requests.get(..., params=..., headers=...)`.
        *   Extract the `place_id` (e.g., 'bloomington-4254679') from the first result in the JSON response.
    *   **Step 3b (Get Forecast):**
        *   Define `meteosource_point_url_parameters` including the retrieved `place_id`, `sections='daily'`, and `units='metric'`.
        *   Send `GET` request to `/point` API using `requests.get(..., params=..., headers=...)`.
        *   Extract today's weather `summary` string (e.g., "Partly sunny changing to cloudy...") from the `daily.data[0]` part of the JSON response into the `weather_forecast` variable.

4.  **Generate Update Text (`Task 3: Generate the "Update message"`):**
    *   Define `system_message` (AI persona, instructions, desired structure: greeting, weather, news summaries, closing).
    *   Define `user_message` using an f-string to dynamically insert the fetched `weather_forecast` string and the `headline_articles` list (formatted within the string). Specifies the desired "funny and light" tone.
    *   Define `openai_headers` with the `Authorization: Bearer {API_KEY_OPENAI}` token.
    *   Construct the `completions_request_data` dictionary specifying `model='gpt-4o-mini'` and the `messages` list containing the system and user prompts.
    *   Send a `POST` request to `https://api.openai.com/v1/chat/completions` using `requests.post(..., headers=..., json=...)`.
    *   Check for `200 OK`.
    *   Extract the AI-generated monologue from `response.json()['choices'][0]['message']['content']` into the `morning_update` variable.

5.  **Generate Audio File (`Task 4: Use Text to Speech (TTS)...`):**
    *   Construct the `tts_request_data` dictionary specifying `model='tts-1'`, `voice='fable'`, and `input=morning_update`.
    *   Send a `POST` request to `https://api.openai.com/v1/audio/speech` using `requests.post(..., headers=..., json=...)`.
    *   Check for `200 OK`.
    *   **Crucially:** Open a local file (`morningupdate.mp3`) in **binary write mode (`'wb'`)**.
    *   Write the **binary content** of the response (`response.content`) directly to the file.
    *   Close the file (`file.close()`).

---

## 🎧 The Result: Your Personalized MP3!

After running the script, you'll find a file named `morningupdate.mp3` in your workspace!

*(Note: Standard Markdown as used on platforms like GitHub doesn't reliably support embedding playable audio directly within the README file itself. To listen, please download the generated `morningupdate.mp3` file from the project directory and play it using your preferred audio player.)*

---

## 💡 Key Learnings & Why This Project Rocks

*   **APIs are Connectors:** This project perfectly illustrates how APIs act as bridges, allowing different specialized services (news, weather, AI text, AI speech) to work together seamlessly.
*   **Handling Diverse APIs:** Successfully navigated different authentication methods (URL params vs. headers vs. Bearer tokens) and HTTP verbs (GET vs. POST).
*   **Beyond Text Responses:** Learned to handle binary data responses (the MP3 audio stream) from an API.
*   **The Power of Prompting:** Demonstrated how well-structured prompts, combining instructions (system message) with dynamic data (user message), can guide powerful AI models like GPT-4o-mini to generate creative and relevant content.
*   **Practical Automation:** Built a script that automates a genuinely useful (and fun!) task – creating a personalized daily briefing.

---

## 🚀 What's Next? Expanding Your AI Assistant

This is just the beginning! You could enhance this project by:

*   **Adding More Data Sources:** Integrate Google Calendar events, unread email counts (Gmail API), stock market updates, or even personal fitness tracker data!
*   **More Sophisticated Error Handling:** Add `try-except` blocks around API calls for more graceful failure management.
*   **User Customization:** Allow users to easily change the location, news sources, AI voice, or desired tone via input variables or a simple UI (maybe even Streamlit!).
*   **Scheduling:** Use system tools (like `cron` on Linux/macOS or Task Scheduler on Windows) or cloud services to run the script automatically every morning.
*   **Exploring Different Models:** Try other OpenAI models (like GPT-4) or different TTS voices.

---

*Day 82 of #100DaysOfDataScience complete! This project was a fantastic dive into practical API orchestration, combining data retrieval, AI text generation, and AI speech synthesis into a tangible, personalized output. Building bridges between services is key! - Vatsal Parikh*
