from crewai import Task

def create_tasks(topic, researcher, writer, reviewer):

    task1 = Task(
        description=f"""
        Research the topic: {topic}

        Provide:
        - Key facts (short bullets)
        - Important names/dates/terms (if relevant)
        """,
        agent=researcher,
        expected_output="Bulleted factual notes only"
    )

    task2 = Task(
        description="""
        Using the research notes, draft an explanation for a beginner in exactly 5 bullet points.
        Constraints:
        - Exactly 5 bullets
        - Each bullet 1 sentence, concise
        - No headings, no extra text before/after the bullets
        - No repetition between bullets
        """,
        agent=writer,
        expected_output="Exactly 5 bullet points"
    )

    task3 = Task(
        description="""
        Rewrite the draft into the final answer.
        Output MUST be exactly 5 bullet points.
        Constraints:
        - Exactly 5 bullets (start each line with "- ")
        - Each bullet 1 sentence
        - No headings, no numbering, no extra text before/after
        - Beginner-friendly, concise, and factual
        """,
        agent=reviewer,
        expected_output="Final answer: exactly 5 bullet points"
    )

    return [task1, task2, task3]