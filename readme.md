# CodeAgents vs ToolCallingAgents

## CodeAgents : 
    - does safe imports [ does not `import os` to physically delete files / change directories ]
    - uses math function / printh function ( simple function involving no risk )
    - to import other function : 


```python 
from smolagents import CodeAgent

# Initialize the CodeAgent
agent = CodeAgent(
    tools=[],  # No external tools required for this example
    additional_authorized_imports=["numpy"]  # Allow the numpy library
)

# Provide the task
task = "Calculate the area of a circle with radius 5."

# Run the agent
result = agent.run(task)
print("Result:", result)
```

## ToolCaling agent 

- calls the tools you mentioned 
- Suppose you give the agent access to these tools:
    A calculator tool for arithmetic.
    A search tool for looking up information.
- for task : What is 15 squared? : `What is 15 squared?`
- for task : What is the capital of France? : `search.lookup("Capital of France")`
- calculator + summarizer + trnaslation + image recognition + text2speech + code exection tools  are available

code : 
```python
from smolagents import ToolCallingAgent, Tool

# Define a simple calculator tool
class CalculatorTool(Tool):
    def calculate(self, expression):
        return eval(expression)

# Initialize the ToolCallingAgent with the calculator tool
calculator = CalculatorTool(name="calculator", description="Performs basic arithmetic calculations.")
agent = ToolCallingAgent(tools=[calculator])

# Provide the task
task = "What is 15 squared?"

# Run the agent
result = agent.run(task)
print("Result:", result)
```



## some exmaples of agent output

- all .md files in `crewai` folder -> blog outputs created by agent
