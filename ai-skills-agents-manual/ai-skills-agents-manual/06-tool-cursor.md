# Chapter 6: Cursor

## What Cursor is

Cursor is an AI first code editor made by a company called Anysphere. It is a fork of Visual Studio Code, which means it looks and behaves like the widely used VS Code editor, with AI features built into the center of the workflow rather than added on the side. It runs on Windows, macOS, and Linux. As of 2026 the current generation is Cursor 3, released in April 2026, which reframed the editor as a workspace for running agents.

Because Cursor is built on VS Code, if you have ever used VS Code, the file explorer, editor pane, and terminal will already be familiar. You can even install many of the same extensions.

## The interface, described

```
+-------------------------------------------------------------+
|  Menu bar        file tabs                         settings  |
+--------+-----------------------------------+----------------+
|        |                                   |                |
| Side   |   Editor pane:                    |  AI panel:     |
| bar:   |    your code and files            |   Chat and     |
|  files |                                   |   Agent live   |
|  search|                                   |   here, on the |
|  source|                                   |   right side   |
|  control                                   |                |
|        |                                   |                |
+--------+-----------------------------------+----------------+
|  Terminal panel (toggle): run commands here                 |
+-------------------------------------------------------------+
```

The regions you will use:

- Side bar. File explorer, search, and source control (Git), just as in VS Code.
- Editor pane. Where you read and write files.
- AI panel. On the right, where Chat and Agent run. This is the part that makes Cursor different.
- Terminal panel. A built in command line, so you can run and test without leaving the editor.

## The four AI features that matter

You do not need every feature to start. Learn these four in order.

1. Tab, the autocomplete. As you type, Cursor predicts the next lines and can suggest edits that span multiple lines and jump across files. Press Tab to accept. This is the fastest way to feel the benefit on day one.

2. Inline edit. Select a block of code, then open the inline edit box, commonly with Control or Command and K. Describe the change in words, for example "add error handling to this function," and Cursor rewrites the selected code in place. When it proposes a change, review the difference and click Apply to accept.

3. Chat. Open the chat panel, commonly with Control or Command and L. Ask questions about your code, request an explanation, or ask for a new function. Chat can see the context of your open files, so its answers are grounded in your actual project.

4. Agent mode. This is the autonomous mode. You give a higher level goal, and the agent plans the steps, edits files, and can run commands in the terminal to reach the goal. Two safety features are built for real work: Plan Mode, where the agent lays out its plan before acting, and Checkpoints, which let you roll back to an earlier state if a change goes wrong.

## Rules files: teaching Cursor your standards

Cursor can read a rules file in your project that tells it how you want it to behave, for example which style to follow or which directories to avoid. This is the closest thing in Cursor to a project level skill: written standards the agent applies every time. You can also add an ignore file that keeps the AI from indexing noisy directories such as build outputs and dependency folders, which keeps its context focused.

## How Cursor relates to skills

Cursor supports the open skill standard, which means a `SKILL.md` written for the standard can be used here as well as in other supporting tools. This is the practical payoff of the open format from Chapter 1: the research report skill you built is not locked to one tool.

## When to reach for Cursor

Choose Cursor when the work is code: building a feature, refactoring, fixing a bug, or understanding an unfamiliar codebase. Its codebase indexing is strong on large projects, and its agent experience is polished. For office documents and research, WorkBuddy is the better fit. For a free option with broad model access, see TRAE in the next chapter.

## A caution that applies to every AI coding tool

An agent can write code you do not understand. The discipline that protects you is simple and non negotiable: read the difference it proposes, run the tests yourself, and never merge code you cannot explain. The tool accelerates you; it does not absolve you of understanding what ships.

## Scenario exercise: your first hour in Cursor

Goal: feel all four AI features on a tiny project.

1. Open Cursor and create a new folder with a single file named `app.py`.
2. Tab: start typing `def add(a, b):` and let Tab suggest the body. Accept it.
3. Inline edit: select the function, open inline edit, and ask it to "add a docstring and input validation." Review the difference and apply.
4. Chat: open the chat panel and ask, "what does this file do and how would I test it?" Read the explanation.
5. Terminal: open the terminal and run the file to confirm it works.
6. Agent mode: give the goal "add a subtract function and a small test, then run the test." Watch it plan, edit, and run. Review every change before accepting.

At the end you will have touched autocomplete, inline edit, chat, terminal, and the agent, which is the whole core of Cursor.

## Sources for live screenshots and current details

Cursor updates frequently. Confirm the current interface and shortcuts against official and recent material:

- Cursor official site: https://cursor.com
- What Is Cursor, explained (2026): https://www.developersdigest.tech/blog/what-is-cursor-ai-code-editor-2026
- Cursor beginner tutorial (2026): https://www.nxcode.io/resources/news/cursor-tutorial-beginners-2026
