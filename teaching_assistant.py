# Import necessary modules and classes from Langchain and CrewAI
from langchain.llms import Ollama
from langchain.tools import DuckDuckGoSearchRun
from crewai import Agent, Task, Crew, Process

# Create an instance of the DuckDuckGoSearchRun tool
search_tool = DuckDuckGoSearchRun()

# Create instances of Ollama models for openhermes and mistral
ollama_openhermes = Ollama(model="openhermes")
ollama_mistral = Ollama(model="mistral")

# Researcher Agent: Develops ideas for teaching NLP
researcher = Agent(
    role='Researcher',
    goal='Generate engaging ideas and concepts for teaching NLP to beginners.',
    backstory='The Researcher Agent, an expert in NLP, aims to create captivating concepts to serve as a foundation for the Writer Agent.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_openhermes
)

# Writer Agent: Uses the ideas to write a piece of text
writer = Agent(
    role='Writer',
    goal='Compose a clear and informative piece of text explaining NLP.',
    backstory='Drawing inspiration from the ideas provided by the Researcher, the Writer Agent\'s goal is to produce an easily digestible text on NLP.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_mistral
)

# Examiner Agent: Crafts test questions based on the written text
examiner = Agent(
    role='Examiner',
    goal='Create 2-3 test questions and correct answers to evaluate understanding of the NLP text.',
    backstory='The Examiner Agent, armed with deep knowledge in NLP, will meticulously design questions and provide correct answers to gauge the students\' comprehension after reading the text crafted by the Writer.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_openhermes
)

# Tasks with descriptions for each agent
task1 = Task(description='Generate engaging ideas for teaching NLP', agent=researcher)
task2 = Task(description='Compose a clear and informative text on NLP', agent=writer)
task3 = Task(description='Craft 2-3 test questions to evaluate understanding', agent=examiner)

# Create a Crew with the agents and tasks
crew = Crew(
    agents=[researcher, writer, examiner],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential
)

# Kick off the Crew's workflow
result = crew.kickoff()

# Print the result of the workflow
print(result)