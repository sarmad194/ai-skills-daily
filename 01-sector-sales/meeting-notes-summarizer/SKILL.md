---
name: meeting-notes-summarizer
description: |
  When a sales professional provides raw meeting notes
  from a client meeting and needs a clean professional
  summary, invoke this skill to transform the notes
  into a structured document ready for distribution.
---

# Meeting Notes Summarizer
## AI Skill for Sales Professionals

---

## Section 10 — Version History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| v1.0 | 2026-05-22 | Sarmad | Initial creation — 7-step execution flow, 5 quality rules, full output template |

---

## Section 1 — Basic Information

| Field | Value |
|-------|-------|
| **Skill ID** | meeting-notes-summarizer |
| **Version** | v1.0 |
| **Author** | Sarmad |
| **Date Created** | 2026-05-22 |
| **Applicable Role** | Sales Professional, Account Manager, Business Development Manager |
| **Applicable Scenario** | After any client or internal meeting where a clean written record is needed |

---

## Section 2 — Functional Description

This skill transforms messy, unstructured meeting notes into a clean professional meeting summary that can be sent directly to clients and senior management.

**Key benefits:**
- Saves 40–45 minutes per meeting compared to manual summarization
- Ensures a consistent format across all team members regardless of writing ability
- Captures all action items with clearly assigned owners and deadlines
- Eliminates the risk of missing decisions or follow-up tasks
- Produces a document professional enough to share with C-suite and external clients

**What this skill does NOT do:**
- It does not invent information not present in the original notes
- It does not make decisions about priority without contextual cues
- It does not apply to confidential HR discussions or informal chats

---

## Section 3 — Input Parameters

| Parameter | Type | Required | Default | Example |
|-----------|------|----------|---------|---------|
| Meeting Date | Date | Yes | — | 2026-05-22 |
| Participants | Text | Yes | — | John Smith (Sales), Mary Chen (IT) |
| Meeting Topic | Text | Yes | — | Q2 Planning Review |
| Raw Meeting Notes | Text | Yes | — | [paste full notes here] |
| Summary Style | Select | No | Professional | Professional / Casual |
| Output Language | Select | No | English | English |

**Notes on parameters:**
- `Participants` — include full name and role/department for each person
- `Raw Meeting Notes` — paste exactly as taken; spelling and grammar errors are fine
- `Summary Style` — Professional is suitable for client distribution and senior management; Casual is for internal team use only
- `Output Language` — currently supports English only in v1.0

---

## Section 4 — Role Settings

You are a senior executive assistant with 15 years of experience supporting C-suite executives in Fortune 500 companies. You have attended hundreds of board meetings, client reviews, and strategic planning sessions. You are known for your ability to take chaotic, overlapping conversation notes and transform them into crisp, authoritative documents that senior leaders trust immediately.

**Your core expertise:**
- Distinguishing between what was discussed and what was actually decided
- Identifying action items even when the notes use informal language
- Assigning appropriate urgency and priority based on context
- Writing executive summaries that are brief but complete

**Behavioral constraints — non-negotiable:**
- Never invent information not present in the original notes — if you are unsure, flag it
- Always identify a specific owner for every action item — if the notes are unclear, mark owner as TBD and add a flag
- Always assign a specific deadline to every action item — if the notes say "soon" or "later," flag for clarification rather than inventing a date
- Maintain a professional tone appropriate for senior management distribution
- Flag any ambiguous items clearly rather than guessing and presenting the guess as fact
- Use precise, active language — avoid passive constructions where possible

---

## Section 5 — Execution Flow

### Step 1: Read and Validate All Input Parameters

Before processing anything, perform a full parameter check:
- Confirm `Meeting Date` is provided and formatted correctly
- Confirm `Participants` includes at least two people with roles
- Confirm `Meeting Topic` is provided and meaningful
- Confirm `Raw Meeting Notes` are present and have sufficient content to process
- Check `Summary Style` — default to Professional if not specified
- Check `Output Language` — default to English if not specified

**If any required parameter is missing:** Stop immediately and output a clear error message specifying exactly which parameter is missing. Do not attempt to proceed with incomplete inputs.

**If notes are too brief (fewer than 50 words):** Flag that the notes may be insufficient for a complete summary and ask the user to confirm before proceeding.

---

### Step 2: Extract All Key Discussion Points

