# AI Skills Engineering — A Practical Guide for Everyone
## Chapter 3: Your First Skill in 30 Minutes

---

### Introduction — What You Will Build Today

Stop reading for a moment and look at your calendar. How many meetings do you have this week? Three? Five? Eight? Now think about what happens after each one. Someone — maybe you — has to capture what was discussed, who is doing what, and when things are due. That task typically lands in a document full of half-sentences, abbreviations, and notes that only made sense in the room. Turning those messy notes into a professional summary that you can actually send to your manager or your client takes anywhere from 30 to 60 minutes. Every single time.

By the end of this chapter, that task will take you under 2 minutes.

This chapter is different from the previous ones. We have been building up theory — understanding what a Skill is, learning the 5-Step Method in detail. Now we put down the textbook and pick up the tools. Everything you do in the next 30 minutes is real. The Skill you are about to build is not a practice exercise. It is not a simulation. It is a fully functioning AI Skill called **meeting-notes-summarizer** that you can invoke in your actual job, with your actual meeting notes, starting tomorrow morning.

Here is exactly what we are building:
- **Input:** Your raw, messy meeting notes — just paste them in
- **Output:** A clean, structured, professional meeting summary ready to send

This skill works for every profession. Sales teams use it to capture client conversations. Teachers use it after staff meetings. Doctors use it after case conferences. Project managers use it after sprint reviews. Finance teams use it after investor calls. If you attend meetings — and every professional does — this skill will save you time every single week for the rest of your career.

Here is what you need to complete this chapter successfully:
- **Time required:** Approximately 30 minutes
- **Tools needed:** WorkBuddy (free) or any AI coding assistant
- **Prior experience:** Zero. None. Not a single line of code in your life? Perfect. You are exactly who this chapter was written for.

We chose the meeting notes summarizer for your first Skill because it hits every requirement: it is universally needed, the output has a clear structure, the input is always messy in the same way, and it demonstrates all five steps of the method in a satisfying, real-world context. Let us begin.

---

### Before You Start — 5-Minute Setup

Before we write a single line, let us make sure you have everything you need. This setup takes less than five minutes and you only have to do it once. Think of it as setting out your ingredients before you start cooking. A professional chef never reaches into a cabinet mid-recipe. Everything is ready before the heat goes on.

Here is your complete checklist:

**1. A computer with internet access**
Any computer works. Mac, Windows, or Linux. A tablet with a keyboard can work in a pinch, but a proper computer will make the experience much smoother. Make sure your internet connection is stable — you will be working with WorkBuddy throughout this chapter.

**2. WorkBuddy installed and open**
WorkBuddy is the AI coding and skill-building assistant we use throughout this book. If you have not installed it yet, visit the official site and follow the installation instructions — it takes about 3 minutes. Once installed, open it now. You should see a clean workspace with a chat input area. That is your workspace.

**3. A folder created on your Desktop called: `my-first-skill/`**
This is where your Skill will live. Create a new folder on your Desktop right now and name it exactly: `my-first-skill` (all lowercase, with the hyphen). This small habit — keeping your skills in organized folders — is a professional practice that will serve you well as your skill library grows.

**4. A text editor open and ready**
Notepad (Windows) or TextEdit (Mac) is completely fine. You will use it to keep notes, copy prompts, and track your progress. Nothing fancy needed.

**5. 30 minutes of uninterrupted time**
This is not negotiable. Close your email. Put your phone face down. Tell your colleagues you are in a focus session. Interruptions in the middle of a skill build are frustrating, and they break your momentum. Protect this time. You are investing 30 minutes today to save hundreds of hours in the future. That is one of the best trades available to any professional.

**6. Excitement and curiosity — that is all!**
You do not need to know how to code. You do not need to understand AI architecture. You do not need any technical background at all. You need the same thing you needed to bake your first cake from a recipe: the willingness to follow instructions and the curiosity to see what happens. Everything else, this chapter provides.

Ready? Let us count down.

---

### Minute 0–5: Step 1 — Scene Recognition

The clock starts now. This first five minutes is about understanding the problem you are solving at the deepest level. This is the step most beginners want to skip — "Can we just get to building it?" — but it is the step that separates skills that actually get used from skills that sit in a folder, forgotten after the first week.

