def classify(input):
    return "greeting" if "greet" in input else "handle_search"


def classify_input_node(state):
    question = state.get("question", "").strip()
    classification = classify(question)  # Assume a function that classifies the input
    return {"classification": classification}


def handle_greeting_node(state):
    return {
        "response": "Hello I am from the greet so i can answer you. How can I help you?"
    }


def handle_search_node(state):
    question = state.get("question", "").strip()
    search_result = f"I am from Search result for '{question}'"
    return {"response": search_result}


def decide_next_node(state):
    return (
        "handle_greeting"
        if state.get("classification") == "greeting"
        else "handle_search"
    )
