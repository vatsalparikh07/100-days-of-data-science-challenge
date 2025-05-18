# 🧠 LlamaIndex Deep Research Agent System 🔬

[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.12.36-blue?logo=data:image/svg%2bxml;base64,PHN2ZyBmaWxsPSIjRkZGRkZGIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+TGxhbWFJbmRleDwvdGl0bGU+PHBhdGggZD0iTTEzLjAyIDE0LjY2YTIuNTEgMi41MSAwIDAxLTQuMDQgMGMtMS4yNC0xLjI0LTEuMjQtMy4yNiAwLTQuNTEgMS4yNC0xLjI0IDMuMjYtMS4yNCA0LjUxIDAgMS4xOCAxLjI0IDEuMiAzLjIyLjAzIDQuNTF6TTguNjUgNy45MmMxLjM1LTEuNDIgMy41My0xLjU0IDUuMDMtLjI4bC0uNzEuNzEtNC4wNC00LjA1LjI4LTUuMDItLjc1LS43NXptNi43MyA4LjE2Yy0xLjM1IDEuNDItMy41MyAxLjU0LTUuMDMuMjhsLjcxLS43MSA0LjA0IDQuMDUtLjI4IDUuMDIuNzUuNzV6TTguMSA0LjAxbC0uMy4yOGMuMDQuMSA1LjIgNS4yIDUuMiA1LjJsNC4wMyA0LjA0Yy4wMy4wNC4wNi4wOC4xLjFsLjI3LS4yOWMtLjA3LS4xLTUuMjEtNS4yLTUuMjEtNS4yTC40NCAxLjQxIDEuNDEuNDRsNi42OCA2LjY4ek0xOC41OSA5Ljg5bC0xLjYxIDEuNjFhMi41MSAyLjUxIDAgMDEtLjAyIDMuNTNsMS42MSAxLjYxYy44OC0xLjExLjU5LTIuNzctLjU1LTMuNTJhMS45NCAxLjk0IDAgMDEtLjU4LTEuMDF6TTkuNzQgMTguNjFsLTEuNjEtMS42MWExLjk0IDEuOTQgMCAwMS0xLjAxLS41OGMyLjUxIDIuNTEgMi41MSAyLjUxIDMuNTMtLjAyYTIuNTEgMi41MSAwIDAxIDEuNjEtMS42MXptMy4xNi04LjY1bDEuNjEtMS42MWExLjk0IDEuOTQgMCAwMS41OC0xLjAxYy0yLjUxLTIuNTEtMi41MS0yLjUxLTMuNTMgLjAyYTIuNTEgMi41MSAwIDAxLTEuNjEgMS42MXptNS40NSAxLjU4Yy41OCAxLjAxLjU4IDIuNDggMCAzLjUzbC0xLjYxIDEuNjFjMS4wOS0uNzQgMS40NS0yLjE1LjU1LTMuNTJ6bS04Ljc4IDMuMDdjLS41OC0xLjAxLS41OC0yLjQ4IDAtMy41M2wxLjYxLTEuNjFjLTEuMDkuNzQtMS40NSAyLjE1LS41NSAzLjUyek0xMiAxLjA0YTYuNjEgNi42MSAwIDAwLTYuNjIgNi42Mmw2LjYyIDYuNjIgNi42Mi02LjYyQTYuNjEgNi42MSAwIDAwMTIgMS4wNHptMCAxOC4zOGE2LjYxIDYuNjEgMCAwMC02LjYyLTYuNjJsNi42Mi02LjYyIDYuNjIgNi42MkE2LjYxIDYuNjEgMCAwMDEyIDE5LjQyeiIvPjwvc3ZnPg==&style=flat-square)](https://www.llamaindex.ai/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-brightgreen?logo=openai&style=flat-square)](https://platform.openai.com/)
[![Tavily AI](https://img.shields.io/badge/Tavily-Web_Search_Tool-yellow?style=flat-square)](https://tavily.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_95-purple?style=flat-square)](https://www.100daysofcode.com/)

![image](https://github.com/user-attachments/assets/e313a764-441c-4965-ae01-fdb77d292aab)
*Fig 1: Visualization of the project workflow*

## 🎯 Project Goal: Mastering Agentic Workflows with LlamaIndex

Welcome to Day 95 of my #100DaysOfDataScience challenge! Today, we dive deep into the world of **Agentic AI** using **LlamaIndex**, a powerful framework for building applications with Large Language Models (LLMs). This project explores LlamaIndex's `Workflow` and `AgentWorkflow` abstractions to construct both single-agent and multi-agent systems capable of complex reasoning, tool usage, and state management.

**The Mission:**
1.  Understand and implement the **`AgentWorkflow`** for single agents, enabling them to:
    *   Use external **Tools** (e.g., web search via Tavily AI).
    *   Maintain **conversational state** across multiple turns.
    *   Access and modify **shared context** from within tools.
    *   Stream **events and outputs** for real-time feedback.
    *   Incorporate **Human-in-the-Loop (HITL)** for critical decisions.
2.  Build a **multi-agent system** using `AgentWorkflow` to simulate a "Deep Research" process, involving:
    *   A `ResearchAgent` (uses web search, records notes).
    *   A `WriteAgent` (writes a report based on research).
    *   A `ReviewAgent` (provides feedback on the report).
3.  Explore building **custom `Workflow`s from scratch**, understanding core concepts like:
    *   Steps (`@step` decorator).
    *   Custom Events for inter-step communication.
    *   Implementing **looping, branching, and concurrent execution** patterns.
    *   Collecting results from parallel tasks.
4.  Create a sophisticated **multi-agent "Deep Research" system** using a *custom `Workflow`*, demonstrating fine-grained control over agent interaction and data flow to generate a comprehensive report on a given topic.

This project showcases how LlamaIndex Workflows provide a flexible and powerful way to orchestrate LLM interactions, tool use, and state management for building advanced AI applications.

---

## ✨ Key Features & Concepts Mastered

*   **LlamaIndex Workflows (`llama_index.core.workflow`):**
    *   **`AgentWorkflow`:** A pre-built workflow for quickly creating agents with tools. Used for both single and multi-agent setups (`AgentWorkflow.from_tools_or_functions`, direct instantiation for multi-agent).
    *   **Custom Workflows:** Defined custom classes inheriting from `Workflow`, using the `@step` decorator to define processing stages.
    *   **Events:** Fundamental for communication between workflow steps.
        *   Standard Events: `StartEvent`, `StopEvent`, `InputRequiredEvent`, `HumanResponseEvent`.
        *   Custom Events: Defined Pydantic-like classes inheriting from `Event` to pass specific data structures.
    *   **Context (`Context`):** A crucial object for maintaining and sharing state *within* a single workflow run and *between* multiple runs (for conversational memory). Tools can access and modify this context.
    *   **State Management:** Used `ctx.get("state")` and `ctx.set("state", state)` for agents to read/write shared information (e.g., research notes, draft reports).
    *   **Event Streaming:** Streamed various event types (`AgentStream`, `AgentInput`, `AgentOutput`, `ToolCall`, `ToolCallResult`) to observe the agent's internal operations in real-time.
    *   **Flow Control in Custom Workflows:**
        *   **Looping:** Achieved by a step emitting an event that re-triggers an earlier step (e.g., `step_two` emitting a `LoopEvent` that `step_one` can also accept).
        *   **Branching:** A step emits one of several possible event types, each triggering a different downstream step.
        *   **Concurrency:** A step uses `ctx.send_event()` multiple times to trigger several instances of another step in parallel (e.g., `AnswerAgent` for multiple questions). The `@step(num_workers=N)` decorator helps manage parallel execution.
        *   **Event Collection:** Used `ctx.collect_events(event, [ExpectedEvent1, ExpectedEvent2, ...])` to wait for multiple, potentially different, events from parallel tasks before proceeding.
*   **LLM Integration (`llama_index.llms.openai`):**
    *   Used OpenAI's `gpt-4.1-mini` as the core reasoning engine for agents.
*   **Tool Creation & Usage:**
    *   Defined Python `async` functions as tools (e.g., `search_web` using `AsyncTavilyClient`, `record_notes`, `write_report`, `review_report`, `dangerous_task`).
    *   Emphasized the importance of clear tool names, docstrings (for LLM understanding), and type annotations.
*   **Agent Types (`FunctionAgent`):**
    *   Utilized `FunctionAgent` (suitable for LLMs with tool-calling capabilities) for creating the research, writing, and review agents in the multi-agent system.
    *   Configured agents with system prompts, tools, and `can_handoff_to` specifications.
*   **Human-in-the-Loop (HITL):**
    *   Demonstrated how a tool can emit an `InputRequiredEvent`, pause the workflow, wait for a `HumanResponseEvent` (triggered by user input via `handler.ctx.send_event`), and then proceed based on the human's response.
*   **Workflow Visualization (`llama_index.utils.workflow`):**
    *   Used `draw_all_possible_flows()` to generate HTML visualizations of custom workflow structures, aiding in debugging and understanding.

---

## 🛠️ Tech Stack: The Agentic AI Toolkit

*   **Core Framework:** LlamaIndex (`llama-index` base package and various sub-packages like `llama-index-llms-openai`, `llama-index-utils-workflow`)
*   **LLM Provider:** OpenAI (`gpt-4.1-mini`)
*   **External Tool API:** Tavily AI (for web search capabilities)
*   **Programming Language:** Python 3.8+ (with `asyncio` for asynchronous operations)
*   **Development Environment:** Jupyter Notebook (`solution.ipynb`) / Google Colab
*   **Utilities:** `google.colab.userdata` (for API key management in Colab)

---

## 🗺️ Project Walkthrough: From Single Agent to Deep Research System

The project systematically builds understanding, starting simple and adding complexity:

### Part 1: Mastering `AgentWorkflow` (Single Agent)

1.  **Basic Agent:** Created an `AgentWorkflow` with `gpt-4.1-mini` and a single `search_web` tool (using Tavily). Demonstrated basic querying.
2.  **Stateful Conversations:** Introduced `Context` to allow the agent to remember previous interactions (e.g., remembering the user's name).
3.  **Tools Accessing Context:** Showed how a tool (`set_name`) can directly read from and write to the `state` variable within the `Context`.
4.  **Streaming Events:** Implemented event streaming to observe the LLM's output token-by-token (`AgentStream`) and detailed internal operations (`AgentInput`, `AgentOutput`, `ToolCallResult`).
5.  **Human-in-the-Loop:** Created a `dangerous_task` tool that pauses execution, emits an `InputRequiredEvent`, waits for user confirmation via a `HumanResponseEvent` (sent by the main script), and then acts accordingly.

![image](https://github.com/user-attachments/assets/ce582b5f-e1bc-4832-ae0f-1fd14049e3f6)
*Fig 2: Workflow involving a human confirmation step*

### Part 2: Multi-Agent System with `AgentWorkflow`

1.  **Define Agents & Tools:**
    *   `ResearchAgent`: Uses `search_web` and `record_notes` (writes to context state).
    *   `WriteAgent`: Uses `write_report` (writes draft report to context state).
    *   `ReviewAgent`: Uses `review_report` (writes review to context state).
2.  **Instantiate Multi-Agent Workflow:** Created an `AgentWorkflow` specifying the list of agents, the `root_agent` (ResearchAgent), and an `initial_state` for shared context variables.
3.  **Run & Observe:** Executed the workflow with a research topic. Streamed events to watch as agents handed off tasks (e.g., Research -> Write -> Review -> potentially back to Write if changes needed). The final report and review were stored in the context state.

### Part 3: Building Custom Workflows from Scratch

1.  **Basic Workflow:** Created `MyWorkflow` with a single `@step` reacting to `StartEvent` and emitting `StopEvent`.
2.  **Workflow Visualization:** Used `draw_all_possible_flows` to generate an HTML diagram of the workflow.
3.  **Custom Events & Multi-Step:** Defined `FirstEvent`, `SecondEvent` and built a linear 3-step workflow where each step triggers the next via these custom events.
4.  **Looping Logic:** Modified a step to randomly emit either a `SecondEvent` (proceed) or a `LoopEvent` (go back to a step that accepts `LoopEvent`), demonstrating how loops are formed.
5.  **Branching Logic:** Created a workflow where the first step randomly emits one of two different event types (`BranchA1Event` or `BranchB1Event`), leading to execution down one of two distinct paths.
6.  **Concurrent Execution & Event Collection:**
    *   A `start` step used `ctx.send_event()` multiple times to trigger several instances of `step_two` in parallel. The `@step(num_workers=4)` decorator managed this.
    *   A `step_three` used `ctx.collect_events(event, [ExpectedEvent1, ExpectedEvent2, ExpectedEvent3])` to wait until all parallel tasks completed (each emitting their respective completion event) before processing their combined results. This demonstrated map-reduce style patterns.

![image](https://github.com/user-attachments/assets/a53a5d4b-887b-472b-bc5c-8ca7aab0ea23)
    *Fig 5: Visualization of a workflow with concurrent steps collected by a final step*
    
7.  **Streaming from Custom Workflow:** Showed how `ctx.write_event_to_stream(MyCustomEvent(...))` allows a custom workflow to emit events (like `TextEvent` for LLM tokens, `ProgressEvent` for status updates) that can be handled by the calling script, similar to `AgentWorkflow`.

### Part 4: Sophisticated Multi-Agent System with Custom Workflow (Deep Research)

1.  **Define Agents:**
    *   `QuestionAgent`: Given a topic, generates a list of research questions.
    *   `AnswerAgent`: Takes a single question and uses `search_web` to find a deep answer.
    *   `ReportAgent`: Takes all questions and answers, synthesizes them into a comprehensive report.
2.  **Define Custom Events:** `GenerateEvent` (carries topic), `QuestionEvent` (carries questions), `AnswerEvent` (carries a question and its answer), `ReportEvent` (carries the final report).
3.  **Construct the `DeepResearchWorkflow`:**
    *   `generate_questions` (receives `GenerateEvent` | `StartEvent`) -> Uses `QuestionAgent` -> Emits `QuestionEvent`.
    *   `answer_questions` (receives `QuestionEvent`) -> For each question, uses `ctx.send_event()` to trigger an `AnswerAgent` instance (via a new internal event, conceptually) -> Emits an `AnswerEvent` *for each answered question*.
    *   `generate_report` (receives `AnswerEvent`) -> Uses `ctx.collect_events()` to gather all answers. Once all are collected, uses `ReportAgent` -> Emits `ReportEvent`.
    *   `finalize_report` (receives `ReportEvent`) -> Emits `StopEvent` with the report as the result.
4.  **Run & Stream:** Executed the workflow with a research topic (e.g., "history of the web"). Streamed events to show the progression: questions generated, each question being answered (potentially in parallel), and the final report being compiled.

---

## 💡 Key Learnings & Impact

*   **Workflows are the Backbone:** LlamaIndex `Workflow` is a highly flexible and powerful abstraction for orchestrating complex, multi-step processes involving LLMs, tools, and state.
*   **Granular Control:** Custom Workflows offer finer control over data flow, parallelization, looping, and branching than pre-built agent loops, enabling sophisticated agent designs.
*   **State as a First-Class Citizen:** The `Context` object is key to building stateful agents and multi-agent systems where information needs to be shared and updated across steps or runs.
*   **Event-Driven Architecture:** The event-based system (steps emitting and reacting to typed events) is intuitive for defining dependencies and control flow.
*   **Modularity & Reusability:** Agents (`FunctionAgent`) and Tools (Python functions) can be defined once and reused across different workflows.
*   **Human Oversight:** Easily integrate human checkpoints for critical tasks or feedback loops.
*   **Debugging & Observability:** Event streaming and workflow visualization are invaluable for understanding what an agent system is doing internally.

---

*Day 95 of #100DaysOfDataScience marks a significant leap into building sophisticated agentic systems with LlamaIndex Workflows. From single tool-using agents to complex multi-agent research assistants, the possibilities are vast! - Vatsal Parikh*