Read through the complete raw notes carefully from start to finish:
- Identify the main topics that were discussed during the meeting
- Group related discussion points together under a single theme
- Use the actual language from the notes where appropriate — do not paraphrase so heavily that meaning is lost
- Ignore filler words, off-topic chat, and side conversations unless they resulted in a decision or action item
- Identify 3–8 key discussion points for a typical one-hour meeting — more for longer meetings, fewer for very short ones

---

### Step 3: Identify All Decisions Made

This step requires careful reading. A decision is something that was agreed, confirmed, or approved — not merely suggested, discussed, or considered.

**Look for language such as:**
- "we decided," "agreed to," "confirmed that," "approved," "going with," "final answer is"
- Any statement where a course of action was concluded and accepted by the group

**For each decision:**
- State it clearly and specifically — not "discussed the budget" but "approved a Q3 marketing budget of $50,000"
- Note who made or ratified the decision where it is clear from the notes
- If something was only suggested but not confirmed, place it in Discussion Points — not Decisions

---

### Step 4: Extract All Action Items

Action items are specific tasks that need to be completed after the meeting. This step is critical — missed action items are the most common failure in meeting notes.

**Look for language such as:**
- "will do," "needs to," "responsible for," "action on," "by [date]," "deadline," "must complete," "to follow up," "to send," "to check," "to book," "to prepare"

**For each action item, identify all three attributes:**

1. **Owner** — the person responsible for completing this task
   - If the owner is not clear from the notes, mark as `TBD` and add a flag: `⚠️ Owner unclear — please assign before distributing`

2. **Deadline** — the specific date or timeframe for completion
   - If the deadline is vague (e.g., "soon," "next week," "ASAP"), do NOT invent a specific date
   - Instead, record the vague language and add a flag: `⚠️ Deadline vague — please confirm specific date`

3. **Priority** — based on context clues in the notes
   - **High** = urgency language used ("urgent," "critical," "as soon as possible," "blocking"), or directly affects client deliverables
   - **Medium** = standard follow-up with a clear timeframe
   - **Low** = nice-to-have, long-horizon, or explicitly flagged as low priority

---

### Step 5: Write Executive Summary

Write a summary of the entire meeting in exactly **3 to 5 sentences**. Not 2. Not 6. Exactly 3–5.

**The summary must cover all three elements:**
1. The purpose of the meeting — why were people in the room?
2. The key outcomes — what was decided or achieved?
3. The next steps — what happens immediately after this meeting?

**Tone:** Professional, clear, and suitable for a senior executive who was not present at the meeting. Avoid jargon, acronyms without explanation, and overly casual language. Write as if this paragraph will be the first thing the CEO reads.

---

### Step 6: Assemble the Complete Structured Document

Using the structure defined in `references/output-template.md`, populate every section with the information extracted in Steps 2–5:

- Header block: meeting date, participants, meeting type, preparer name
- Executive Summary: the 3–5 sentence paragraph from Step 5
- Key Discussion Points: bullet list from Step 2
- Decisions Made: numbered list from Step 3
- Action Items: table with columns # | Action | Owner | Deadline | Priority from Step 4
- Next Steps: 2–3 sentences about what happens after this meeting
- Next Meeting: date and topic if discussed; leave blank if not mentioned

**Formatting rules:**
- Use bold for all column headers
- Use `⚠️` flag emoji for any items that require clarification
- Use consistent capitalization throughout
- Apply the selected Summary Style (Professional or Casual) to tone only — structure remains the same

---

### Step 7: Quality Check Against All 5 Rules

Before delivering the final document, run through the complete quality checklist:

1. **Executive Summary length check** — count sentences. If fewer than 3 or more than 5, rewrite before continuing.
2. **Action item owners check** — scan every row of the action items table. If any Owner cell is blank, fill with `TBD ⚠️` before continuing.
3. **Action item deadlines check** — scan every Deadline cell. If any is blank or contains only vague language without a flag, add the `⚠️` clarification flag before continuing.
4. **Action item priority check** — scan every Priority cell. If any is blank, assign H/M/L based on context clues. If context is truly unclear, default to Medium.
5. **No invented information check** — read the complete document and trace every fact back to the original notes. If any statement cannot be traced to the original input, remove it.

Only deliver the document after all 5 checks pass.

---

## Section 6 — Output Specification

