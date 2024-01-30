# Teaching Assistant

---

**Table of Contents**

1. [Introduction](#1-introduction)
2. [Getting Started](#2-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#3-usage)
    - [Setting up the Development Environment](#setting-up-the-development-environment)
    - [Building the Teaching Assistant](#building-the-teaching-assistant)
    - [Running the Teaching Assistant](#running-the-teaching-assistant)
4. [Agents and Workflow](#4-agents-and-workflow)
    - [Researcher Agent](#researcher-agent)
    - [Writer Agent](#writer-agent)
    - [Examiner Agent](#examiner-agent)
    - [Task Assignments](#task-assignments)
5. [Troubleshooting](#5-troubleshooting)
6. [Contributing](#6-contributing)

---

#### 1. Introduction

Welcome to the Teaching Assistant project. This project utilizes CrewAI, Langchain, and Ollama to create an agent-based framework for generating educational content on Natural Language Processing (NLP).

#### 2. Getting Started

##### Prerequisites

Before you start, ensure you have the following prerequisites:

- Python 3 installed
- Access to a terminal or command prompt
- Reliable internet connection

##### Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

- Download Ollama from [Here](https://ollama.ai/download). Once it is downloaded, open your terminal and download the weights of any model of your choice. In my case, I used Mistral and Openhermes. Refer to the Ollama website [Here](https://ollama.ai/library) to see the models they have.

- Download the Mistral and Openhermes models using:

```bash
ollama run mistral
ollama run openhermes
```

#### 3. Usage

##### Setting up the Development Environment

- Install CrewAI using:

```bash
pip install crewai
```

##### Building the Teaching Assistant

- Create the Researcher, Writer, and Examiner agents using the provided code.
- Assign tasks to each agent within a Crew as shown in the example code.

##### Running the Teaching Assistant

Execute the script to run the Teaching Assistant:

```bash
python teaching_assistant.py
```

#### 4. Agents and Workflow

##### Researcher Agent

The Researcher Agent generates engaging ideas for teaching NLP using the Openhermes model. It utilizes the DuckDuckGoSearchRun tool from Langchain, which is used to search the web for the latest articles, in my case NLP.

```bash
# Researcher Agent
researcher = Agent(
    role='Researcher',
    goal='Generate engaging ideas and concepts for teaching NLP to beginners.',
    backstory='The Researcher Agent, an expert in NLP, aims to create captivating concepts to serve as a foundation for the Writer Agent.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_openhermes
)
```

##### Writer Agent

The Writer Agent composes a clear and informative text on NLP using ideas provided by the Researcher. The Writer Agent uses the Mistral model.

```bash
# Writer Agent
writer = Agent(
    role='Writer',
    goal='Compose a clear and informative piece of text explaining NLP.',
    backstory='Drawing inspiration from the ideas provided by the Researcher, the Writer Agent\'s goal is to produce an easily digestible text on NLP.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_mistral
)
```

##### Examiner Agent

The Examiner Agent leverages the Openhermes model to craft 2-3 insightful test questions to evaluate understanding.

```bash
# Examiner Agent
examiner = Agent(
    role='Examiner',
    goal='Create 2-3 test questions and correct answers to evaluate the understanding of the NLP text.',
    backstory='The Examiner Agent, armed with deep knowledge in NLP, will meticulously design questions and provide correct answers to gauge the students\' comprehension after reading the text crafted by the Writer.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_openhermes
)
```

##### Task Assignments

Assign tasks to each agent within a Crew:

```bash
# Create a Crew with the agents and tasks
crew = Crew(
    agents=[researcher, writer, examiner],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential
)

# Kick off the Crew's workflow
result = crew.kickoff()
```

#### 5. Troubleshooting

- Verify that all prerequisites are installed.
- Review error messages in the console for guidance.

#### 6. Contributing

Contributions to this project are welcome! To contribute:

- Fork the repository and create a new branch for your changes.
- Submit a pull request with detailed explanations of your changes.
- Report bugs or suggest new features through the issue tracker.
```
