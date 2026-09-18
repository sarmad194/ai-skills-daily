# AI Skills and Agents: A Field Manual from Scratch

A teaching manual that starts at zero and builds up to running real AI skills and agents, then walks through the three tools you will use to do the work: WorkBuddy, Cursor, and TRAE.

This manual is written for a complete beginner. You do not need a programming background to read Part 1. If you can open a folder and type a command, you can follow every runnable example here.

## What you will be able to do after this manual

- Explain, in plain language, what an AI skill is and what an agent is, and how they differ.
- Read and write a `SKILL.md` file, the single file that defines a skill.
- Run three small Python scripts that demonstrate the core ideas with no API key and no internet connection.
- Navigate the interface of WorkBuddy, Cursor, and TRAE, and know which one to reach for.
- Complete four scenario exercises that mirror real work.

## How the manual is organized

### Part 1: Foundations
- [Chapter 1: What Is an AI Skill](01-what-is-a-skill.md)
- [Chapter 2: What Is an Agent](02-what-is-an-agent.md)
- [Chapter 3: How Skills Are Created](03-how-skills-are-created.md)
- [Chapter 4: Using and Testing Skills](04-using-and-testing-skills.md)

### Part 2: Tool interface guides
- [Chapter 5: WorkBuddy](05-tool-workbuddy.md)
- [Chapter 6: Cursor](06-tool-cursor.md)
- [Chapter 7: TRAE](07-tool-trae.md)

### Part 3: Practice
- [Scenario Exercises](exercises/scenario-exercises.md)

## The runnable scripts

All three scripts live in the `scripts/` folder. They are written to teach, not to impress. Each one runs offline.

| Script | What it teaches | How to run |
|--------|-----------------|------------|
| `scripts/validate_skill.py` | The anatomy of a skill file | `python validate_skill.py hello_skill/SKILL.md` |
| `scripts/mini_agent.py` | The perceive, think, act loop of an agent | `python mini_agent.py "add 12 and 30"` |
| `scripts/skill_runner.py` | How an agent checks inputs before running a skill | `python skill_runner.py hello_skill/SKILL.md person_name="Director Wang" occasion="project kickoff"` |

To run them, you need Python 3 installed. Check with `python --version` or `python3 --version`. If you see a version number such as 3.11, you are ready.

## A note on the screenshots in Part 2

The tool chapters describe each interface using labeled text layouts rather than embedded images, so the manual stays accurate as the tools update and stays free of copyrighted screenshots. Each tool chapter ends with a Sources section that links to the official pages where you can see live screenshots and confirm the current layout, because these tools change quickly.

## License

Released under the MIT License. See the LICENSE file in the repository root.
