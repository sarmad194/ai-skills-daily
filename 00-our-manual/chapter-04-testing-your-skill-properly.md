# AI Skills Engineering — A Practical Guide for Everyone
## Chapter 4: Testing Your Skill Properly

---

## Introduction

In Chapter 3, you built your first skill from scratch. You followed the Five-Step Method, wrote the SKILL.md file, defined input parameters, created an output template, and ran a quick test to see if something came out the other end. That was a major accomplishment — most people never get that far. You should feel good about it.

But here is the honest question you need to sit with: **Do you actually know it works?**

Not just once, by accident, on a good day, with perfect inputs and a generous interpretation of the output. But reliably, consistently, for anyone, in any reasonable situation?

Building a skill is only half the job. The other half — the half that separates a rough draft from a professional-grade tool — is testing.

Think about how a car manufacturer works. Their engineers spend months designing an engine, a chassis, a braking system. But they do not drive the car off the assembly line and hand it to a customer. First, they test every single component individually. Then they test the whole car together. They test it in the rain. They test it in snow. They test it in desert heat and freezing cold. They test it at high speed, at low speed, when it is loaded with passengers, and when it is empty. They crash-test it deliberately. They test until they are certain — not hopeful, certain — that this car will protect the person sitting inside it.

Your skill needs the same treatment. Not because you are paranoid, but because professionalism demands proof.

Testing gives you **confidence to share** your skill. When a colleague asks "Does this actually work?", you will not say "I think so" — you will say "Yes, and here is the evidence." Testing gives **others confidence to use** your skill. A skill with documented test results feels like a finished product. A skill without them feels like an experiment. Testing also **creates the evidence chain** that proves quality — the trail of results, pass criteria, and failure notes that transforms your personal tool into a professional portfolio asset.

This chapter teaches you exactly how to test your skill, level by level, until you can stand behind it completely.

---

## Why Testing Matters — The 3 Big Reasons

There are three reasons testing is non-negotiable. Each one builds on the last, and together they explain why the best skill engineers in any profession treat testing as sacred — not optional, not hurried, not skipped when time is short.

---

### Reason 1 — Confidence

Without testing, you are guessing your skill works. You ran it once and the output looked reasonable, so you assume it will always be reasonable. This is the same reasoning a cook uses when they taste the soup at the beginning of preparation and assume it will be good after two more hours of boiling. The original taste tells you nothing about the final result.

With testing, you **know** your skill works. Not because you believe in it — but because you have documented evidence that it performs consistently across multiple inputs, multiple contexts, and multiple users.

Why does confidence matter so much? Because confident skills get **shared**. When you know your skill works, you send it to your team without hesitation. You mention it in a meeting. You add it to your portfolio. You tell your manager what it does.

Sharing leads to **team adoption**. When three people on your team are using the same skill, the time savings multiply by three. When ten people use it, the value multiplies by ten. The skill you spent four hours building and testing can save your entire department hundreds of hours over the course of a year. But none of that happens if you never share it — and you never share it if you are not confident — and you are not confident if you have not tested it.

Testing is the trigger that starts the chain reaction of value creation.

---

### Reason 2 — Evidence Chain

In professional environments, proof matters. Intention does not pay salaries. Belief does not justify investment. Evidence does.

When you tell your manager "I built a skill that saves 45 minutes per task," the next question — always — is: "Can you prove it?" This is not a challenge to your integrity. It is a completely reasonable professional expectation. Managers approve budgets, allocate resources, and recommend promotions based on evidence. Give them evidence.

Your test outputs are your proof. A saved Level 1 test result showing "Expected output: present. Actual output: present. Pass criteria: met" is not glamorous, but it is concrete. A folder of test evidence files showing that your skill has been tested against seven different inputs, three different users, and two edge cases is the kind of documentation that gets attention.

Saved test results become your **portfolio**. Every skill you build, test, and document becomes a permanent record of your engineering capability. This is especially powerful for people who do not have traditional technical backgrounds. A healthcare administrator who built, tested, and documented a patient intake summarizer skill has demonstrated something real — not a theoretical capability, but a proven, working tool.

