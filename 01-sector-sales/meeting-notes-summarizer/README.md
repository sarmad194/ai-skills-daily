# Meeting Notes Summarizer Skill

**Version:** v1.0
**Last Updated:** 2026-05-22
**Author:** Sarmad
**Category:** Sales Professional Tools

---

## What This Skill Does

Transforms messy, unstructured meeting notes into clean professional meeting summaries ready for immediate distribution to clients and management. No editing required after the skill runs.

The skill extracts key discussion points, identifies decisions made, captures all action items with owners and deadlines, and produces a formatted document that looks like it was written by a senior executive assistant.

---

## Time Saved

| Task | Before This Skill | After This Skill |
|------|-------------------|------------------|
| Writing meeting summary | 40–45 minutes | Under 2 minutes |
| Formatting document | 10–15 minutes | Zero — done automatically |
| Finding missed action items | Often missed | Systematically captured |
| Consistent team format | Varies by person | Identical every time |

---

## How to Use

### Invoke the skill with:

```
/meeting-notes-summarizer
```

### Then provide the following:

```
1. Meeting Date: [e.g., 2026-05-22]
2. Participants: [e.g., John Smith (Sales), Mary Chen (IT)]
3. Meeting Topic: [e.g., Q2 Planning Review]
4. Raw Meeting Notes: [paste your full notes here]
5. Summary Style: Professional  (or Casual — optional)
```

### That is all. The skill handles everything else.

---

## Input Required

| Parameter | Required? | What to Provide |
|-----------|-----------|-----------------|
| Meeting Date | ✅ Yes | Date of the meeting (any format) |
| Participants with roles | ✅ Yes | Full name and department/role for each person |
| Meeting Topic | ✅ Yes | The subject or title of the meeting |
| Raw Meeting Notes | ✅ Yes | Paste your notes exactly as taken — typos are fine |
| Summary Style | ⬜ Optional | Professional (default) or Casual |
| Output Language | ⬜ Optional | English (default) |

**Tip:** Your notes can be rough. Single words, fragments, shorthand — all fine. The skill is designed to work with real meeting notes, not polished writing.

---

## Output

A professionally formatted Markdown document saved as:

```
[topic]-meeting-summary-[date].md
```

**Example:** `q2-planning-review-meeting-summary-2026-05-22.md`

### The document contains:

1. **Header** — date, participants, meeting type, preparer name
2. **Executive Summary** — exactly 3–5 sentences for senior management
3. **Key Discussion Points** — bullet list of main topics raised
4. **Decisions Made** — numbered list of confirmed decisions only
5. **Action Items** — table with owner, deadline, and priority (High/Medium/Low)
6. **Next Steps** — 2–3 sentences on immediate follow-up
7. **Next Meeting** — date and topic if discussed

---

## Quality Guarantees

This skill enforces five non-negotiable quality rules before delivering output:

| Rule | What It Ensures |
|------|-----------------|
| Executive Summary is 3–5 sentences | Never too brief, never too long |
| Every action item has an owner | No "orphaned" tasks that nobody is responsible for |
| Every action item has a deadline | No vague follow-ups — flagged if unclear |
| Every action item has a priority | Teams know exactly what to focus on first |
| No invented information | Every fact traces back to your original notes |

---

## File Structure

```
meeting-notes-summarizer/
├── SKILL.md                          ← The skill file (10 sections)
├── README.md                         ← This file
└── references/
    └── output-template.md            ← The output document template
```

---

## Who This Is For

| Role | How You Use It |
|------|---------------|
| Sales Representative | Summarize client calls before sending follow-ups |
| Account Manager | Capture client requirements from discovery meetings |
| Business Development Manager | Document partner meetings and joint planning sessions |
| Pre-Sales Consultant | Record technical requirement discussions |
| Project Manager | Summarize kickoff and review meetings |

---

## Known Limitations

- Currently supports English output only (v1.0)
- Not suitable for confidential HR discussions or personal conversations
- Requires at least moderate meeting notes — very sparse notes (under 50 words) may produce limited output
- Does not connect to calendars, email, or external systems in v1.0

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1.0 | 2026-05-22 | Initial release — 7-step execution flow, 5 quality rules, full output template |

---

## Feedback and Iteration

Found a problem? Have a suggestion?

Follow the 5-step iteration process from Chapter 5 of the AI Skills Engineering manual:
1. Identify the problem clearly (one specific sentence)
2. Describe the expected behavior precisely
3. Submit an iteration command to WorkBuddy
4. Verify the fix in SKILL.md
5. Record in test-evidence.md and update version history

Every reported issue makes this skill better for the whole team.

---

*Meeting Notes Summarizer — AI Skills Engineering Portfolio*
*Part of the Sales Professional Toolkit — 01-sector-sales/*
