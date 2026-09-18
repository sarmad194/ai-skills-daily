# Chapter 1: What Is an AI Skill

## Start with a picture you already know

Think about a recipe card. A recipe card has a title, a short line telling you what dish it makes, a list of ingredients, and numbered steps. Anyone can pick up the card and cook the dish, even someone who has never made it before, because the knowledge is written down in a fixed, repeatable form.

An AI skill is a recipe card for an AI agent. It is a small folder that holds written instructions telling the AI how to do one specific task well, every single time, for anyone who uses it.

That is the whole idea. Everything else in this chapter is detail.

## The formal definition

An AI skill is a lightweight, open-format package of instructions and supporting files that gives an AI agent a specific, reusable capability. At its core, a skill is a folder containing one required file named `SKILL.md`. That file holds metadata (a name and a description at minimum) and the instructions that tell the agent how to perform the task. A skill can also bundle scripts, reference documents, and templates.

This format is an open standard. The same skill folder can be used across many different AI tools that support the standard, which is why a skill you write once can be installed in more than one place.

## Why skills matter: the four properties

A good skill has four properties. Remember them with the word each property starts with.

1. Reusable. You write the instructions once, and then you or anyone else can invoke the skill again and again. A research report that used to take three hours becomes a fifteen minute task, because the method is captured in the skill instead of being redone from memory each time.

2. Structured. A skill declares what inputs it needs, what steps it follows, and what output it produces. This structure is what makes the result consistent. Two different people invoking the same skill get output of the same shape and quality.

3. Versioned. A skill has a version number. When you improve it, you move from version 1.0 to version 1.1 and record what changed. This means you can improve a skill over time without losing track of what it used to do.

4. Engineering grade. A skill turns knowledge that lived in one expert's head into an asset the whole organization can use. When a senior colleague leaves, their method stays behind in the skill file.

## What a skill folder looks like

Here is the standard shape of a skill folder. Only the first file is required. The rest are optional and are added when the task needs them.

```
my-skill/
  SKILL.md        Required. Metadata plus instructions.
  scripts/        Optional. Runnable code the skill can call.
  references/     Optional. Background documents the skill can read.
  assets/         Optional. Templates and other resources.
```

## The one file that matters: SKILL.md

Open the file `scripts/hello_skill/SKILL.md` in this repository. It is a complete, working skill. The top of the file, between the two lines of three dashes, is called the frontmatter. It carries the metadata.

```
---
name: greeting_writer
description: Writes a short, professional greeting message for a named person and occasion. Use when a user needs a quick, polite opening line for an email or message.
version: 1.0
---
```

Below the frontmatter come the human readable instructions: the purpose, the inputs, the process, the output, and the constraints. An agent reads the whole file and follows it.

## Run your first script

You do not have to take any of this on trust. The repository ships a small script that reads a real skill file and reports whether it is valid. It runs offline and needs no API key.

Open a terminal, move into the scripts folder, and run:

```
cd scripts
python validate_skill.py hello_skill/SKILL.md
```

You will see the script confirm that the file has a name and a description, and declare the skill valid. Now try breaking it on purpose: open `hello_skill/SKILL.md`, delete the `description:` line, save, and run the command again. The script will report a failure and tell you exactly what is missing. Put the line back when you are done.

That single exercise teaches the most important rule in this entire manual: a skill without a clear name and description is not a skill yet. The description is not decoration. It is how an agent decides whether to use the skill at all.

## What a skill is not

- A skill is not a chatbot conversation. A conversation disappears when you close it. A skill is saved and reused.
- A skill is not a program you must run yourself. You describe the task in the skill, and the agent carries it out.
- A skill is not tied to one company or one tool. Because the format is open, the same skill works across supporting tools.

## Key terms from this chapter

- Skill: a folder with a `SKILL.md` file that gives an agent a reusable capability.
- SKILL.md: the single required file that defines a skill.
- Frontmatter: the metadata block at the very top of `SKILL.md`, wrapped in two lines of three dashes.
- Description: the line that tells an agent when to use the skill. The most important line in the file.

## What is coming next

You now know what a skill is: written knowledge an agent can follow. In Chapter 2 you will meet the thing that follows those instructions: the agent itself. You will run a second script that shows an agent thinking and acting, step by step.
