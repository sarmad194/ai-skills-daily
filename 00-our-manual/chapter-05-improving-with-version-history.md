# AI Skills Engineering — A Practical Guide for Everyone
## Chapter 5: Improving with Version History

---

## Introduction

By this point in your journey, you have already accomplished something most people never do. In Chapter 3 you built your first real AI skill from scratch — a SKILL.md file with an execution flow, input parameters, quality rules, and an output template. In Chapter 4 you learned how to test that skill properly, generate test evidence, and distinguish between a skill that feels good and a skill that actually performs consistently. You ran it through multiple scenarios, documented the results, and probably discovered a few things that did not work quite right.

That last part — discovering things that do not work — is not a failure. It is the whole point of testing. Every problem you found during testing is information. It is a data point telling you exactly where your skill needs to improve. And now, in Chapter 5, you are going to learn what to do with that information.

The answer is: iterate and improve.

Think about your favorite mobile app — the one you open every single day. When you first downloaded it, it probably had bugs. Buttons that did not work. Screens that crashed. Features that were confusing. The developers found those problems through testing and user feedback, fixed them, and released version 2.0. Then they kept going — version 3.0, 4.0, 5.0. Each release was better than the last. Today that app feels seamless and natural, but it took years of iteration to reach that quality level.

Your AI skill works exactly the same way. Version 1.0 is just the beginning. It is the foundation you build on, not the finished product. The professionals who build the most powerful, reliable skills are not the ones who wrote a perfect skill on the first try — they are the ones who iterated the most consistently and recorded their improvements with discipline.

This chapter teaches you the complete iteration workflow: how to identify problems clearly, how to apply fixes permanently, how to use version numbers correctly, and how to build a version history that tells a compelling story of skill growth. Every concept here directly continues the work you did in Chapters 3 and 4. By the end of this chapter, you will have a system for continuous improvement that turns your v1.0 skill into something genuinely powerful over time.

---

## Why Version History Is Not Optional

### The Problem Without Version History

Here is a cycle that frustrates beginners more than almost anything else in AI skill development. You run your skill and notice a problem — maybe the output is missing a section, or the formatting is wrong, or the tone does not match your industry. You are smart, so you tell the AI in the conversation: "Fix this, make the action items table include a Priority column." The AI does it. The output looks great. You feel good.

Then you close the conversation.

The next time you run the skill, you open a fresh conversation, paste in your SKILL.md, and provide your input. The AI runs your skill exactly as written in the file. The action items table has no Priority column. The same problem is back. You fix it again in the conversation. It looks great again. You close the conversation again. The next time — same problem again.

This cycle repeats indefinitely because you are fixing the output of the conversation, not the source of the skill. The SKILL.md file is the source of truth. If the fix is not in the file, the fix does not exist.

This is not a small inconvenience. It means every hour you spend fixing problems in conversations is wasted effort. You are running on a treadmill — moving constantly but making no forward progress. The skill does not get better. You just get more tired.

### The Solution — Update the Skill File

The solution is straightforward: every fix must be written back into SKILL.md. Every fix must also be recorded in the version history table at the top of the file. These are two separate requirements, and both are mandatory.

When you update the execution flow in SKILL.md to include the Priority column requirement in Step 5 — that fix is now permanent. Every time anyone runs the skill in any conversation, they will get Priority columns in their action items table. The fix is part of the skill's DNA.

When you record that fix in the version history with a date and description — that creates a trail of evidence showing how the skill evolved. Anyone who picks up the skill file six months later can read the history and understand exactly what improvements were made and why.

### The Golden Rule of Iteration

> **GOLDEN RULE:**
> Every fix must be written back into the skill file AND recorded in the version history.
> If you fix it only in the conversation — the next run will have the same problem.
> If you fix it in the skill file — the problem is gone forever for everyone.

Memorize this rule. Print it out if you need to. Tape it to your monitor. It is the single most important habit in AI skill engineering.

### Real-World Consequence of Ignoring This

