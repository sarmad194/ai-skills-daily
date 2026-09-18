# Chapter 7: TRAE

## What TRAE is

TRAE is an AI native code editor from ByteDance, the company behind TikTok. Like Cursor, it is built on the VS Code framework, so the layout is familiar, but its interface is restyled with a cleaner look inspired by JetBrains Fleet. It was released in early 2025 and has developed quickly since. Its main selling points are that it is free to start, works out of the box, and lets you switch between top tier models, with access to models such as Claude, GPT class models, and DeepSeek without supplying your own API key on the free plan.

As of early 2026, TRAE runs on macOS and Windows. Linux users are limited to the cloud version. Because it is a VS Code fork, most VS Code extensions and settings work directly, which keeps the learning curve low.

## An honest note on privacy

TRAE sends telemetry data to ByteDance, and by default that telemetry is enabled. TRAE documents a Privacy Mode which, when enabled, states that your chat interactions, related code snippets, and AI outputs will not be used for analytics, product improvement, or model training. For sensitive or proprietary work, weigh this carefully and turn on Privacy Mode, or choose a different tool. This is a real consideration, not a formality, and you should make the decision deliberately rather than by default.

## The interface, described

```
+-------------------------------------------------------------+
|  Menu bar        file tabs                     model switch  |
+--------+-----------------------------------+----------------+
|        |                                   |                |
| Side   |   Editor pane:                    |  AI side panel:|
| bar:   |    your code and files            |   Chat,        |
|  files |                                   |   Builder,     |
|  search|                                   |   and SOLO      |
|  git   |                                   |   modes         |
|        |                                   |                |
+--------+-----------------------------------+----------------+
|  Terminal panel (toggle)                                    |
+-------------------------------------------------------------+
```

If you have read Chapter 6, this will look familiar, because both tools share VS Code roots. The distinctive part of TRAE is its three modes.

## The three modes to understand

1. Chat mode. A conversational assistant for everyday coding: analyze code, debug an error, refactor, or ask for suggestions. This is your day to day companion, the equivalent of Cursor's chat.

2. Builder mode. You describe a feature or small project in natural language, and Builder generates it through multi step actions, including scaffolding files and running terminal commands. Think of it as the "build me this" mode.

3. SOLO mode. The most autonomous mode. SOLO takes an idea, plans the workflow, picks the tools, executes, and aims to deliver a running result, scaffolding frontend, backend, and configuration as a running agent rather than a single generation. SOLO is available in the desktop editor and in a web version for people who prefer not to install anything.

These three map neatly onto the autonomy levels from Chapter 2: Chat is assisted, Builder is supervised, and SOLO is autonomous.

## Model switching

A defining feature of TRAE is easy switching between models from the interface. Different models have different strengths and costs, and TRAE lets you pick per task. For learning, start with the default; as you grow confident, experiment to feel the differences.

## MCP and skills

TRAE supports the Model Context Protocol, the same connector standard mentioned in the WorkBuddy chapter, which lets it plug into external tools and data. It also fits the broader open skill ecosystem, so the concepts you learned about skills carry over.

## When to reach for TRAE

Choose TRAE when you want a capable AI editor at no cost, when you want to try several models without managing API keys, or when you want an autonomous build mode to prototype something quickly. Weigh the privacy consideration above for anything sensitive. For large existing codebases, Cursor's indexing is often stronger; for office and research deliverables, WorkBuddy remains the better fit.

## A known limit to keep in mind

On very large projects, for example tens of thousands of lines, TRAE can lose track of the wider project structure, and its most autonomous mode can occasionally get stuck in an error loop that needs a human to step in. Start on smaller tasks, and supervise the autonomous mode until you trust it on a given kind of work.

## Scenario exercise: prototype a small page three ways

Goal: feel all three modes on the same simple task.

1. Install TRAE, or open the web version, and create an empty project. Decide now whether to enable Privacy Mode.
2. Chat mode: ask it to explain how a simple contact form works in HTML, and read the explanation.
3. Builder mode: ask it to "build a contact form with name, email, and message fields, plus basic validation." Review the files it generates.
4. SOLO mode: give the goal "turn the contact form into a small single page site with a header and a thank you message on submit." Watch it plan and execute, and step in if it stalls.
5. Model switch: repeat the Builder step with a different model and compare the two results.

At the end you will have experienced assisted, supervised, and autonomous work in one tool, and felt what model switching changes.

## Sources for live screenshots and current details

TRAE is evolving quickly and its modes and platform support change. Confirm current details against official and recent material:

- TRAE official site: https://www.trae.ai/
- TRAE review with interface details (2026): https://weavai.app/blog/en/2026/05/08/trae-ai-ide-review-2026-bytedances-free-ai-editor/
- TRAE SOLO overview: https://tooldirectory.ai/tools/trae
