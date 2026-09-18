#!/usr/bin/env python3
"""
mini_agent.py
Teaching script: the smallest honest example of an AI agent loop.

An agent is a program that runs a loop: it PERCEIVES a goal, THINKS about which
tool to use, ACTS by calling that tool, observes the result, and repeats until
the goal is met. Real agents use a large language model as the "thinking" step.
To keep this runnable offline with no API key, the thinking step here is a
simple rule-based router. The loop structure is exactly the same as a real
agent; only the brain is simpler.

Usage:
    python mini_agent.py "add 12 and 30"
    python mini_agent.py "uppercase hello world"
    python mini_agent.py "count words in the quick brown fox"

Swap the think() function for a real model call and this becomes a real agent.
"""

import sys


# ---- TOOLS: small, single-purpose functions the agent is allowed to call ----

def tool_add(text):
    numbers = [int(word) for word in text.replace("and", " ").split() if word.lstrip("-").isdigit()]
    return str(sum(numbers)) if numbers else "No numbers found to add."


def tool_uppercase(text):
    payload = text.replace("uppercase", "", 1).strip()
    return payload.upper()


def tool_count_words(text):
    payload = text.replace("count words in", "", 1).strip()
    return str(len(payload.split()))


TOOLS = {
    "add": tool_add,
    "uppercase": tool_uppercase,
    "count_words": tool_count_words,
}


# ---- THINK: choose a tool for the goal. A real agent asks an LLM here. ----

def think(goal):
    text = goal.lower()
    if "add" in text or "sum" in text:
        return "add"
    if "uppercase" in text or "capital" in text:
        return "uppercase"
    if "count words" in text:
        return "count_words"
    return None


# ---- THE AGENT LOOP: perceive, think, act, observe, stop ----

def run_agent(goal, max_steps=3):
    print("GOAL:", goal)
    for step in range(1, max_steps + 1):
        print("\nStep", step)
        chosen = think(goal)
        print("  THINK: selected tool ->", chosen)
        if chosen is None:
            print("  ACT:   no suitable tool. Stopping.")
            return "I do not have a tool for that goal."
        result = TOOLS[chosen](goal)
        print("  ACT:   called", chosen, "->", result)
        print("  CHECK: goal satisfied, stopping.")
        return result
    return "Reached step limit without finishing."


if __name__ == "__main__":
    user_goal = " ".join(sys.argv[1:]) or "add 12 and 30"
    print("=" * 55)
    final = run_agent(user_goal)
    print("=" * 55)
    print("FINAL ANSWER:", final)
