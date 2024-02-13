# Import necessary modules and classes from Langchain and CrewAI
from langchain.llms import Ollama
from langchain.tools import DuckDuckGoSearchRun
from crewai import Agent, Task, Crew, Process

# Create an instance of the DuckDuckGoSearchRun tool. This tool will be used by the Researcher to search for information related to NLP concepts for teaching beginners.
search_tool = DuckDuckGoSearchRun()

# Create instances of Ollama models for openhermes and mistral. These models will be used by the agents to generate text and understand instructions.
ollama_openhermes = Ollama(model="openhermes")
ollama_mistral = Ollama(model="mistral")

# Researcher Agent: Develops ideas for teaching NLP
researcher = Agent(
    role='Researcher',
    goal='Generate 5 engaging and interactive ideas for teaching NLP key concepts to beginners.',
    backstory='A seasoned NLP enthusiast, dives into language processing, crafting captivating ideas to ignite exploration in beginners.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_openhermes
)

# Writer Agent: Uses the ideas to write a piece of text
writer = Agent(
    role='Writer',
    goal='Craft a captivating and easily digestible text on NLP that demystifies complex concepts for beginners. Weave compelling examples and clear explanations to spark curiosity and equip learners with a solid foundation in NLP.',
    backstory='Inspired by the Researcher\'s ideas, the Writer crafts engaging text that unravels NLP\'s mysteries for beginners. Fueled by a passion for clarity, they aim to spark curiosity and unlock the potential of language processing.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_mistral
)

# Examiner Agent: Crafts test questions based on the written text
examiner = Agent(
    role='Examiner',
    goal='Craft 3 diverse test questions, including at least 2 multiple-choice and 1 fill-in-the-blank question, to effectively assess different levels of understanding of the NLP text. Ensure questions cover key concepts explained in the text and promote critical thinking.',
    backstory='The Examiner, a master of NLP knowledge, rigorously analyzes the Writer\'s text. With keen attention to detail, crafts diverse and thought-provoking questions to unveil learners\' true understanding of the presented concepts.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_openhermes
)

# Tasks with descriptions for each agent. Each task describes what the agent needs to do.
task1 = Task(description='Generate 5 engaging ideas for teaching NLP', agent=researcher)
task2 = Task(description='Compose a clear and informative text on NLP', agent=writer)
task3 = Task(description='Craft 2-3 test questions to evaluate understanding', agent=examiner)

# Create a Crew with the agents and tasks. This defines the workflow and order of execution.
crew = Crew(
    agents=[researcher, writer, examiner],
    tasks=[task1, task2, task3],
    verbose=2,  
    process=Process.sequential  # Tasks run one after another.
)

# Kick off the Crew's workflow
result = crew.kickoff()

# Print the result of the workflow
print(result)
