import os
import sys
from dotenv import load_dotenv

from crewai import Crew, LLM
from agents import create_agents
from tasks import create_tasks

load_dotenv()

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py "your topic"')
        sys.exit(1)

    topic = sys.argv[1]
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY is missing")
        sys.exit(1)

    llm = LLM(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        api_key=api_key,
        base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
    )

    researcher, writer, reviewer = create_agents(llm)
    tasks = create_tasks(topic, researcher, writer, reviewer)

    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks=tasks,
        verbose=False
    )
    try:
        result = crew.kickoff()
        print(result)
    except Exception:
        print("Error: request failed")
        sys.exit(1)


if __name__ == "__main__":
    main()