Consider this story from a sales professional we will call Sarah. Sarah built a meeting notes skill to help her summarize client calls. She tested it, found a problem — the action items section had no priority levels, which made it hard for her team to know what to do first. She told the AI to fix it in the conversation. The output looked excellent. She was satisfied.

Then Sarah did something generous — she shared the skill file with her colleague David. David ran the skill on his own call transcript. The action items had no priority levels. He messaged Sarah: "Hey, your skill is missing priorities." Sarah fixed it again in her conversation and told David how to fix it in his. David shared the skill with two more colleagues. Both of them had the same problem. Sarah had to explain the fix two more times.

The skill had been shared four times. The fix had been applied four times in four separate conversations. But the SKILL.md file still had the original version with no Priority column — because Sarah never wrote the fix back into the file.

This is what happens without version history. You work harder to stay in the same place. Your colleagues lose trust in your skill. The improvement is invisible to everyone except you, in that one conversation, on that one day.

---

## How Version Numbers Work

### The Version Number System

Version numbers exist in virtually every piece of software you have ever used. The system is simple once you understand the logic behind it. Here is the complete framework:

- **v1.0** — First working version. Basic functionality is in place. The skill does what it was designed to do at a fundamental level.
- **v1.1** — Small fix or minor improvement. Something was slightly wrong or missing, and you corrected it.
- **v1.2** — Another small improvement on top of v1.1.
- **v1.3** — Another incremental improvement.
- **v2.0** — A major new feature or significant redesign. The skill now does something fundamentally different or more powerful than before.
- **v2.1** — A small fix on top of the major v2.0 release.
- **v3.0** — Another major redesign or capability expansion.

The pattern is clear: the number after the dot tracks small improvements, and the number before the dot tracks major transformations.

### When to Use Each Version Type

**Use v1.X increments for:**
- Bug fixes (something was broken, now it works)
- Word count or length improvements (output was too short or too long)
- Adding missing sections that should have been in v1.0
- Improving quality validation rules to catch more edge cases
- Fixing formatting issues (tables were misaligned, headers were wrong)
- Adjusting tone or language to better match your audience
- Correcting factual or structural errors in the output template

**Use vX.0 major releases for:**
- Adding completely new input parameters that change what the skill can do
- Redesigning the execution flow from the ground up
- Adding support for entirely new industries, contexts, or use cases
- A major template redesign that changes the output structure significantly
- Adding a new capability that did not exist before (like support for video transcripts, or a second language output, or integration with a new data format)

The key question for major vs. minor: "Does this change what the skill fundamentally does, or does it just do the same thing better?" Better = minor. Fundamentally different = major.

### Practical Example — Meeting Notes Skill Version Timeline

Here is what a healthy iteration history looks like for a simple meeting notes skill, showing both minor and major progression over time:

- **v1.0** — Initial creation with basic 6-step flow and 5 quality rules
- **v1.1** — Added Priority column to action items table
- **v1.2** — Fixed vague deadline handling — now flags "TBD" deadlines with a warning
- **v1.3** — Added industry terminology adaptation for medical context
- **v1.4** — Improved Executive Summary to always be exactly 3–5 sentences
- **v2.0** — Major update — added full support for video call transcript inputs
- **v2.1** — Fixed character encoding issue with special characters in names

Notice how each entry is specific. You can read this history and immediately understand what each version added without having to open the skill file and compare versions manually. That clarity is the goal.

For a lawyer: the same pattern applies to a contract review skill — v1.0 catches basic issues, v1.1 adds missing clause detection, v1.2 handles international jurisdiction cases, v2.0 adds support for a second document type entirely.

For a nurse: a patient discharge summary skill might go v1.0 basic structure, v1.1 medication allergy warnings added, v1.2 follow-up appointment formatting improved, v2.0 now handles pediatric cases with different templates.

The profession changes. The version number system stays exactly the same.

---

## The Iteration Process — Step by Step

The 5-step iteration process gives you a repeatable framework for every improvement you make to any skill, in any profession, at any level of experience. Follow these steps every single time you find a problem during testing.

### Step 1 — Identify the Problem Clearly

