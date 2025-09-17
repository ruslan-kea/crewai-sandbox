#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew_ai_sandbox.crew import CrewAiSandbox

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "project_type": "Todo Application with Real-time Collaboration"
    }
    try:
        result = CrewAiSandbox().crew().kickoff(inputs=inputs)
        print("Software Development Crew execution completed successfully!")
        print(f"Development project documentation generated: {result}")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "project_type": "Todo Application with Real-time Collaboration"
    }
    try:
        CrewAiSandbox().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewAiSandbox().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "project_type": "Todo Application with Real-time Collaboration"
    }
    
    try:
        CrewAiSandbox().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
