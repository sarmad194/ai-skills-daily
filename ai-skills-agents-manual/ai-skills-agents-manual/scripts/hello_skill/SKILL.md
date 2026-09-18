---
name: greeting_writer
description: Writes a short, professional greeting message for a named person and occasion. Use when a user needs a quick, polite opening line for an email or message.
version: 1.0
---

# Greeting Writer

## Purpose
Produce one short, professional greeting line for a given person and occasion.

## Inputs
- person_name (required): the name of the person being greeted.
- occasion (required): the reason for the message, for example "project kickoff" or "new year".
- tone (optional): "formal" or "friendly". Default is "formal".

## Process
1. Read person_name, occasion, and tone.
2. If tone is missing, use "formal".
3. Compose exactly one sentence that names the person and references the occasion.
4. Keep the sentence under 25 words.

## Output
A single greeting sentence, with no extra commentary.

## Constraints
- Never invent facts about the person.
- Do not add more than one sentence.

## Example
Input: person_name = "Director Wang", occasion = "project kickoff", tone = "formal"
Output: "Dear Director Wang, thank you for joining today's project kickoff; we look forward to a productive collaboration."