Vague problem descriptions lead to vague fixes. A vague fix often introduces new problems or fails to solve the original one. Be ruthlessly specific about what is wrong before you attempt any fix.

**Wrong (too vague):**
> "The output is not good enough."

**Right (specific and actionable):**
> "The action items table is missing a Priority column showing High, Medium, or Low — making it impossible for team members to know which tasks to complete first."

Write the problem in one clear sentence. If you cannot describe the problem in one sentence, you do not understand it well enough yet. Keep observing the output until you can articulate exactly what is missing, wrong, or inconsistent.

A human resources professional reviewing a job posting skill might write: "The skill does not adjust the required qualifications section when the seniority level is Junior versus Senior — both outputs are identical."

A financial analyst using a report generation skill might write: "The executive summary never mentions the risk level, even when the risk section of the report identifies multiple high-severity concerns."

Specific problems get specific fixes. Vague problems get vague fixes that do not last.

### Step 2 — Describe the Expected Behavior

Once you know what is wrong, you must describe what correct looks like. This is your specification for the fix. Again, specificity is everything.

**Wrong:**
> "Make it better."

**Right:**
> "Each action item in the table should have a Priority column. The value should always be one of three options: High, Medium, or Low. High means the task must be completed this week. Medium means this month. Low means when time allows. The Priority column should appear as the third column in the table, between Owner and Deadline."

Notice the detail: what the column is called, what values it accepts, what those values mean, and where it should appear. That level of detail leaves nothing ambiguous for the AI when it applies the fix.

A teacher using a lesson plan skill might specify: "The learning objectives section should always contain exactly 3 bullet points, each starting with a measurable action verb (such as: identify, explain, demonstrate, compare, create), and each objective should be achievable within a single 45-minute class session."

A customer service manager using a complaint response skill might specify: "The response must always acknowledge the specific problem mentioned by the customer in the first sentence — not a generic 'I understand your frustration' but a sentence that names the actual issue they reported."

### Step 3 — Write the Iteration Command

Use this exact template when giving WorkBuddy the instruction to fix your skill:

```
Please fix the following issue in the [skill-name] skill 
and update the SKILL.md file and any relevant scripts 
or templates.

Record this as version [X.X] with today's date 
and the following change description: [your description]

Issue found:
[Describe the problem in one clear sentence]

Expected behavior:
[Describe exactly what should happen instead]

Files to update:
- [skill-name]/SKILL.md (execution flow, quality rules)
- [skill-name]/references/[template-file].md (if the template needs updating)
```

Do not skip any part of this template. Each section serves a purpose:
- The version number tells WorkBuddy to update the history table
- The issue description ensures the AI understands what is broken
- The expected behavior gives the AI its target for the fix
- The files list prevents the AI from forgetting to update all relevant files

### Step 4 — Verify the Fix

After WorkBuddy makes the fix, do not immediately celebrate. Verify it. Open the updated SKILL.md and read the execution flow section. Find the step that was changed. Confirm the new behavior is explicitly stated in the text of that step — not implied, not adjacent to it, but actually written there.

Then scroll to the version history table at the top of the file. Confirm that a new row has been added with the correct version number, today's date, and an accurate description of the change. If the version history was not updated, ask WorkBuddy to add it before moving on.

Finally, run the skill again with the same test input that originally revealed the problem. Confirm with your own eyes that the problem is gone. Do not assume the fix worked — verify it produces the expected output before recording it as resolved.

### Step 5 — Record in Your Test Evidence File

Open your test-evidence.md file from Chapter 4 and add a new iteration entry:

```markdown
## Iteration Record — Version [X.X] — [date]

**Problem found:** [description of what was wrong]
**Root cause:** [why it was happening]
**Fix applied:** [what was changed in SKILL.md]
**Files updated:** SKILL.md / references/template.md
**Test result after fix:** Pass ✅ / Fail ❌
**Notes:** [any observations about the fix or related issues]
```

This creates a permanent record that links your test evidence to your version history. Six months from now, if someone asks "why did you add this rule in v1.3?" — you can open your test evidence file and show them exactly what triggered it.

---

## The Exact Iteration Command Format