Your portfolio becomes your **career asset**. It is visible, shareable, and objective. Long after the specific project is finished, the portfolio remains. It shows what you can do, not what you say you can do.

---

### Reason 3 — Improvement Discovery

Here is the counterintuitive truth about testing: **failure is the goal**.

Not failure as a final state — but failure as an early warning system. Testing is designed to find problems before they reach real users in real situations. Every problem your test catches is a problem that never becomes an embarrassing moment in a client presentation, a confusing response to a colleague, or a skill that quietly breaks and nobody knows why.

Testing reveals problems you never imagined. You designed your meeting notes summarizer for clean, well-organized meeting transcripts. What happens when someone runs it against a set of notes that were typed on a phone while driving, full of abbreviations, missing punctuation, and with zero structure? Does it still work? Testing will tell you — and the answer might surprise you.

Problems found during testing become **improvements**. Each failure gives you a specific, concrete item to fix. This is the raw material for iteration.

Improvements become **version iterations**. Each iteration makes the skill more robust, more flexible, more reliable. Version 1.0 passes the basics. Version 1.3 handles edge cases. Version 2.0 works beautifully across industries.

Version iterations make your skill genuinely excellent. The best skills in any portfolio have been tested hundreds of times, by many users, against many inputs, with every failure carefully documented and fixed. Excellence is not an accident. It is the result of systematic, disciplined testing.

---

## The 4 Levels of Testing

Testing does not happen all at once. Just like you cannot understand advanced calculus before learning addition, you cannot jump straight to complex edge case testing before confirming the basics work.

Testing happens in **4 levels**, each one building on the foundation of the previous. Each level tests something fundamentally different: basic function, quality rule behavior, boundary conditions, and real-world reusability. Think of it like levels in a video game. You cannot unlock Level 2 until you have cleared Level 1. Trying to skip levels leads to confusion — you will not know whether a problem comes from a basic functionality failure or an edge case issue, because you never confirmed the basics were working.

Complete Level 1 before moving to Level 2. Complete Level 2 before moving to Level 3. By the time you reach Level 4, you will have a skill that is ready for real professional use.

---

## Level 1 — Functionality Test
## (Does it actually work?)

### What It Tests

Level 1 answers the most fundamental question: **Does the skill produce the expected output when given normal, standard inputs?**

Not exceptional inputs. Not broken inputs. Not trick inputs. Normal, realistic, typical inputs — the kind a real user would provide on a regular Tuesday morning when everything is working fine.

This is your baseline. If Level 1 fails, nothing else matters. You do not move to Level 2 until Level 1 passes completely.

---

### How to Run the Level 1 Test

**Step 1: Prepare Standard Test Inputs**

For the meeting notes summarizer from Chapter 3, your test input should look like a real meeting transcript — not perfect, but realistic. It should include the information a typical user would provide: attendee names, some discussion points, some action items that are reasonably clear, and a meeting date and topic.

Use inputs that are:
- **Realistic** — representative of what real users will provide
- **Complete enough** — includes all required information in a typical form
- **Not designed to trick** — save edge cases for Level 3

Sample Level 1 Input for Meeting Notes Summarizer:
```
Date: May 20, 2026
Attendees: Sarah Chen (PM), David Okafor (Engineering Lead), 
           Priya Nair (Design), Marcus Webb (Sales)
Topic: Q2 Product Launch Review

Sarah opened by noting that the beta launch missed the April 15 
deadline by 10 days. David explained the authentication module 
needed an unexpected security patch, which caused the delay. 
The team agreed this was acceptable given the circumstances.

Priya presented revised UI mockups for onboarding. The team 
approved them with minor changes to the color scheme. Priya 
will finalize by May 28.

Marcus reported that 12 pilot customers are ready and waiting. 
He needs the technical documentation by June 1 so sales can 
begin demos. David confirmed his team will deliver it.

Sarah assigned herself to write the launch announcement for 
the website. Target date: June 3.

Next meeting scheduled for June 5.
```

**Step 2: Invoke the Skill Exactly as a User Would**

