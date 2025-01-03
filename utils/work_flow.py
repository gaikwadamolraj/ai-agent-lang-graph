from langgraph.graph import StateGraph, END
from utils.state import GraphState
from utils.node_functions import (
    classify_input_node,
    handle_greeting_node,
    handle_search_node,
    decide_next_node,
)


def get_workflow():
    # init the graph here
    workflow = StateGraph(GraphState)

    # add the nodes to workflow
    workflow.add_node(
        "classify_input", classify_input_node
    )  # this will be the start node to decide route where to go
    workflow.add_node("handle_greeting", handle_greeting_node)  # handle the greetings
    workflow.add_node("handle_search", handle_search_node)  # handle the search

    # add conditional edges to workflow

    workflow.add_conditional_edges(
        "classify_input",
        decide_next_node,
        {"handle_greeting": "handle_greeting", "handle_search": "handle_search"},
    )

    # set the entry point

    workflow.set_entry_point("classify_input")
    workflow.add_edge("handle_greeting", END)
    workflow.add_edge("handle_search", END)

    return workflow
