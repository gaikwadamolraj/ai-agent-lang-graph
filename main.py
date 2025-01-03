from utils.work_flow import get_workflow
import os

workflow = get_workflow()

# compile the workflow

app = workflow.compile()

question = input("Enter your question:")

# greet: greet to see you here -> Will show the greet response
# if no greet word then will show search result api


inputs = {"question": question}

result = app.invoke(inputs)

print(result)

# will generate the png file for the workflow

from IPython.display import Image, display

# Assuming you have already created and compiled your graph as 'app'
png_graph = app.get_graph().draw_mermaid_png()
# save file to temp folder
with open("graph_flow.png", "wb") as f:
    f.write(png_graph)