Run the skill with these inputs as a first-time user would. Do not correct the AI if something looks off mid-run. Let it complete and evaluate the full output afterward.

**Step 3: Check the Output Against the Pass Criteria**

---

### Pass Criteria for Meeting Notes Summarizer

Go through this checklist systematically after running the test. Do not evaluate from memory — compare the actual output against each criterion line by line.

| Criterion | Expected | Actual | Pass? |
|---|---|---|---|
| Executive Summary present | Yes | ? | ? |
| Key Discussion Points section present | Yes | ? | ? |
| Action Items table present | Yes | ? | ? |
| Every action item has an owner name | Yes | ? | ? |
| Every action item has a specific deadline | Yes | ? | ? |
| Output uses professional language | Yes | ? | ? |
| Output length is ≥ 300 words | Yes | ? | ? |
| Next meeting date is captured | Yes | ? | ? |

A Level 1 pass requires **all criteria met**. If any criterion fails, note it, record it, and add it to your iteration list. Do not move to Level 2 with unresolved Level 1 failures.

---

### Level 1 Examples Across Professions

**Teacher — Lesson Plan Generator:**
Run the skill with a standard topic (e.g., "Introduction to Fractions, Grade 4, 45-minute class").
Check: Does it produce a complete plan with learning objectives, activities, and assessment?

**Nurse — Patient Handoff Summarizer:**
Run with typical handoff notes from a morning shift.
Check: Does it produce a structured summary with vitals, medications, flags, and next actions?

**Financial Analyst — Report Summarizer:**
Run with a one-page earnings summary.
Check: Does it produce a brief, accurate summary with key metrics highlighted?

**Lawyer — Contract Clause Extractor:**
Run with a standard NDA document.
Check: Does it correctly identify and extract the key clauses without missing critical terms?

---

### What to Do If Level 1 Fails

Do not panic. A Level 1 failure is normal — especially on a first version. Here is the process:

1. **Note exactly which criterion failed** — Be specific. "Action Items table present: No" is useful. "The output was bad" is not.
2. **Note what the output showed instead** — Did it produce something or nothing? Did it produce a list instead of a table?
3. **Record the failure in your test evidence file** — This becomes your iteration item.
4. **Refer to Chapter 5** — Chapter 5 covers exactly how to diagnose and fix these failures systematically.

---

## Level 2 — Quality Validation Test
## (Do the quality rules actually work?)

### What It Tests

Your SKILL.md contains quality rules — instructions that tell the AI to catch certain problems, flag them, and handle them appropriately. Level 2 tests whether those rules actually activate when they should.

The question is not "Does the skill work with good inputs?" You already confirmed that in Level 1. The Level 2 question is: **When something goes wrong, does the skill catch the problem and handle it gracefully?**

This is the difference between a fragile skill and a robust one. A fragile skill only works when everything is perfect. A robust skill works even when users provide messy, incomplete, or unclear inputs — which, in real life, happens constantly.

---

### How to Run Level 2 Tests

You deliberately provide **incomplete or problematic inputs**. You are not trying to break the skill maliciously — you are simulating the realistic mistakes and gaps that real users will accidentally create.

---

### Test Case 1 — Missing Action Item Owners

**What you do:**
Provide meeting notes that mention tasks being assigned, but do not specify who owns each task.

**Sample Input:**
```
The team agreed that the documentation needs to be updated.
Someone will handle the database migration.
The client presentation will be prepared before Friday.
```

**What to observe:**
Does the skill leave the "Owner" column blank? Does it say "Owner: Unknown"? Does it flag this problem and ask for clarification? Does it write "Owner: TBD" with a note?

**Expected behavior:** The skill should NOT silently leave cells blank. It should either flag the missing owner clearly or write "TBD" with a visible note that the owner needs to be confirmed.

**Pass criteria:**
- Does NOT leave blank cells in the owner column: Yes/No
- Flags the ambiguity clearly: Yes/No

---

### Test Case 2 — Missing or Vague Deadlines

**What you do:**
Provide meeting notes where deadlines are expressed vaguely: "soon," "next week," "as soon as possible," "before the end of the quarter."

