from pathlib import Path
from dotenv import load_dotenv
from agents import Agent, Runner

def main():
    # Charger les variables d'environnement depuis .env.local
    dotenv_path = Path(".env.local")
    load_dotenv(dotenv_path=dotenv_path)

    example_agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    triage_agent = Agent(
        name="Triage Agent",
        instructions="You determine which agent to use based on the user's homework question",
        handoffs=[example_agent]
    )

    result = Runner.run_sync(triage_agent, "Write a haiku about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    main()
