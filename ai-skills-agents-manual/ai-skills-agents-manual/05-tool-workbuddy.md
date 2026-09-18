# Chapter 5: WorkBuddy

## What WorkBuddy is

WorkBuddy is an AI workbench from Tencent, built for office and knowledge work rather than for writing code. You describe what you need in plain language, and a team of agents can plan the task, split it into parallel sub tasks, and hand back finished deliverables such as Markdown, Word, and PowerPoint files in one flow. Its strength is documents, research, spreadsheets, and communication. This is the tool you have been using to build skills.

## The three layers to understand

WorkBuddy is easiest to learn if you picture it as three stacked layers.

1. Skills. Modular capabilities you create or install, each defined by a `SKILL.md` file. This is the layer this manual has been teaching. You invoke a skill to perform a repeatable task.
2. Connectors, also called MCP. Integration bridges to outside services such as documents, GitHub, and knowledge bases. Connectors let an agent reach your real tools and data rather than working in a sealed box.
3. Experts. Domain specific agents tuned for a kind of work, for example research or review. You pick an expert suited to the job instead of asking one general assistant to do everything.

Most beginners underuse the Skills layer. That is exactly the layer you have been strengthening, which puts you ahead of the typical user.

## The interface, described

WorkBuddy presents a task centered workspace. A typical layout, described as labeled regions:

```
+-------------------------------------------------------------+
|  Top bar:  workspace name        model picker      account  |
+----------------+--------------------------------------------+
|                |                                            |
|  Left panel:   |   Main task area:                          |
|   - New Task    |    the conversation and the agent's       |
|   - Task list   |    step by step plan and progress         |
|   - Skills      |                                            |
|   - Connectors  |                                            |
|   - Experts     |                                            |
|                |                                            |
+----------------+--------------------------------------------+
|  Input box:  describe the task, attach files, choose mode   |
+-------------------------------------------------------------+
```

The pieces you will use most:

- New Task. Starts a fresh task. Begin skill testing here, so that no context leaks in from an earlier conversation.
- Task list. Your history of tasks, so you can return to earlier work.
- Skills. Where your installed and created skills live, and where you start the Create Skills flow.
- Input box and mode selector. Where you type the instruction and choose how much autonomy to grant, for example an automatic mode that plans and runs the task end to end.
- Model picker. WorkBuddy can route different tasks to different underlying models. For most skill work the default is fine.

## Creating a skill in WorkBuddy

WorkBuddy can generate a skill for you from a description, which is a fast way to produce a first draft you then refine by hand.

1. Open a New Task and follow the Create Skills path.
2. In plain language, ask it to create a specific skill. Supply the purpose, the inputs, the outputs, and the limits, the same four components from Chapter 3.
3. WorkBuddy generates the skill files, typically a definition file plus any implementation and a short readme.
4. Inspect the generated files. Read them against the four questions. Do not assume they are correct because they were generated.
5. Install the skill, then open a fresh conversation and invoke it with a real task.
6. Test using the pyramid from Chapter 4: a normal input, a missing input, and an unusual input.

The reason to test in a fresh conversation is worth repeating: context from the creation session can hide missing instructions, so a skill that looks complete may in fact be leaning on the earlier chat.

## Where skills live on disk

When you build skills locally, they are stored in a skills folder inside your project, commonly under a hidden `.workbuddy` directory. Because that folder is hidden and is specific to the tool, you usually do not publish it to a public repository. You publish the clean, desensitized skill files instead. This matches the practice you have been following: keep tool specific and private material out of public repositories.

## A safety habit specific to installed skills

If you install a skill made by someone else, review it before you run it. Community skills can contain scripts, and a script can do anything the tool permits. Read the `SKILL.md` and any scripts first, and prefer skills that only read from an input area and write to a separate output area. Grant nothing more than the task needs.

## Scenario exercise: build and test a status update skill

Goal: produce a skill that writes a one line project status update.

1. Open a New Task and start the Create Skills flow.
2. Ask WorkBuddy to create a skill named `status_update_writer` with these components:
   - Inputs: project_name (required), status (required, one of on track, at risk, blocked), one_blocker (optional).
   - Process: state the project, state the status, add the blocker only if supplied, keep to one sentence under 30 words.
   - Output: a single sentence.
   - Constraints: never invent a blocker; never exceed one sentence.
3. Inspect the generated `SKILL.md` against those four components. Correct anything that drifted.
4. In a fresh conversation, invoke it three times: once with all inputs, once with the status left out, once with an unusually long project name.
5. Confirm the second run asks for the missing status rather than guessing. If it does not, strengthen the input contract and raise the version to 1.1.

When it passes all three, commit it to your repository with a clear message, and you have another tested skill in your portfolio.

## Sources for live screenshots and current details

WorkBuddy changes over time. Confirm the current interface and features against the official material:

- WorkBuddy official site: https://www.workbuddy.ai/
- How to create reusable skills with WorkBuddy (walkthrough): https://www.tencentcloud.com/techpedia/145692?lang=en
- Agent Skills open standard: https://agentskills.io/home
