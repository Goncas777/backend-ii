from crewai import Agent


TARGET_QUERY = "Hello"
PREDEFINED_RESPONSE = "Hi! This is a predefined response."


def respond(agent: Agent, user_input: str) -> str:
    if user_input == TARGET_QUERY:
        return PREDEFINED_RESPONSE
    return "Input not recognized."


def main():
    agent = Agent(
        role="SimpleAgent",
        goal="Return a predefined response for a specific input.",
        backstory="A minimal agent created for a simple exercise.",
    )
    user_input = TARGET_QUERY
    response = respond(agent, user_input)
    print(response)


if __name__ == "__main__":
    main()
