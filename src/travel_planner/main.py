#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from travel_planner.crew import TravelPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
    "city": "Hyderabad, India",
    "duration": "3 days",
    "budget": "Moderate (around $150/day excluding accommodation)",
    "interests": "Nature, incredible street food, historical shrines, and futuristic architecture"
}

    try:
        TravelPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "city": "Tokyo, Japan",
        "duration": "3 days",
        "budget": "Moderate (around $150/day excluding accommodation)",
        "interests": "Anime culture, incredible street food, historical shrines, and futuristic architecture"
    }
    try:
        TravelPlanner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelPlanner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "city": "Tokyo, Japan",
        "duration": "3 days",
        "budget": "Moderate (around $150/day excluding accommodation)",
        "interests": "Anime culture, incredible street food, historical shrines, and futuristic architecture"
    }

    try:
        TravelPlanner().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "city": "",
        "duration": "",
        "budget": "",
        "interests": ""
    }

    try:
        result = TravelPlanner().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")


if __name__ == "__main__":
    run()