The previous section showed a general template. This section gives you the full professional-grade iteration command with every field filled in — the exact language to use with WorkBuddy when you are ready to improve your skill.

### The Complete Template Command

```
Please optimize the following issue found during testing 
of the [skill-name] skill.

Update these files:
1. [skill-name]/SKILL.md
2. [skill-name]/references/[template-file].md (if needed)

Issue identified during testing:
[Describe the problem in one clear, specific sentence]

Root cause:
[Explain why this problem occurs — what is missing or 
wrong in the current SKILL.md that causes this behavior]

Required fix:
[Describe exactly what needs to change — which step, 
which rule, which part of the template, and what the 
new text should say]

After fixing, please:
1. Update the relevant step(s) in the execution flow in SKILL.md
2. Update the quality validation rules in SKILL.md if needed
3. Update the output template in references/ if needed
4. Add a new row to the version history table:
   | v[X.X] | [today's date] | [your name] | [change description] |
5. Confirm all changes have been saved and list which files were modified
```

This command is thorough without being complicated. You are telling WorkBuddy exactly what the problem is, why it happens, what the fix should be, and where to record it. The final confirmation step ensures you get a clear report of everything that changed so you can verify it.

### A Real Example — Meeting Notes Skill Iteration

Here is the exact command a project manager might send to improve their meeting notes skill:

```
Please optimize the following issue found during testing 
of the meeting-notes-summarizer skill.

Update these files:
1. meeting-notes-summarizer/SKILL.md
2. meeting-notes-summarizer/references/output-template.md

Issue identified during testing:
The action items table does not include a Priority column, 
making it difficult for teams to know which tasks 
to focus on first.

Root cause:
The output template and execution flow Step 5 do not 
specify a Priority column in the action items table. 
The current template only has: Task | Owner | Deadline.

Required fix:
1. Add a Priority column (High / Medium / Low) to the 
   action items table in output-template.md — place it 
   between Owner and Deadline.
2. Update Step 5 of the execution flow in SKILL.md to 
   explicitly instruct the AI to assign a priority level 
   to each action item based on urgency and impact.
3. Update Quality Rule 1 to check that every action item 
   has a Priority value — flag as error if any are blank.

After fixing, please add to version history:
| v1.1 | 2026-05-28 | Sarmad | Added Priority column 
(High/Medium/Low) to action items table to support 
better team task prioritization |
```

Every part of this command is precise. Notice how it names the specific step (Step 5), the specific rule (Quality Rule 1), the specific column position, and the exact values the Priority field should accept. A doctor writing a patient intake skill iteration command would use the same structure — just with different steps, rules, and field names relevant to their context.

A teacher improving a lesson plan skill might specify that the learning objectives step needs to be updated. A financial analyst improving a quarterly summary skill might specify that the risk section step needs a minimum threshold before flagging. The command format is universal. Only the content changes.

---

## Building a Version History That Impresses

### What a Great Version History Looks Like

The version history table lives at the very top of your SKILL.md file, just below the title and description. It is the first thing anyone sees when they open your skill file. A rich, well-maintained version history immediately communicates that this is a professional, reliable skill — not an experiment that was tried once and abandoned.

Here is a complete example of an impressive version history for a meeting notes skill:

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-22 | Sarmad | Initial creation with 6-step flow and 5 quality rules covering basic meeting summarization |
| v1.1 | 2026-05-22 | Sarmad | Added Priority column (High/Medium/Low) to action items table to support team task prioritization |
| v1.2 | 2026-05-23 | Sarmad | Fixed vague deadline handling — execution flow now flags "TBD" deadlines with a warning note |
| v1.3 | 2026-05-24 | Sarmad | Added industry terminology adaptation — new input field allows users to specify their sector for appropriate vocabulary |
| v1.4 | 2026-05-25 | Sarmad | Improved Executive Summary rule — now enforces exactly 3–5 sentences with mandatory mention of the most critical decision |
| v2.0 | 2026-06-01 | Sarmad | Major update — added complete support for video call transcript inputs including timestamps and speaker identification |
| v2.1 | 2026-06-03 | Sarmad | Fixed encoding issue with special characters in participant names (international colleagues) |

