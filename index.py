import os 
from crewai import Agent, Task , Crew
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

llm=Ollama(model='openhermes')
researcher=Agent(
    llm=llm,
    role="Senior Property Researcher",
    goal="Find promising investment properties",
    backstory="You are a veterah property analyst. In this case you're looking for retail properties to invest in.",
    allow_delegation=False
)

#part-2
#Define a task
task1=Task(
    description="Search the internet and find 5 promising real estate investment suburbs in Sydney, Australia. For each suburb highlighting the mean, low and max prices as well as the rental yield and any potential factors that would be useful to know for that area.",
    expected_output="""A detailed report of each of the suburbs.The results should be formatted as shown below: 

    Suburb 1: Randosuburbville
    Mean Price: $1,200,000
    Rental Vacancy: 4.2%
    Rental Yield: 2.9%
    Background Information: These suburbs are typically located near major transport hubs, employment centers, and educational institutions. The following list highlights some of the top contenders for investment opportunities """,
    agent=researcher,
    output_file='task1_output.txt'
)

#part-3
#setting up the crew
crew=Crew(agents=[researcher],tasks=[task1],verbose=2)
task_output=crew.kickoff()
print(task_output)