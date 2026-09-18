# Scenario Exercises

These four exercises move from understanding to building. Each one names a goal, lists the steps, and states how you will know you succeeded. Do them in order. They assume you have read Part 1 and skimmed the tool chapter for whichever tool you choose.

Every scenario below uses fully invented, anonymized data. Use no real names, clients, or internal details in anything you publish.

---

## Exercise 1: Trace the agent loop by hand

Goal: prove to yourself that you understand the perceive, think, act loop, with no tool at all.

Steps:
1. Take this goal: "count words in the quick brown fox jumps."
2. On paper, write the four parts of one loop turn: what the agent perceives, what it thinks (which tool), what it acts (the call), and what it checks.
3. Now run the script to compare: `python scripts/mini_agent.py "count words in the quick brown fox jumps"`.
4. Confirm your paper trace matches the script's printed steps.

Success: your written loop matches the script's THINK, ACT, and CHECK lines.

---

## Exercise 2: Break and repair a skill contract

Goal: feel why the input contract is the backbone of a reliable skill.

Steps:
1. Run the runner with all inputs: `python scripts/skill_runner.py scripts/hello_skill/SKILL.md person_name="Ms Osei" occasion="new year"`. Confirm it passes and prints the process.
2. Run it again with the occasion removed. Confirm it refuses and names the missing input.
3. Open `scripts/hello_skill/SKILL.md` and add a new required input, `sender_name (required)`, to the Inputs section.
4. Re run step 1. The runner should now report that `sender_name` is missing, because you added it to the contract but did not supply it.
5. Supply it and confirm it passes again.

Success: you can add a required input and watch the contract enforce it, then satisfy it.

---

## Exercise 3: Build a tested skill end to end

Goal: produce a small skill with a golden test set, the way a professional would.

Steps:
1. Choose a narrow, repeatable task you actually do. Keep it small.
2. Answer the four design questions from Chapter 3: inputs, process, output, constraints.
3. Write the `SKILL.md`. Validate it: `python scripts/validate_skill.py path/to/your/SKILL.md`.
4. Create a `tests/` folder beside it with two cases: a normal input and an edge input. For each, write an `input.md` and an `expected.md` checklist.
5. Add a `TEST-LOG.md` with a baseline row for version 1.0.
6. In your tool of choice, invoke the skill on both test inputs and mark each checklist item pass or fail. Record the results in the log.
7. Fix any failure in the skill file, raise the version to 1.1, and re run both tests.

Success: a skill folder that contains a valid `SKILL.md`, a `tests/` folder with two cases, and a `TEST-LOG.md` showing at least one version with both tests passing.

---

## Exercise 4: Choose the right tool for three jobs

Goal: practice matching the tool to the task, which is a real skill in itself.

For each job below, name which of the three tools you would reach for and write one sentence saying why. There is a defensible answer for each; the reasoning matters more than the label.

1. Turn three days of anonymized research notes into a five chapter report as a Word document.
2. Refactor a two thousand line codebase and run its test suite.
3. Prototype a small single page site quickly, for free, trying two different models.

Suggested reasoning:
- Job 1 points to WorkBuddy, because the deliverable is an office document produced from research notes.
- Job 2 points to Cursor, because it is code work on a large existing codebase where indexing and a polished agent help.
- Job 3 points to TRAE, because it is a quick free prototype and you want to compare models without managing keys.

Success: you can justify each choice in one clear sentence, and you understand that the same underlying skill concepts apply across all three tools.

---

## Where to go from here

You now have the full arc: what skills and agents are, how to build and test a skill, and how to work in the three tools. The natural next steps are to build one tested skill per week, keep a public repository of your work, and write up what you learn so others can follow. Teaching a thing is the fastest way to master it.
