# Chapter 3: How Skills Are Created

## The mindset shift

Most people, when they want an AI to do something, type a long message and hope. Skill engineering replaces hope with a written contract. You decide, before any generation happens, exactly what goes in, what comes out, and how quality will be judged. Then you write it down once, and it holds forever.

This chapter gives you a repeatable five step method and the anatomy of the file you will produce.

## The five step method

### Step 1: Recognize the scene

Pick one task that you do repeatedly and that follows a recognizable pattern. The best first skills are narrow. "Write anything" is not a skill. "Turn messy meeting notes into a professional summary with an action item table" is a skill. Name the task in a single sentence before you go further.

### Step 2: Design the core components

For your chosen task, answer four questions on paper first:

- Inputs: what does the skill need from the user to do its job? Mark each input as required or optional.
- Process: what are the ordered steps that turn the inputs into the output?
- Output: what exactly is produced, and in what shape?
- Constraints: what must the skill never do, and what limits apply?

These four answers are the heart of the skill. If you cannot answer them, the task is not yet clear enough to automate.

### Step 3: Write the SKILL.md

Now transfer those answers into the standard file. The anatomy is below. Keep the description sharp, because that single line decides whether an agent reaches for this skill at the right moment.

### Step 4: Test with a pyramid

Test small, then broad. Start with one normal example that should clearly succeed. Then test an example with a missing input, to confirm the skill asks for it rather than guessing. Then test an unusual example, to see where the skill bends. Testing in a fresh conversation matters, because leftover context from the writing session can hide missing instructions. Chapter 4 covers testing in full.

### Step 5: Iterate and version

When a test reveals a gap, fix the instructions and raise the version, for example from 1.0 to 1.1, recording what changed. Do not patch a weak skill by adding extra prompts each time you use it. Fix the file, so the improvement is permanent.

## The anatomy of SKILL.md

A complete `SKILL.md` has two parts: the frontmatter and the body.

### The frontmatter

The frontmatter sits at the very top, wrapped in two lines of three dashes. At minimum it carries a name and a description.

```
---
name: meeting_notes_summarizer
description: Turns raw meeting notes into a professional summary with an action item table. Use after any meeting when the user has rough notes and needs a clean, shareable write up.
version: 1.0
---
```

The name is a short machine friendly label, lowercase with underscores. The description does two jobs at once: it says what the skill does, and it says when to use it. Write the description so that an agent scanning a shelf of skills can pick the right one from this line alone.

### The body

Below the frontmatter, use clear headings. A dependable structure is:

```
# Title

## Purpose
One or two sentences on what the skill achieves.

## Inputs
- input_name (required): what it is.
- input_name (optional): what it is, and the default if omitted.

## Process
1. First step.
2. Second step.
3. And so on, in order.

## Output
A precise description of what is produced and its shape.

## Constraints
- What the skill must never do.
- Any limits, such as maximum length.

## Example
A short input and the matching output, so the agent has a model to imitate.
```

## The input contract

The Inputs section is not a formality. It is a contract. It states which fields are required, which are optional, what formats are accepted, and what should happen when something is missing. A skill that enforces its contract is reliable. A skill that skips the check will quietly invent missing information, which is the most common way skills go wrong.

You can see contract enforcement for real. From the scripts folder, run:

```
cd scripts
python skill_runner.py hello_skill/SKILL.md person_name="Director Wang" occasion="project kickoff"
```

The runner loads the skill, confirms both required inputs are present, and prints the process the agent would follow. Now leave one out on purpose:

```
python skill_runner.py hello_skill/SKILL.md person_name="Director Wang"
```

This time the runner refuses to proceed and names the missing input. That refusal is the contract doing its job. A well built skill stops and asks rather than guessing.

## Give tools the least access they need

If your skill uses tools, grant only what the purpose requires. Prefer reading from an input directory and writing new files to a separate output directory. Do not allow a skill to change source files just because editing is technically possible. Require confirmation before anything that can overwrite, delete, or publish. This single habit prevents most accidents.

## A worked micro example

Suppose you want a skill that writes a one line project status update. Walking the method:

- Scene: a status line you write daily.
- Inputs: project_name (required), status (required, one of on track, at risk, blocked), one_blocker (optional).
- Process: state the project, state the status, add the blocker if present, keep to one sentence.
- Output: a single sentence, under 30 words.
- Constraints: never invent a blocker that was not supplied; never exceed one sentence.

That is a complete skill design, ready to become a `SKILL.md`. Notice how much clarity you gained by answering four questions before writing a single instruction.

## Key terms from this chapter

- Input contract: the rules for what inputs are required, optional, and what happens when one is missing.
- Frontmatter description: the line that tells an agent when to use the skill.
- Versioning: raising the version number and recording what changed when you improve a skill.
- Least access: giving a skill's tools only the permissions the task requires.

## What is coming next

You can now write a skill from a blank page. Chapter 4 shows the other side: how to invoke a skill, and how to test it properly so you trust the output before it reaches anyone else.