Every row tells a story. Every change has a date. Every description is specific enough that someone reading it understands exactly what changed without needing to compare file versions manually.

### Why This Impresses Managers and Colleagues

When a manager or senior colleague opens a skill file and sees a version history like the one above, several things register immediately:

- **Systematic thinking.** This person does not just try things randomly — they test, identify problems precisely, and fix them methodically.
- **Learning from problems.** Every entry in the history represents a problem that was found and resolved. That is intellectual honesty in action.
- **Documentation discipline.** They took the time to record their work clearly, which means other people can benefit from it and maintain it.
- **Active maintenance.** This skill has been cared for. It is not a one-time creation — it has been improved seven times. It has probably been used seriously.
- **Professional software habits.** This is exactly how professional software development teams operate. Applying these habits to AI skills signals high competence.

In a team environment, a well-documented skill with version history is an asset that the whole organization can rely on. A skill without version history is a black box that nobody fully understands. The difference matters enormously when someone new joins the team and needs to use or extend your skill.

### The Compound Effect of Iteration

Here is a way to think about the long-term value of consistent iteration. Imagine your skill quality on a scale from 0 to 100:

- **v1.0** — Perhaps 60% quality. It works, but with notable gaps.
- **v1.5** — Perhaps 78% quality. The most critical gaps have been fixed.
- **v2.0** — Perhaps 90% quality. Major capability expansion and multiple rounds of refinement.
- **v2.5** — Perhaps 95% quality. Edge cases handled, language polished, reliability high.

Each small improvement compounds on the ones before it. After 10 iterations your skill is dramatically more reliable and useful than v1.0. After 50 iterations it is genuinely professional-grade — the kind of tool that your colleagues ask to use because it consistently delivers excellent results.

This is how individual expertise becomes organizational knowledge. A skill that has been iterated 30 times by one thoughtful person contains the accumulated learning of every problem that person encountered and solved. It is expertise made permanent — no longer locked inside one person's head, but encoded in a file that anyone on the team can use and that will outlast any individual's time at the company.

---

## When to Share vs When to Keep Improving

### The Sharing Readiness Checklist

One of the most common mistakes beginner skill engineers make is hoarding their skills — keeping them private and continuing to improve them indefinitely instead of sharing them. The opposite mistake is sharing too early, before the skill is reliable enough to be useful to others. Here is the checklist that helps you find the right moment:

- [ ] **Level 1 functionality test passed** — The skill completes successfully on a standard input without errors
- [ ] **At least one iteration made (v1.1 exists)** — You have found at least one problem and fixed it, which means you have done real quality checking
- [ ] **Version history is documented** — The SKILL.md file has a version history table with at least two rows
- [ ] **README explains how to use the skill** — Someone new to the skill can understand the input requirements and what the output will look like
- [ ] **Test evidence file exists** — You have documentation showing you ran the skill on real inputs and evaluated the results

When all five boxes are checked, your skill is ready to share. You do not need it to be perfect. You need it to be reliable and transparent.

### Do Not Wait for Perfection

Many people never share their skills because they keep thinking "it needs one more improvement." This is a trap. There is always one more improvement. Waiting for perfection means waiting forever.

Share at v1.1 or v1.2. Let colleagues use it and give you feedback. Their feedback is more valuable than anything you can discover through solo testing, because they will use the skill in contexts you never anticipated. They will provide inputs you would never have tried. They will notice problems that your familiarity with the skill has made invisible to you.

A lawyer who shares their contract review skill with a paralegal will discover edge cases in contract language they never personally handle. A doctor who shares their patient notes skill with a nurse will discover that the output format is incompatible with the hospital's intake form. A sales professional who shares their proposal skill with a junior colleague will discover that the input instructions were unclear to someone who was not in the room when the skill was built.

Every piece of feedback from real usage is a gift. It is a v1.3 or v1.4 improvement delivered to you for free. The sooner you share, the faster your skill improves.

### The Sharing Command

When you are ready to share your skill with a colleague, use this simple process:

