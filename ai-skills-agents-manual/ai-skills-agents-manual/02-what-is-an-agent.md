# Chapter 2: What Is an Agent

## The one sentence version

An agent is a program that pursues a goal by running a loop: it looks at the goal, decides what to do next, does it using a tool, looks at the result, and repeats until the goal is met.

If a skill is a recipe card, an agent is the cook who reads the card and actually makes the dish, fetching ingredients, using the oven, and tasting as they go.

## Why a loop, and not a single answer

A plain question and answer is one shot. You ask, the model answers, and it is done. That works for "what is the capital of France." It does not work for "book me a workspace, invite three people, and send them the details," because that task has several steps, and each step depends on the result of the one before it.

An agent handles multi step work by looping. Each turn around the loop has four parts:

1. Perceive. Read the goal and any results gathered so far.
2. Think. Decide which single tool to use next. In a real agent, this decision is made by a large language model.
3. Act. Call that tool and capture the result.
4. Check. Ask whether the goal is now met. If yes, stop. If no, loop again.

This loop is sometimes called the agent loop, or the perceive, think, act cycle.

## Tools: the hands of the agent

A model on its own can only produce text. An agent becomes useful when it is given tools: small, single purpose functions it is allowed to call. A tool might search the web, read a file, run a calculation, send an email, or open a browser. The model does the thinking; the tools do the doing.

Two ideas about tools matter from the start:

- Give an agent only the tools its task needs. An agent that only writes reports does not need permission to delete files.
- Require confirmation before any action that can overwrite, delete, publish, or change an outside system. Reading is safe. Writing deserves a checkpoint.

## Run the agent script

The repository ships a tiny agent you can run offline. Its "thinking" step is a simple set of rules rather than a paid model, so that it runs on any machine with no key. The loop structure, though, is exactly the structure a real agent uses.

Move into the scripts folder and run:

```
cd scripts
python mini_agent.py "add 12 and 30"
```

Read the output carefully. You will see the agent announce the goal, then take one step: it THINKS and selects the `add` tool, it ACTS by calling that tool, it gets the result 42, it CHECKS that the goal is met, and it stops. Now try two more:

```
python mini_agent.py "uppercase hello world"
python mini_agent.py "count words in the quick brown fox"
```

Each goal routes to a different tool. Then try a goal it has no tool for:

```
python mini_agent.py "translate this to French"
```

The agent reports honestly that it has no suitable tool and stops, rather than pretending. That honest stop is a feature, not a failure. A real agent should do the same when it lacks the means to finish.

## From the toy to the real thing

The only difference between the script you just ran and a production agent is the THINK step. In the script, a handful of `if` rules choose the tool. In a real agent, that choice is made by a language model that reads the goal, considers the available tools, and picks one. Open `scripts/mini_agent.py` and find the `think` function. The comment there marks the exact line you would replace with a model call to turn the toy into a genuine agent.

Everything else, the loop, the tools, the checkpoints, stays the same. This is worth pausing on, because it means agents are less mysterious than they sound. An agent is a loop around a model, with tools attached.

## How skills and agents fit together

Here is the relationship in one line: the agent is the engine, and the skill is the instruction sheet the engine follows for a particular job.

When you invoke a skill, the agent loads the skill's `SKILL.md`, checks that you supplied the required inputs, and then follows the skill's process, using its tools as needed, until it produces the declared output. Chapter 4 shows this end to end.

## Levels of autonomy

Not every agent runs unattended. Modern tools let you choose how much freedom to hand over:

- Assisted: the agent suggests, and you approve each step. Good for high stakes or unfamiliar work.
- Supervised: the agent runs a sequence, pausing at key checkpoints for your confirmation.
- Autonomous: the agent plans and executes a whole task, reporting back at the end. Good for well understood, low risk work.

You will see these levels again in Part 2. WorkBuddy, Cursor, and TRAE each offer a version of this choice.

## Key terms from this chapter

- Agent: a program that pursues a goal through a perceive, think, act loop.
- Agent loop: the repeating cycle of reading the goal, choosing a tool, acting, and checking.
- Tool: a single purpose function an agent is allowed to call, such as search or file read.
- Autonomy level: how much the agent does before pausing for your approval.

## What is coming next

You can now describe both halves of the system: the skill that holds the knowledge, and the agent that acts on it. In Chapter 3 you will build the knowledge half yourself, writing a `SKILL.md` from a blank page using a five step method.