Here is the scenario we are solving together.

#### The Scenario

You are a professional. Your title does not matter — you could be a Sales Representative, a Project Manager, a School Principal, a Hospital Administrator, or a Financial Advisor. What matters is this: you attend meetings regularly, and after every meeting, someone has to write up what happened.

Right now, that process looks like this:
- You leave the meeting with some scribbled notes, a few voice memos, and a blurry memory of who said what
- You sit down to write it up and realize your notes are incomplete
- You spend 30–45 minutes turning chaos into something readable
- You send it to the team, and half of them reply with corrections because they remember things differently
- This happens after every single meeting, every single week

With the skill you are about to build, the process looks like this:
- You paste your messy notes into WorkBuddy
- You type one command
- In under 90 seconds, you have a structured professional summary
- You review it, confirm it is accurate, and send it immediately

Now let us answer the three diagnostic questions from Chapter 2 for this exact scenario.

#### Question 1 — What is the Business Objective?

> **Transform messy, informal meeting notes into a clean, structured, professional summary that can be sent directly to all meeting participants — including senior management — immediately after the meeting ends.**

The key word here is "immediately." The value of a meeting summary drops with every hour it is delayed. People forget. Action items get lost. The skill must produce output fast enough that you can send it before you even leave the building.

#### Question 2 — What are the Key Variables?

Every time you use this skill, some things will change (the content) and some things stay the same (the structure). The things that change are your **input parameters**. For this skill they are:

- **Meeting date and time** — so the summary is properly time-stamped
- **Participant names and roles** — so action items are assigned to real people
- **Meeting topic or project name** — so the summary can be filed correctly
- **The raw meeting notes** — this is the main input, the messy stuff we are cleaning up
- **Output format preference** — professional vs. casual, depending on your audience

#### Question 3 — What are the Constraints?

This is where your professional judgment comes in. These are the rules the AI must follow, non-negotiably:

- **Never invent information.** If a deadline was not mentioned in the notes, the skill must not make one up.
- **Every action item must have an owner.** "Someone will follow up" is not acceptable.
- **Every action item must have a deadline.** "Soon" is not acceptable.
- **The output must be professional enough to send to senior management.** No slang, no abbreviations, no half-sentences.

#### Your Turn

Before moving to Step 2, take two minutes to write down your own answers to these three questions — not for this meeting notes scenario, but for a repetitive task in your own job. What task drains 30 minutes of your day that follows the same structure every time? What are the key inputs? What are the rules it must never break?

This is not homework. This is preparation. By the time you finish this chapter, you will have a second skill idea already mapped in your head, ready to build next week.

---

### Minute 5–15: Step 2 — Design Your Skill

Now we move from problem analysis into design. Think of this step as drawing the blueprint before construction begins. An architect does not show up at a building site and start laying bricks — they design the building first, on paper, where changes are free and fast. You are doing the same thing here.

#### Input Parameters Table

The first design decision is: what information does the skill need to do its job? Here is the complete parameter design for the meeting-notes-summarizer:

| Parameter | Required? | Default Value | Example |
|---|---|---|---|
| Meeting Date | Yes | — | May 22, 2026 |
| Participants | Yes | — | Sarah (Manager), John (Dev) |
| Meeting Topic | Yes | — | Q2 Planning Review |
| Raw Meeting Notes | Yes | — | [paste your notes here] |
| Summary Style | No | Professional | Professional / Casual |
| Output Language | No | English | English / Chinese / Spanish |

**Why this table matters:** Required parameters are non-negotiable — the skill cannot run without them. Optional parameters have defaults, so if you do not specify them, the skill still works sensibly. This design pattern makes your skill both flexible and foolproof.

Notice that "Output Language" defaults to English but can be changed. A sales team in Shanghai can set it to Chinese. A team in Madrid can set it to Spanish. You built this capability in once, and it works everywhere.

#### Execution Flow Design

This is the heart of the skill — the exact sequence of steps the AI will follow, every single time, without deviation. Think of it as the assembly line instructions at a factory: same steps, same order, same quality check at the end.

Here are the 6 execution steps for the meeting-notes-summarizer:

