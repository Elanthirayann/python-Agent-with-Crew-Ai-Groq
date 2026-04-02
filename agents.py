from crewai import Agent

def create_agents(llm):

    researcher = Agent(
        role="Researcher",
        goal="Find accurate information about the topic, briefly",
        backstory="Expert researcher who gathers clear facts",
        llm=llm,
        verbose=False
        
        
    )

    writer = Agent(
        role="Writer",
        goal="Draft a concise explanation in exactly 5 bullet points",
        backstory="Good at simplifying complex ideas",
        llm=llm,
        verbose=False
    )

    reviewer = Agent(
        role="Reviewer",
        goal="Polish the final answer into exactly 5 bullet points",
        backstory="Critical editor who refines content",
        llm=llm,
        verbose=False
    )

    return researcher, writer, reviewer