**Sample Input:**
```
Sarah will update the website copy soon.
David will fix the login bug when he gets a chance.
The team will review the budget sometime next quarter.
```

**What to observe:**
Does the skill write "soon" in the deadline column? Does it flag that these need specific dates? Does it estimate based on context?

**Expected behavior:** The skill should flag vague deadlines clearly — not accept them silently. A deadline of "soon" in an action item table is useless. The skill should note that specific dates are required.

---

### Test Case 3 — Very Short Meeting Notes

**What you do:**
Provide only 2–3 sentences of meeting notes — barely enough to work with.

**Sample Input:**
```
We discussed the project. Things are going okay. 
We will meet again next week.
```

**What to observe:**
Does the skill crash or produce empty output? Does it produce something thin but valid? Does it note that the input lacks sufficient detail for a complete summary?

**Expected behavior:** The skill should produce the best possible output given the thin input, and note explicitly that more detailed meeting notes would produce a more useful summary. It should NEVER produce empty output.

---

### Real World Examples Across Professions

**Sales — Client Proposal Generator:**
Test with inputs where the client's name, industry, or budget range is missing. Does the skill ask for it? Does it note "Client Name: Not Provided"? Or does it silently generate a proposal addressed to nobody?

**Teacher — Lesson Plan Generator:**
Test without specifying the grade level. Does the skill default to a general audience? Does it ask for clarification? A lesson plan for Grade 2 and one for Grade 12 should look very different — the skill must handle this gap.

**Doctor — Clinical Note Summarizer:**
Test without patient age or relevant medical history. Clinical summaries without patient age are nearly useless for clinical decisions. Does the skill flag this critical missing information immediately?

**Finance — Earnings Report Summarizer:**
Test without specifying the reporting period or date range. A financial summary without a clear time period is potentially misleading. Does the skill catch this and request clarification?

---

### Level 2 Pass Criteria

| Test Case | Input Problem | Expected Behavior | Actual Behavior | Pass? |
|---|---|---|---|---|
| Missing owners | No owner names in notes | Flag as TBD, do not leave blank | ? | ? |
| Vague deadlines | "soon", "next week" | Flag, request specific dates | ? | ? |
| Very short notes | 2–3 sentence input | Produce thin but valid output | ? | ? |
| Skill handles errors gracefully | Any malformed input | No empty output, no crash | ? | ? |

A Level 2 pass requires all four tests to produce appropriate, graceful handling of the problem inputs.

---

## Level 3 — Boundary Case Testing
## (What happens in extreme situations?)

### What It Tests

Level 3 asks the hardest question yet: **Can your skill handle unusual, extreme, or unexpected inputs without breaking?**

Real users are creative in ways you cannot predict. They paste entire documents. They provide two-word inputs. They switch industries without telling the skill. They include emoji, foreign phrases, and dense technical jargon. Level 3 systematically stress-tests your skill against these extreme conditions before real users discover them in production.

---

### Boundary Case 1 — Very Long Input

**The scenario:**
A user copies and pastes five hours of meeting transcripts into your skill — over 5,000 words of raw discussion.

**What to test:**
Run your meeting notes summarizer against a genuinely long block of text. You can find or create a 2,000–5,000 word document for this purpose. Paste it as the "meeting notes" input.

**What to observe:**
- Does the skill complete successfully, or does it time out?
- Does it attempt to summarize all 5,000 words equally, or does it intelligently prioritize key decisions and action items?
- Is the output still usable and structured, or does it become a wall of text?

**Why this matters:**
Some users, especially meticulous ones, provide exhaustive inputs. Your skill should handle abundance gracefully — producing a focused summary, not an equally exhaustive output.

---

### Boundary Case 2 — Very Short Input

**The scenario:**
A user provides only two sentences: "We met. We will meet again Tuesday."

**What to test:**
Run the skill with the absolute minimum viable input.

**What to observe:**
- Does it crash? Does it produce empty output?
- Does it produce something embarrassingly thin that reads like a joke?
- Does it note that insufficient information was provided while still producing the best possible output?