| Step | What Happens |
|---|---|
| **Step 1** | Read and confirm all input parameters are present |
| **Step 2** | Extract key discussion points from the raw notes |
| **Step 3** | Identify all action items and match each one to an owner |
| **Step 4** | Identify all decisions that were made (not just discussed — decided) |
| **Step 5** | Structure everything into the professional output format |
| **Step 6** | Run quality validation: confirm every action item has an owner AND a deadline |

Step 6 is the quality gate. Just like a factory worker who checks every product before it leaves the line, the skill inspects its own output before delivering it to you. If an action item is missing an owner, the skill flags it for your attention rather than silently handing you an incomplete document.

#### Output Specification

Knowing what the output looks like before you build the skill is one of the most important design habits in Skill Engineering. Here is the complete output structure:

```
## Meeting Summary

**Date:** [Meeting Date]
**Participants:** [Names and Roles]
**Topic:** [Meeting Topic]

---

### Executive Summary
[3–5 sentences summarizing the meeting purpose and main outcomes]

---

### Key Discussion Points
- [Point 1]
- [Point 2]
- [Point 3]

---

### Decisions Made
1. [Decision 1]
2. [Decision 2]

---

### Action Items

| # | Action | Owner | Deadline | Priority |
|---|---|---|---|---|
| 1 | [Action description] | [Name] | [Date] | High/Med/Low |

---

### Next Steps
[Brief paragraph on immediate next steps]

### Next Meeting
[Date and time if mentioned in the notes]
```

Every section has a purpose. The Executive Summary is for busy executives who only read the top. The Action Items table is for the team members who need to know what to do next. The Decisions Made section is the institutional memory — it answers the question "Wait, did we agree on that?" six weeks later when no one remembers.

#### Quality Validation Rules

Before you move to building, write down these five rules on a piece of paper. These are the rules your skill will use to evaluate its own output:

- **Rule 1:** Every action item must have an owner (a person's name, not "the team")
- **Rule 2:** Every action item must have a deadline (a specific date, not "ASAP")
- **Rule 3:** The Executive Summary must be exactly 3–5 sentences — not 2, not 6
- **Rule 4:** No information may appear in the output that was not in the original notes
- **Rule 5:** The tone and vocabulary must be suitable for senior management

These rules are the difference between a skill that produces professional output and one that produces almost-professional output. Almost professional is not good enough for something you are sending to your manager.

---

### Minute 15–25: Step 3 — Build Your SKILL.md

Here is where the magic happens. You are going to talk to WorkBuddy, and it is going to build your skill for you. This is the meta-moment: you are using AI to build an AI skill. Welcome to the future.

#### Open WorkBuddy

1. Launch WorkBuddy on your computer
2. Look for the **Auto** mode selector in the interface — make sure it is set to **Auto**
3. Click the workspace/folder selector and navigate to the `my-first-skill/` folder you created on your Desktop
4. You should now see `my-first-skill/` listed as your active workspace

> **What you should see:** A clean workspace with the folder name shown at the top or in the sidebar. The chat input box is at the bottom. There are no files yet — that is correct. The folder is empty. You are about to fill it.

#### Copy This Exact Prompt

Below is the exact prompt you will paste into WorkBuddy. Do not paraphrase it. Do not shorten it. Copy it exactly, word for word. The precision of your instructions directly determines the quality of what WorkBuddy builds.

---

**📋 COPY FROM HERE:**

```
Please create a complete skill package for a meeting notes summarizer skill.

Skill name: meeting-notes-summarizer
Save location: current workspace (my-first-skill/)

Create the following files:
1. meeting-notes-summarizer/SKILL.md
2. meeting-notes-summarizer/references/output-template.md

The SKILL.md must contain all 10 standard sections:

1. Basic Information
   - Skill ID: meeting-notes-summarizer-v1
   - Version: v1.0
   - Creation Date: today's date
   - Author: [your name]
   - Category: Productivity / Meeting Management

2. Functional Description
   Transforms messy, informal meeting notes into a clean, structured,
   professional meeting summary suitable for sending to all participants,
   including senior management, immediately after the meeting.

3. Input Parameters
   - Meeting Date (required): The date the meeting took place
   - Participants (required): Names and roles of all attendees
   - Meeting Topic (required): The subject or project name for the meeting
   - Raw Meeting Notes (required): The unstructured notes to be processed
   - Summary Style (optional, default: Professional): Professional or Casual
   - Output Language (optional, default: English): Language for the summary

4. Role Settings
   You are an experienced Executive Assistant with 10+ years supporting
   C-suite executives in corporate environments. You produce meeting
   summaries that are clear, complete, and professional. You never
   invent information. You always ensure every action item has a named
   owner and a specific deadline.

5. Execution Flow
   Step 1: Confirm all required input parameters are present
   Step 2: Extract key discussion points from the raw notes
   Step 3: Identify all action items and assign each to a named owner
   Step 4: Identify all decisions made (decided, not just discussed)
   Step 5: Structure everything using the output-template.md format
   Step 6: Quality validation — verify every action item has owner AND deadline

6. Output Specification
   Refer to references/output-template.md for the complete output structure.
   The output must include: Meeting Header, Executive Summary (3-5 sentences),
   Key Discussion Points, Decisions Made, Action Items Table, Next Steps,
   and Next Meeting Date (if mentioned in the notes).

7. Quality Validation Rules
   Rule 1: Every action item must have a specific owner (not "the team")
   Rule 2: Every action item must have a specific deadline (not "ASAP")
   Rule 3: Executive Summary must be exactly 3–5 sentences
   Rule 4: No information may appear that was not in the original notes
   Rule 5: Tone and vocabulary must be suitable for senior management

8. Usage Examples
   Example invocation:
   /meeting-notes-summarizer
   - Meeting Date: May 22, 2026
   - Participants: Sarah (Manager), John (Dev), Lisa (Designer)
   - Meeting Topic: Website Redesign Kickoff
   - Raw Meeting Notes: [paste notes here]
   - Summary Style: Professional

9. Constraints
   - NEVER invent dates, names, decisions, or action items not in the notes
   - ALWAYS include owner and deadline for every action item
   - If a deadline is not mentioned, note it as "[To be confirmed]" NOT a made-up date
   - If an owner is unclear, flag it as "[Owner: TBC]" NOT guess a name
   - Maintain confidentiality: do not echo sensitive information unnecessarily

10. Version History
    v1.0 — Initial creation. Core functionality for meeting note summarization.

The output-template.md should contain the full meeting summary template
with all sections clearly labeled and placeholder text showing where each
type of content belongs.

Please confirm when both files are created and show me the file structure.
```

**📋 COPY TO HERE**

---

#### Paste and Send

Paste the entire prompt into WorkBuddy's chat input and press Enter (or click Send). Then watch.

> **What you should see within 30–60 seconds:**
> WorkBuddy will begin working. You will see it thinking, then generating content. When it finishes, you should see:
> - A confirmation message: "Skill package created successfully" (or similar)
> - The file structure showing `meeting-notes-summarizer/SKILL.md` and `meeting-notes-summarizer/references/output-template.md`
> - A summary of what was created, often with the first few lines of the SKILL.md shown
>
> In your `my-first-skill/` folder on your Desktop, you can now navigate to `meeting-notes-summarizer/` and see both files sitting there, ready to use.

If WorkBuddy shows an error or seems confused, do not panic. This happens occasionally. Simply type: "Please try again and create the meeting-notes-summarizer skill package as described above." WorkBuddy will retry. Errors are not failures — they are feedback. This is true in Skill Engineering and in life.

#### Verify the Output

Once the files are created, open `SKILL.md` in your text editor. Scroll through it and check that all 10 sections are present. You do not need to read every word right now — you will do that during testing. For now, just confirm the sections exist and the file looks substantial. A proper SKILL.md for a skill like this should be at least 100–150 lines long.

> **Feeling proud?** You should be. You just created your first skill file. It exists. It is real. It is sitting in a folder on your computer right now, ready to do work for you.

---

### Minute 25–28: Step 4 — Test Your Skill

Building a skill without testing it is like buying a car and never turning on the engine. The test is where you find out if everything you designed actually works in practice. And more importantly, it is where you experience the satisfaction of seeing your work deliver real value.

We are going to test your new skill with a realistic set of meeting notes. These notes are intentionally messy — that is the point. Real meeting notes are never clean.

#### Your Test Meeting Notes

Here are the sample notes you will use for the test. Copy them exactly — every typo, every abbreviation, every incomplete sentence. That is what real meeting notes look like.

---

**📋 SAMPLE MEETING NOTES — COPY THESE:**

```
Date: May 22 2026
Attendees: Sarah (Manager), John (Developer), Lisa (Designer), Mike (Sales)

talked about new website project
Sarah said deadline is June 30 — this is firm, client signed off
john needs to finish the backend by june 15 no excuses
Lisa — mockups to be sent by May 28. she mentioned she needs the brand guidelines first. 
    Mike said he will send brand guidelines to lisa by tomorrow (may 23)
Mike worried about client presentation — thinks demo needs to wow them
We decided to do a live demo on June 20 before final delivery
Mike will make the demo slides - deadline june 18
Budget — Sarah approved 50,000 for design phase. went over the cost breakdown briefly.
    everyone agreed the numbers looked ok
next meeting — may 29 10am. Sarah's office.
open issue: we still need to assign someone to QA testing. sarah said she will confirm by friday
```

**📋 COPY TO HERE**

---

#### Your Test Invocation Command

Now type this exact command into WorkBuddy to invoke your new skill:

---

**📋 COPY THIS INVOCATION:**

```
/meeting-notes-summarizer

Meeting Date: May 22, 2026
Participants: Sarah (Manager), John (Developer), Lisa (Designer), Mike (Sales)
Meeting Topic: New Website Project — Planning Meeting
Raw Meeting Notes:
[paste the sample meeting notes above here]
Summary Style: Professional
Output Language: English
```

**📋 COPY TO HERE**

---

Replace `[paste the sample meeting notes above here]` with the actual sample notes you copied, then send the message.

#### What a Successful Output Looks Like

Within 60–90 seconds, you should receive a clean, professional meeting summary. Here is what to look for:

**✅ Signs of success:**
- A proper meeting header with date, participants, and topic
- An Executive Summary of 3–5 complete, professional sentences
- A bulleted list of Key Discussion Points (should capture the website, timeline, budget)
- A Decisions Made section listing at least 2 clear decisions (June 30 deadline, June 20 demo)
- An Action Items table with at minimum 4 rows — one for John, one for Lisa, one for Mike (brand guidelines), one for Mike (demo slides) — each with a specific owner and deadline
- The next meeting date (May 29, 10am, Sarah's office)
- A flag or note about the open QA testing assignment

**🔎 What to check carefully:**
- Did every action item get a deadline? John: June 15. Lisa: May 28. Mike brand guidelines: May 23. Mike slides: June 18.
- Did the skill handle the "open issue" about QA correctly? It should flag `[Owner: TBC]` rather than assigning it to someone randomly.
- Is the tone formal and professional? Would you be comfortable forwarding this to a client?

If the output looks like a real document you would be proud to send — congratulations. Your skill works. If something looks off, do not worry. That is exactly what Step 5 is for.

---

### Minute 28–30: Step 5 — Your First Iteration

Look at what WorkBuddy produced. Read it carefully. Not as someone who built it — as someone who is about to send it to their manager. Ask yourself three honest questions:

1. Is there anything in here that should be there but is not?
2. Is there anything in here that should not be there?
3. Would I be comfortable sending this to my manager right now, with zero edits?

Most first-time builders answer question three with "almost — but there is one small thing." That "one small thing" is your first improvement. And improving your skill is just as important as building it.

#### Common First Improvements

After testing the meeting-notes-summarizer for the first time, here are the three improvements that most people want to make:

**Improvement 1 — Add a Priority Level to action items**
The action items table shows who is doing what and when. But it does not tell you which items are critical path versus nice-to-have. Adding a Priority column (High / Medium / Low) helps teams focus their attention correctly.

**Improvement 2 — Add a company or project name to the header**
When you are looking through ten meeting summaries from a busy month, all the headers look the same. Adding the company name or project code to the header makes scanning much faster.

**Improvement 3 — Add a Risks and Blockers section**
The sample notes included an open issue about QA testing. Professional project management separates open issues from action items — they belong in a dedicated section so nothing slips through.

#### How to Iterate — Your First Version Update

Paste this exact prompt into WorkBuddy to make your first improvement and record it properly in the version history:

---

**📋 COPY THIS ITERATION PROMPT:**

```
Please make the following improvement to the meeting-notes-summarizer 
skill and update the SKILL.md file. Record this as version v1.1.

Issue: The Action Items table needs a Priority Level column to help 
teams identify which tasks are critical path versus secondary.

Fix required:
1. Add a "Priority" column to the Action Items table in the Output 
   Specification section (values: High / Medium / Low)
2. Update Step 3 of the Execution Flow: when identifying action items, 
   also assess and assign a priority based on context
3. Update the output-template.md to reflect the new column
4. Add this to the Version History: 
   v1.1 — Added Priority column to Action Items table

Please confirm all changes and show me the updated Action Items table format.
```

**📋 COPY TO HERE**

---

After WorkBuddy completes this update, your SKILL.md will show version v1.1 in the header and v1.1 in the Version History section. You have just written your first changelog entry. This is what professional software development looks like. This is what Skill Engineering looks like.

You are doing it.

---

### Congratulations — You Built Your First Skill!

Stop. Take a breath. Look at what just happened.

Thirty minutes ago, you had a blank folder on your desktop and zero experience building AI Skills. Right now, you have:

- A fully structured **SKILL.md** with all 10 professional sections
- A reusable **output-template.md** that defines exactly what the output should look like
- A **tested, working skill** that you have already verified produces professional output
- Your first **version history entry** (v1.0 and v1.1)
- Your first **iteration completed** — you identified an improvement and implemented it

Let that sink in. You did not just read about AI Skill Engineering. You practiced it. You went through all five steps of the method with a real scenario and produced a real deliverable.

#### What This Skill Will Do For You Starting Tomorrow

The meeting-notes-summarizer is not a toy. The next time you walk out of a meeting with a page of messy notes, pull up WorkBuddy, paste your notes, send one command, and have a professional summary in your hands before you walk back to your desk. What used to take 45 minutes now takes 90 seconds.

But the value goes beyond your own time. This skill is shareable. Every colleague who attends meetings can benefit from what you built today. Send them the `meeting-notes-summarizer/` folder. They install it in their own WorkBuddy. Suddenly, your team produces consistently professional meeting summaries — and nobody had to become a developer to make it happen.

You built something. One person. Thirty minutes. Zero technical background. And now a whole team can use it.

This is the compounding power of Skill Engineering.

#### Your Action Items for This Week

Before you close this chapter, commit to three small actions:

1. **Use the skill after your next real meeting.** Not as a test — as your actual workflow. Paste your real notes in, see what comes out, and experience the time savings firsthand.

2. **Share it with one colleague.** Show them how to invoke it. Watch their reaction when they see messy notes turn into a professional document in 90 seconds. That reaction is your reward.

3. **Notice one thing you want to improve, and make it v1.2.** Maybe the tone needs adjusting for your industry. Maybe you want to add a Confidentiality label. Maybe you want the next meeting date bolded and at the very top. Whatever it is, improve it. Version control is your friend.

#### What Comes Next

In **Chapter 4**, we go deeper into testing. You have now experienced basic functional testing — "does it work?" But professional Skill Engineering requires a higher standard: edge case testing, multi-user validation, and systematic quality benchmarking. Chapter 4 will teach you how to stress-test a skill the way a professional QA engineer would, so you can be genuinely confident in the output quality before you share a skill with your organization.

But for now? Close the laptop. Get yourself a coffee. You earned it.

---

### Chapter 3 Summary

| What We Did | Why It Matters |
|---|---|
| Completed Scene Recognition for a real scenario | Built the habit of analyzing before building |
| Designed input parameters and execution flow on paper | Created the blueprint before construction |
| Used WorkBuddy to generate a complete SKILL.md | Turned design into a working skill file |
| Tested with realistic messy notes | Verified the skill works before relying on it |
| Made our first iteration and updated the version | Established the improvement habit from day one |

---

> **You are no longer just an AI user.**
>
> **You are an AI Skill Engineer.**
>
> **You just proved it.**

---

*End of Chapter 3*

*Next: Chapter 4 — Testing Like a Professional: Edge Cases, Quality Benchmarks, and Multi-User Validation*
