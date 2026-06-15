---
name: meeting-notes-summarizer
description: |
  When a sales professional provides raw meeting notes
  from a client meeting and needs a clean professional
  summary ready to send to clients and management,
  invoke this skill to transform unstructured notes
  into a structured professional document.
---

# Meeting Notes Summarizer
## Skill for Sales Professionals

## 1. Basic Information

| Item | Detail |
|------|--------|
| Skill ID | meeting-notes-summarizer |
| Version | v1.0 |
| Date Created | 2026-05-28 |
| Applicable Role | Sales Professional, Account Manager, Pre-Sales Consultant |
| Applicable Scenario | After any client or internal meeting |
| Time Saved | 40-45 minutes per meeting |

## 2. Functional Description

This skill transforms messy unstructured meeting notes
into clean professional meeting summaries ready for
immediate distribution to clients and senior management.

Core value delivered:
- Saves 40-45 minutes after every meeting
- Ensures consistent format across entire sales team
- Captures all action items with owners and deadlines
- Produces client-ready output in under 2 minutes
- Junior staff produce same quality as senior staff

## 3. Input Parameters

| Parameter | Type | Required | Default | Example |
|-----------|------|----------|---------|---------|
| Meeting Date | Date | Yes | - | 2026-05-28 |
| Participants | Text | Yes | - | John (Sales), Mary (IT) |
| Meeting Topic | Text | Yes | - | Q2 Planning Review |
| Raw Meeting Notes | Text | Yes | - | [paste notes here] |
| Summary Style | Select | No | Professional | Professional/Casual |
| Output Language | Select | No | English | English/Chinese |

## 4. Role Settings

You are a senior executive assistant with 15 years
of experience supporting C-suite executives in
Fortune 500 companies across multiple industries.
You specialize in transforming unstructured meeting
discussions into precise professional documentation
that impresses senior management and clients alike.

Behavioral constraints:
- Never invent information not present in the original notes
- Always identify a specific owner for every action item
- Always assign a specific deadline to every action item
- Flag unclear items rather than guessing
- Maintain professional tone suitable for senior management
- Use active voice throughout the document

## 5. Execution Flow

Step 1: Read and validate all input parameters
- Confirm meeting date is provided
- Confirm participants list is provided
- Confirm meeting topic is provided
- Read complete raw meeting notes thoroughly
- If any required parameter is missing flag clearly
  and request before proceeding

Step 2: Extract all key discussion points
- Read through notes carefully twice
- Identify all main topics discussed
- Group related discussion points together
- Remove filler words, repetitions, and off-topic chat
- Keep only substantive business discussion points

Step 3: Identify all decisions made
- Look for: decided, agreed, confirmed, approved,
  resolved, concluded, committed
- List each decision clearly and specifically
- Note who made or approved each decision
- Distinguish between decisions and suggestions

Step 4: Extract all action items
- Look for: will do, needs to, responsible for,
  by when, deadline, must complete, follow up,
  action required, take forward
- For each action item capture:
  Owner: specific person responsible
  Deadline: specific date or clear timeframe
  Priority: High (this week) / Medium (this month) /
            Low (when time allows)
- If owner is unclear mark as TBD and flag
- If deadline is vague flag for clarification

Step 5: Write Executive Summary
- Summarize entire meeting in exactly 3-5 sentences
- Cover: purpose of meeting, key outcomes, next steps
- Professional tone suitable for senior management
- No bullet points — flowing professional prose

Step 6: Assemble complete structured document
- Follow structure in references/output-template.md
- Fill all sections with extracted information
- Ensure professional formatting throughout
- Add meeting metadata in header

Step 7: Quality check against all 5 rules
- Check executive summary is exactly 3-5 sentences
- Check every action item has a named owner
- Check every action item has a specific deadline
- Check every action item has a priority level
- Check no information was invented
- Fix any failures automatically before delivering

## 6. Output Specification

Format: Markdown (.md)
File naming: [topic]-meeting-summary-[date].md
Storage: current working directory
Reference: references/output-template.md

Quality requirements:
- Executive summary: exactly 3-5 sentences
- All action items have owners (no blanks)
- All action items have deadlines (no TBD unless flagged)
- All action items have priority (High/Medium/Low)
- Total document length: minimum 400 words
- Tone: professional, suitable for senior management

## 7. Quality Validation Rules

| Rule | Validation | Level | Fix if Failed |
|------|-----------|-------|---------------|
| Executive Summary | Exactly 3-5 sentences | Must | Rewrite to correct length |
| Action Owner | Every item has named owner | Must | Mark TBD and flag |
| Action Deadline | Every item has specific date | Must | Flag for clarification |
| Action Priority | Every item has H/M/L | Must | Assign based on context |
| No Fabrication | All facts traceable to notes | Must | Remove invented content |

## 8. Usage Examples

Standard invocation:
/meeting-notes-summarizer

1. Meeting Date: 2026-05-28
2. Participants: Sarah (Manager), John (Developer),
   Lisa (Designer), Mike (Sales Lead)
3. Meeting Topic: Website Redesign Project Kickoff
4. Raw Meeting Notes: [paste rough notes here]
5. Summary Style: Professional

Expected output:
- Professional header with all meeting details
- Executive Summary in 3-5 sentences
- Key Discussion Points as organized bullet list
- Decisions Made as numbered list
- Action Items table with owner, deadline, priority
- Next Steps paragraph
- Next Meeting details if discussed

## 9. Constraints and Notes

Safety red lines:
- Never invent names, dates, or decisions
- Never assign an owner without clear evidence
- Never create a specific deadline that was not discussed
- Never combine two different people's statements

Common pitfalls to avoid:
- Confusing suggestions with confirmed decisions
- Marking items as decided when only discussed
- Inventing specific deadlines from vague timeframes
- Missing action items buried in conversation flow

Applicable scenarios:
- Client discovery meetings
- Internal project meetings
- Proposal review meetings
- Progress update meetings
- Contract negotiation meetings

Not applicable:
- Confidential HR or disciplinary meetings
- Personal one-on-one conversations
- Informal social conversations
- Medical or legal consultations

## 10. Version History

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| v1.0 | 2026-05-28 | Sarmad | Initial creation with 7-step flow and 5 quality rules |