**Why this matters:**
Short inputs reveal whether your quality rules protect against poor output. A skill that produces "Executive Summary: A meeting occurred. Next Steps: None identified." is technically running, but professionally useless.

---

### Boundary Case 3 — Unusual Industry or Context

**The scenario:**
A doctor uses your meeting notes summarizer for a medical conference, not a business meeting. The input contains medical terminology, drug names, and clinical discussion.

**Sample Input:**
```
Attendees: Dr. Martinez (Cardiology), Dr. Patel (Neurology), 
           Dr. Kim (Internal Medicine)
Topic: Patient Care Protocol Review

Discussed the new anticoagulation protocol for atrial fibrillation.
Dr. Martinez noted that the current warfarin dosing guidelines 
need updating based on the recent ARISTOTLE trial data.
Dr. Patel will revise the protocol document by June 15.
```

**What to observe:**
- Does the skill produce a professional, appropriate output for a medical context?
- Does it preserve medical terminology accurately?
- Does it structure the action items correctly even in an unfamiliar context?

**Why this matters:**
A truly reusable skill transcends the context it was designed for. A meeting notes summarizer should work for any meeting — not just the one you had in mind when you built it.

---

### Boundary Case 4 — Special Characters, Numbers, and Mixed Languages

**The scenario:**
The meeting notes include percentages, currency amounts, dates in different formats, and occasional words from another language.

**Sample Input:**
```
Revenue is up 23.5% vs. Q1. The €2.4M contract was discussed.
Launch date: 2026/06/01 (or possibly June 1st, 2026).
Marcus mentioned the partner in München confirmed the deal.
```

**What to observe:**
- Are numbers and percentages preserved accurately?
- Are dates handled consistently (does the skill standardize them)?
- Are foreign words or place names handled without garbling?

---

### Boundary Case 5 — Missing Optional Parameters

**The scenario:**
Your skill has an optional "Summary Style" parameter (Concise / Standard / Detailed). The user does not provide it.

**What to observe:**
- Does the skill crash asking for the missing parameter?
- Does it silently use a default style?
- Does it note which default it used?

**Expected behavior:** Optional parameters must have working defaults. The skill should use the default, mention it in the output ("Using Standard summary style as no preference was specified"), and proceed normally.

---

### How to Document Boundary Tests

Create a simple test log in your test evidence file:

| Test Case | Input Scenario | Expected Result | Actual Result | Pass/Fail | Notes |
|---|---|---|---|---|---|
| Very Long Input | 3,000-word transcript | Produces focused summary | ? | ? | ? |
| Very Short Input | 2 sentences | Thin but valid output | ? | ? | ? |
| Medical Context | Medical conference notes | Professional medical summary | ? | ? | ? |
| Special Characters | Percentages, EUR symbol | Accurate preservation | ? | ? | ? |
| Missing Optional Param | No Summary Style given | Uses default, notes it | ? | ? | ? |

---

### What Boundary Tests Reveal

Level 3 tests reveal the hidden weaknesses in your skill — the assumptions you baked in without realizing it. Your skill might assume inputs are always in English. It might assume inputs are always between 200 and 1,000 words. It might assume the context is always a business meeting. These assumptions are invisible until Level 3 testing makes them visible.

Every failure at this level is a gift. Each failure tells you exactly what to fix. A skill that emerges from thorough Level 3 testing has had its hidden assumptions exposed and resolved. That skill is genuinely more durable than one that was never tested at all.

Document every failure carefully. Each one becomes an iteration item in Chapter 5.

---

## Level 4 — Reusability Test
## (Does it work for others in different situations?)

### What It Tests

Level 4 is the ultimate test. It answers the most important question of all: **Can someone else use your skill in a completely different situation and still get consistently good results?**

This is the level where you discover whether you built a skill or a personal shortcut.

---

### Why Reusability Is the Entire Point

A skill, by definition, is reusable. That is what makes it a skill and not just a prompt. A chef's knife technique works whether the chef is cutting a carrot or a piece of chicken. A teacher's explanation style works whether the class is learning fractions or metaphors. A journalist's interview technique works whether the subject is a scientist or a politician.