1. Locate your skill folder (e.g., `meeting-notes-summarizer/`)
2. Copy the entire folder — including SKILL.md, references/, and your test-evidence.md
3. Share it with one colleague first (not the whole team)
4. Ask them specifically: "Please try this skill on one of your real inputs and tell me any problems you notice"
5. Take their reported problems, run each one through the 5-step iteration process, and release v1.2 or v1.3

Starting with one colleague rather than broadcasting to the whole team reduces embarrassment if there are obvious problems, gives you focused feedback from a single trusted source, and lets you improve before wider adoption. After one round of iteration with one colleague, you will be much more confident sharing broadly.

---

## Chapter Summary

You have now completed the full foundation of AI skill engineering. Let us bring together everything this chapter covered.

**Version history is not optional.** Without it, every fix you make exists only in a single conversation and disappears the moment that conversation closes. The only permanent improvements are the ones written into the SKILL.md file and recorded in the version history table.

**The Golden Rule is the foundation of everything:** fix the skill file, not just the conversation. If you take nothing else from this chapter, take this rule. It separates skill engineers who improve continuously from beginners who fix the same problems repeatedly.

**Version numbers follow a predictable system.** Use v1.X increments for small improvements, bug fixes, and refinements. Use vX.0 major releases when you add fundamentally new capabilities or redesign the core structure. Keep your version numbers honest — do not call something a major release if it is just a small adjustment.

**The 5-step iteration process is your repeatable framework.** Identify the problem specifically. Describe the expected behavior precisely. Write the iteration command using the provided template. Verify the fix was applied correctly. Record the improvement in your test evidence file. These five steps apply to every skill, in every profession, at every level of experience.

**The exact command template removes all ambiguity.** When you give WorkBuddy a precise, structured instruction for a fix — naming the problem, the root cause, the required change, and the version number — you consistently get clean, accurate updates to your skill files. Vague instructions get vague results.

**A well-maintained version history is a professional asset.** It demonstrates systematic thinking, learning discipline, and documentation maturity. In a team setting, it transforms your personal skill into organizational knowledge that everyone can rely on.

**Share early and improve from real feedback.** Check the five-item sharing readiness list. When all boxes are checked, share with one colleague and collect their real-world problems. Their feedback is your best source of iteration items and will improve your skill faster than any amount of solo testing.

The compound effect of iteration is real. A skill at v1.0 is a beginning. A skill at v2.0 — with dozens of real-world improvements behind it — is a genuinely powerful tool that saves time, improves quality, and scales your expertise to everyone who uses it.

---

## What Is Coming in Chapter 6

Chapter 6 is the first sector-specific chapter in this manual, and it is where everything you have learned in Chapters 1 through 5 comes together in a focused, practical way. We move out of general principles and into a specific professional world: the Sales and Pre-Sales professional.

If you work in sales, pre-sales consulting, business development, account management, or any client-facing commercial role — Chapter 6 was written specifically for you. Even if you do not work in sales, reading Chapter 6 will show you exactly how to apply the complete skill engineering methodology to a specific domain, giving you a template you can replicate in your own field.

In Chapter 6 we will build three complete, production-ready skills from scratch:

1. **Customer Research Report Generator** — A skill that takes a company name and context, and produces a structured 5-section research report that a sales professional can use before a client meeting.
2. **Technical Proposal Writer** — A skill designed for pre-sales and solution consultants that generates a structured technical proposal document from a requirements summary and solution approach.
3. **Competitor Analysis Skill** — A skill that takes a competitor name and your own product context, and generates a structured head-to-head comparison that helps sales teams position their solution effectively.

Each of these three skills will be built using the Chapter 3 method, tested using the Chapter 4 protocol, and iterated using the Chapter 5 framework. By the end of Chapter 6 you will have a complete, tested, iterated sales skill toolkit that is ready to use in your real job on your next real client opportunity.

Chapter 6 is where theory becomes practice in your daily professional life. See you there.

---

*Chapter 5 complete — AI Skills Engineering: A Practical Guide for Everyone*
*Next: Chapter 6 — Skills for the Sales Professional*