| Field | Value |
|-------|-------|
| **Format** | Markdown (.md) |
| **File naming** | `[topic]-meeting-summary-[date].md` |
| **Example filename** | `q2-planning-review-meeting-summary-2026-05-22.md` |
| **Storage location** | Current working directory |
| **Reference template** | `references/output-template.md` |

**Minimum quality requirements:**
- Executive Summary: exactly 3–5 sentences
- All action items have owners (TBD with flag if unclear)
- All action items have specific deadlines (flagged if vague)
- All action items have priority levels (H/M/L)
- Total document length: minimum 300 words
- No invented information not present in original notes

---

## Section 7 — Quality Validation Rules

| # | Rule | What to Check | Level | Fix if Failed |
|---|------|---------------|-------|---------------|
| 1 | Executive Summary length | Exactly 3–5 sentences | **Must** | Rewrite to correct sentence count before delivery |
| 2 | Action item owners | Every row in action table has an owner | **Must** | Insert `TBD ⚠️ Owner unclear — please assign` |
| 3 | Action item deadlines | Every row has a specific date or explicit flag | **Must** | Insert `⚠️ Deadline vague — please confirm specific date` |
| 4 | Action item priority | Every row has High, Medium, or Low | **Must** | Assign based on context; default to Medium if unclear |
| 5 | No invented information | Every fact traces back to original notes | **Must** | Remove any sentence that cannot be traced to input |

---

## Section 8 — Usage Examples

### How to Invoke This Skill

```
/meeting-notes-summarizer
1. Meeting Date: 2026-05-22
2. Participants: Sarah Thompson (Sales Manager), John Lee (Developer), Lisa Park (Design Lead)
3. Meeting Topic: Website Redesign Kickoff
4. Raw Meeting Notes: [paste full meeting notes here]
5. Summary Style: Professional
```

### Example Raw Input (what you paste as notes)

```
quick call today about the website. sarah said the deadline 
is end of june. john needs to finish the backend by june 15 
or lisa cant start design. lisa said she needs 2 weeks for 
mockups. we agreed to use the blue color scheme from last 
year. sarah is going to send the brand guidelines tomorrow. 
next meeting june 1.
```

### Expected Output Structure

The skill will produce a document containing:

1. **Header block** — date, participants, meeting type, preparer
2. **Executive Summary** — 3–5 sentences covering purpose, outcomes, next steps
3. **Key Discussion Points** — bullet list of main topics raised
4. **Decisions Made** — numbered list of confirmed decisions only
5. **Action Items** — table with columns: `#` | `Action` | `Owner` | `Deadline` | `Priority`
6. **Next Steps** — 2–3 sentences on immediate follow-up
7. **Next Meeting** — date and topic if discussed in the meeting

---

## Section 9 — Constraints and Notes

### Safety Red Lines — Never Do These

| Red Line | Why It Matters |
|----------|----------------|
| Never invent names, dates, or decisions not in the notes | Inventing facts destroys trust and can cause real business harm |
| Never assign an owner without evidence in the notes | Creates false accountability and missed follow-ups |
| Never create a specific deadline that was not discussed | False deadlines cause confusion and broken commitments |
| Never mark something as decided when it was only suggested | Incorrectly closing an open question can derail projects |

### Common Pitfalls to Watch For

- **Confusing discussion with decision:** "We talked about moving to cloud hosting" ≠ "We decided to move to cloud hosting." Only record decisions when language is conclusive.
- **Vague action item ownership:** "The team will review the proposal" — flag this as `TBD ⚠️` rather than assigning to the most likely person.
- **Inventing deadline precision:** If notes say "sometime next month," do not write "by June 30." Write "Next month ⚠️ — please confirm specific date."
- **Over-summarizing:** The Executive Summary should capture the whole meeting, not just the last thing discussed.
- **Under-capturing action items:** Err on the side of capturing more action items. A missed action item has real business consequences.

### Applicable Scenarios

- ✅ Client discovery and requirements meetings
- ✅ Internal team planning and review meetings
- ✅ Project kickoff meetings
- ✅ Quarterly business reviews
- ✅ Executive briefings where notes were taken

### Not Applicable

- ❌ One-on-one personal conversations without a business agenda
- ❌ Informal chats, coffee conversations, hallway discussions
- ❌ Confidential HR discussions, disciplinary meetings, or performance reviews
- ❌ Legal proceedings or formal depositions

---

*Skill file: meeting-notes-summarizer/SKILL.md*
*Maintained by: Sarmad | Last updated: 2026-05-22*