If your meeting notes summarizer only works reliably when:
- The meeting is a sales team meeting
- The notes are typed in a specific format
- You are the one running it
- The input is between 300 and 800 words

...then you have built a very specific prompt, not a reusable skill. Level 4 will reveal this clearly, and that is valuable information — because it points directly at what needs to be fixed.

---

### Test 1 — Different Industry

Take the meeting notes summarizer and run it with inputs from a completely different industry. Do not choose the same type of meeting you used in Levels 1–3.

**Suggested test inputs by profession:**
- **Healthcare administrator:** Medical department planning meeting notes
- **University lecturer:** Faculty curriculum review meeting notes
- **Startup founder:** Investor pitch debrief meeting notes
- **NGO coordinator:** Community outreach planning meeting notes

**What to observe:**
Does the output quality remain high? Are the action items still structured correctly? Does the professional tone remain appropriate? Does anything look jarring or out of place in the new context?

---

### Test 2 — Different User

This is the most revealing test. Ask a **colleague** to use your skill — without you walking them through it. Give them only:
- The skill file (SKILL.md)
- A set of meeting notes

Then watch silently. Do not help. Do not clarify. Let them discover whatever they discover.

Note every moment of confusion. Every pause. Every question. Every place where they tried something and it did not work the way they expected.

Every confusion point is a documentation improvement item. Every question they ask is a sign that your instructions were unclear to someone who was not you. This is invaluable data that no amount of self-testing can produce.

**Real-world equivalent:**
A UX designer calls this a "usability test." They build something and then watch a real user interact with it without any guidance. The user's frustration, confusion, and delight are the most honest feedback the designer will ever receive. You are doing the same thing for your skill.

---

### Test 3 — Different AI Tool

If you built your skill in WorkBuddy, try running it in a different AI tool — Cursor, Copilot, Claude, or any other assistant you have access to.

Does the output quality hold? Does the structure remain consistent? Are the same quality rules being applied?

A true skill is **tool-agnostic**. The SKILL.md file is plain Markdown with clear instructions. Any competent AI system should be able to follow those instructions and produce consistent, professional output. If the output degrades significantly in a different tool, that tells you the skill relies too heavily on tool-specific behavior rather than clear universal instructions.

---

### Test 4 — Different Language (Optional but Valuable)

If your team works internationally, try running the skill with inputs in a different language. Can the skill produce output in the same language as the input? Does it maintain the structural quality when working in Mandarin, Spanish, French, or German?

This matters more than people realize. Teams in multinational organizations use AI tools across language barriers constantly. A skill that works beautifully in English but degrades in French is limiting your potential audience significantly.

---

### Reusability Checklist and Scoring

After completing all four Level 4 tests, evaluate against this checklist:

| Criterion | Evidence | Pass? |
|---|---|---|
| Works with at least 2 different industries | Test 1 results | Yes/No |
| A colleague used it successfully without help | Test 2 observation | Yes/No |
| Consistent quality across AI tools | Test 3 results | Yes/No |
| Parameters are self-explanatory to new users | Test 2 observation | Yes/No |
| Output quality is consistent regardless of who runs it | Tests 1–4 combined | Yes/No |

**The Reusability Score:**
Count how many "Yes" answers you have.

- **5 Yes:** Excellent — this skill is ready to share widely with full confidence
- **3–4 Yes:** Good — needs minor improvements before broad sharing
- **2 Yes:** Developing — needs significant improvements, primarily in clarity and flexibility
- **0–1 Yes:** Needs fundamental revision — consider revisiting the skill design in Chapter 2

Do not be discouraged by a low score on your first attempt. This is exactly what Level 4 testing is for. The score gives you a specific, actionable picture of what to improve. A skill that scores 2 on its first Level 4 test and 5 after three iterations is a success story — not a failure.

---

## Building Your Test Evidence File

### What Is a Test Evidence File?

A test evidence file is a simple document that records all your testing activity, inputs, outputs, pass/fail results, and issues found. It transforms your testing from an invisible private activity into a visible professional artifact.

It is the difference between a mechanic who checks a car and says "It seemed fine" and a mechanic who hands you a printed inspection report listing every system checked, every measurement taken, and every issue found and resolved.

The inspection report has authority. The verbal assurance does not. Your test evidence file gives your skill authority.

---

### How to Create It

Create a file called `test-evidence.md` and save it in the same folder as your SKILL.md file. This keeps all skill-related materials together and makes your portfolio clean and organized.

---

### What to Include

**Section 1: Skill Information**
```markdown
## Skill: Meeting Notes Summarizer
- Version tested: 1.0
- Date of testing: 2026-05-25
- Tester: [Your name]
- Tools used: WorkBuddy Auto Mode
```

**Section 2: Level 1 — Functionality Test Results**
```markdown
## Level 1: Functionality Test
Input used: [Brief description of test input]
Test date: 2026-05-25

| Criterion | Expected | Actual | Pass? |
|---|---|---|---|
| Executive Summary present | Yes | Yes | ✅ |
| Key Discussion Points section present | Yes | Yes | ✅ |
| Action Items table present | Yes | Yes | ✅ |
| Every action item has an owner | Yes | Partial | ❌ |
| Every action item has a deadline | Yes | Yes | ✅ |
| Professional language quality | Yes | Yes | ✅ |

Issues found: One action item (website copy update) had 
"Owner: Unknown" rather than the assigned name from the notes.
```

**Section 3: Level 2 — Quality Validation Results**
Record which quality rules were tested, whether the skill flagged problems correctly, and whether any quality rule failed to activate.

**Section 4: Level 3 — Boundary Case Results**
Record each boundary case, the specific input used, and the output result. Note any cases where the skill failed or degraded.

**Section 5: Level 4 — Reusability Results**
Record the industries tested, any colleagues who participated in testing, the tools used, and the final Reusability Score.

**Section 6: Issues Found and Fixed**
```markdown
## Issues Found and Fixed

Issue 1: Action item owner not extracted from long sentences
- Found in: Level 1 Test
- Root cause: Output template did not explicitly instruct 
  the AI to scan all sentences for owner assignments
- Fix applied: Added explicit instruction to scan full 
  notes paragraph by paragraph for owner names
- Fixed in version: 1.1
- Retest result: ✅ Passed

Issue 2: "Soon" accepted as a valid deadline
- Found in: Level 2 Test Case 2
- Fix applied: Added quality rule: "Any deadline expressed 
  as a relative term (soon, next week, shortly) must be 
  flagged with ⚠️ and noted as requiring a specific date"
- Fixed in version: 1.1
- Retest result: ✅ Passed
```

---

### Why This File Matters

When you share your skill with a colleague, they can open the test evidence file and see — immediately, without asking you — that this skill has been properly validated. When your manager asks about the quality of the tools your team is using, you have documented proof. When you improve the skill next quarter, you have a baseline to compare your new version against.

The test evidence file is also your own memory. Six months from now, when you revisit this skill, you will not remember which issues you fixed or why. The test evidence file tells you everything you need to know. It is the full historical record of your skill's journey from draft to professional tool.

---

## Your Testing Checklist

Use this checklist every time you test a new skill or a new version of an existing skill. Print it, save it, or copy it into your test evidence file.

---

**BEFORE TESTING:**
- [ ] SKILL.md is complete with all required sections (Purpose, Inputs, Outputs, Quality Rules, etc.)
- [ ] Output template is saved in the references/ folder
- [ ] At least 3 realistic test inputs are prepared
- [ ] test-evidence.md file is created and ready

---

**LEVEL 1 — FUNCTIONALITY:**
- [ ] Ran skill with standard, realistic inputs
- [ ] All required output sections are present in the output
- [ ] Word counts meet the minimum requirements specified
- [ ] Output format matches the template specification
- [ ] Content is relevant and appropriate to the inputs provided
- [ ] Level 1 pass criteria are all met before moving on

---

**LEVEL 2 — QUALITY VALIDATION:**
- [ ] Tested with inputs missing at least one required field
- [ ] Tested with inputs containing vague or ambiguous values
- [ ] Confirmed quality rules caught and flagged actual problems
- [ ] Confirmed skill did not produce empty or blank output
- [ ] Skill handled all error conditions gracefully

---

**LEVEL 3 — BOUNDARY CASES:**
- [ ] Tested with very long input (1,500+ words)
- [ ] Tested with very short input (2–3 sentences)
- [ ] Tested with input from an unusual or different industry context
- [ ] Tested with special characters, numbers, or foreign words
- [ ] Tested with missing optional parameters
- [ ] All boundary test results documented in test log table

---

**LEVEL 4 — REUSABILITY:**
- [ ] Tested with inputs from at least 2 different industries
- [ ] Asked at least one colleague to use the skill without guidance
- [ ] Noted all confusion points from colleague observation
- [ ] Verified consistent output quality across different users
- [ ] Confirmed parameters are self-explanatory to new users
- [ ] Calculated and recorded the Reusability Score

---

**AFTER TESTING:**
- [ ] All test results recorded in test-evidence.md
- [ ] All issues found listed with clear descriptions
- [ ] Fixes applied and retested where issues were found
- [ ] Version history updated in SKILL.md if any fixes were made
- [ ] Skill is ready to share with the team

---

## Chapter Summary

You have now learned the complete professional framework for testing an AI skill. Let us recap everything clearly.

Testing is not a bonus step you do if you have extra time. It is the essential second half of the skill engineering process. Building without testing is like writing a contract and never reading it before signing. Something might be wrong. Something might be missing. You will not know until it is too late.

The **4 Levels of Testing** are designed to catch four different categories of problems:

**Level 1 — Functionality** confirms that the skill works in normal, everyday conditions. It establishes the baseline. If Level 1 fails, nothing else matters. Fix it before continuing.

**Level 2 — Quality Validation** confirms that your quality rules actually activate when they should. A quality rule that never fires is not a quality rule — it is decorative text. Level 2 proves that your skill is robust, not just responsive.

**Level 3 — Boundary Cases** reveals the hidden assumptions built into your skill. You assumed inputs would be a certain length. You assumed a certain context. You assumed users would provide complete information. Level 3 exposes every assumption and gives you the chance to either validate it or eliminate it.

**Level 4 — Reusability** confirms that you built a skill and not a personal shortcut. True reusability — working for multiple people, across multiple industries, in multiple tools — is the gold standard of skill engineering. The Reusability Score gives you a clear, actionable metric.

The **test evidence file** transforms your testing from invisible labor into a professional portfolio asset. It proves your quality. It serves as your memory. It gives confidence to everyone who uses your skill.

And finally: **every failed test is a gift**. Failures found in testing are free. Failures found in production, in front of clients or colleagues, are expensive. Welcome every failure you discover during testing. Document it. Fix it. Retest it. Each one makes your skill stronger.

---

## What Is Coming in Chapter 5

You now know how to build a skill (Chapter 3) and how to test it properly (Chapter 4). But what happens after testing reveals problems? How do you fix them systematically without accidentally breaking something that was already working?

Chapter 5 is about **iteration** — the disciplined process of improving your skill over time.

In Chapter 5, we introduce the **Golden Rule of Iteration**: never change two things at once. When you fix multiple problems simultaneously, you lose the ability to know which fix resolved which problem. The Golden Rule keeps your iteration process clean, trackable, and reliable.

We also explore why **version numbers matter** more than people realize. The difference between version 1.0 and version 1.3 is not just a number — it is a record of everything that was learned, tested, and improved. We show you how to maintain a version history that tells the complete story of your skill's evolution.

We cover the **Iteration Loop** — the repeating cycle of test, discover, fix, retest — and how to use it to build a skill that continuously improves. Every iteration cycle makes the skill more reliable, more flexible, and more valuable.

By the end of Chapter 5, you will not just have a tested skill. You will have a skill with a documented history of improvement, a clean version log, and the ability to keep making it better every time you or a colleague uses it. That is what separates a tool you built once from a living, evolving professional asset.

See you in Chapter 5.

---

*Chapter 4 Complete — AI Skills Engineering: A Practical Guide for Everyone*
*Next: Chapter 5 — Iterating Your Skill: The Art of Continuous Improvement*
