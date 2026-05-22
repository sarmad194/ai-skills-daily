# AI Skills Engineering — A Practical Guide for Everyone
## Chapter 2: The 5-Step Method Made Simple

---

### Introduction

Welcome back. In Chapter 1, we explored what an AI Skill actually is — a structured recipe card that turns your expertise into a reusable, teachable, shareable system. We learned why using AI without skills is like cooking every meal from scratch with no recipe: the results are inconsistent, the effort is wasted, and nobody learns from the experience.

Now we move to the most important question: **How do you actually build one?**

This chapter introduces the **5-Step Method** — the exact framework used by AI Skill engineers at organizations around the world, from tech companies to hospitals to government agencies. When you first see those five steps laid out, they might feel intimidating. They sound professional and systematic, and you might wonder: "Is this really something I can do?" The answer is yes. Absolutely yes.

Here is the key insight: **the 5-step method is not complex. It is logical.** Each step answers a natural question. Together, the five steps take you from a vague idea to a fully working, tested, and documented AI Skill.

Here is the best analogy we know for how this works:

> **Building a skill is like opening a restaurant.** Before you can serve your first customer, you need five things in place. First, you need to know your **menu** — what dishes do you offer, and who will order them? Second, you need to understand your **customers** — who are they, what do they want, what do they dislike? Third, you need a **recipe** for every dish — step-by-step instructions so any chef can cook it consistently. Fourth, you need a **quality check** before food leaves the kitchen — does it taste right, does it look right, is it the right portion? And fifth, you need an **improvement plan** — after opening week, what feedback did you get, and how do you make next week even better?
>
> The 5-Step Method for AI Skill Engineering follows exactly this logic. Step 1 is your menu. Step 2 is understanding your customers. Step 3 is writing your recipe. Step 4 is your quality check. Step 5 is your improvement plan.

By the end of this chapter, you will not just understand what the five steps are — you will understand *why* each step exists, *what happens if you skip one*, and *exactly what to do* at each stage. Let us begin.

---

### Step 1: Scene Recognition and Analysis
### (Understanding What Problem You Are Solving)

---

#### What It Means

Every AI Skill starts with a problem worth solving. Not a vague wish, not a general idea — a specific, observable, repeatable problem in your real working life. Step 1 is about developing the skill of seeing those problems clearly.

This step might feel like the least glamorous part of the process. There is no coding here, no file creation, no AI interaction. It is purely thinking and observing. But do not underestimate it. Of all five steps, this is the one that determines whether your skill will actually be useful in the real world — or whether it will end up as a file nobody opens.

The core question of Step 1 is simple: **What problem am I trying to solve?**

To answer that question well, you need to observe your own work with fresh eyes. Start by watching yourself for one full week. Pay attention to the tasks that drain your energy not because they are hard, but because they are repetitive. Pay attention to the tasks where you constantly think "I have done this before, I just cannot remember exactly how." Pay attention to the tasks where a junior colleague gets it wrong not because they are not smart, but because they have not yet built up the experience to know what "good" looks like.

Ask yourself three diagnostic questions throughout that week:

**Question 1:** What do I do repeatedly, more than once a week?
**Question 2:** What takes too long despite following a predictable pattern?
**Question 3:** What would I need to explain very carefully to a brand new colleague?

If a task comes up in all three answers, it is almost certainly a good candidate for an AI Skill.

---

#### The 5 Signals — How to Know if Something is Worth Building

Not every task deserves a skill. Here are five clear signals that something is worth investing your time to build properly.

**Signal 1: HIGH FREQUENCY**
You perform this task more than once a week, consistently. Frequency is what makes a skill pay off. If you build a skill for something you only do once a year, the return on your investment is low. But if you do a task fifty times a year, even a 30% time improvement saves you weeks of work annually.

*Example: A sales consultant who writes a client research summary after every prospect meeting — that could be 3 to 5 summaries per week.*

**Signal 2: CLEAR PROCESS**
There is a recognizable sequence of steps involved. The task does not require completely unique creative thinking every single time. You could, if pushed, write down the steps you follow. Maybe you have never written them down before, but they exist in your head.

*Example: A teacher who builds lesson plans always starts with learning objectives, then content outline, then activities, then assessment. The structure is predictable even if the topic changes.*

**Signal 3: EXPERIENCE DEPENDENT**
Experienced people do this task noticeably better than beginners. This is the golden signal. It means there is real expertise embedded in the task — expertise that can be captured, documented, and transferred through a Skill file.

*Example: A senior financial analyst writes quarterly reports that are clearer, more insightful, and better structured than a junior analyst's reports. The difference is not intelligence — it is accumulated know-how.*

**Signal 4: STANDARDIZABLE OUTPUT**
The final result of the task always looks roughly similar in structure, even when the content changes. A report is a report. A proposal is a proposal. A patient summary is a patient summary. When the output has a recognizable shape, you can specify it precisely in your Skill design.

*Example: Patient discharge summaries at a hospital all need the same sections: diagnosis, treatment provided, medications prescribed, follow-up instructions. The patient changes every time. The structure does not.*

**Signal 5: MULTIPLE PEOPLE DO IT**
Your entire team, department, or organization performs this task regularly. When one person builds a Skill that ten people use daily, the impact multiplies tenfold. This is how individual knowledge becomes organizational capability.

*Example: Every account manager at a company writes monthly client status reports. If one person builds a great Skill for this, everyone benefits immediately.*

---

#### The 3 Questions to Answer Before Moving On

Before you leave Step 1, make sure you can clearly answer these three questions in writing:

**Question 1: What is the business objective?**
What problem will this skill ultimately solve for the organization or for you personally? Keep this practical and specific. "Save time on client reports" is a business objective. "Be more efficient with AI" is too vague.

*Example: After every sales visit, generate a complete client research report within 10 minutes rather than 2-3 hours, so the sales team can focus on selling instead of writing.*

**Question 2: What are the key variables?**
What changes between each use of this skill? These are the things a user will provide each time they invoke the skill — the information that makes each output unique.

*Example: The client name changes. The industry changes. The pain points discussed in the meeting change. The products they showed interest in change. These become your input parameters in Step 2.*

**Question 3: What are the constraints?**
What rules must never be broken, no matter what? These constraints protect quality, protect your organization, and prevent the AI from making things up.

*Example: Never invent information that was not actually shared by the client. Never include competitor pricing data without verification. Always maintain a professional, neutral tone.*

---

#### Real-World Examples Across Different Professions

Here is how Step 1 looks when applied to different types of work:

| Profession | Repeating Task | The Real Problem It Solves |
|---|---|---|
| **Sales Consultant** | Writing proposals after client meetings | Proposals take 3 hours and quality varies by consultant |
| **Schoolteacher** | Creating lesson plans for each new topic | Plans take too long and junior teachers struggle with structure |
| **Doctor / Clinician** | Writing patient case summaries | Summaries are inconsistent and time-consuming across staff |
| **Financial Analyst** | Generating monthly financial reports | Report formats differ by analyst, insights are inconsistently communicated |
| **HR Manager** | Writing job descriptions for open positions | Each job description is written from scratch, style varies widely |
| **Legal Assistant** | Summarizing contracts for clients | Summaries miss key clauses when done by less experienced staff |

Notice the pattern: in every case, the task is **frequent**, **process-driven**, **experience-dependent**, and currently producing **inconsistent results** across different people.

---

#### Common Mistake to Avoid

The single most common mistake in Step 1 is **rushing past it**. People get excited about building something, and they jump straight to creating the skill file before they have actually thought through the problem. This is the equivalent of a chef running into the kitchen and starting to cook without deciding what dish they are making.

When you skip Step 1 properly, your skill ends up either too narrow (it only works for one specific situation) or too vague (it works for everything but is excellent at nothing). Both outcomes waste your effort.

Spend at least 30 minutes on Step 1. Write your answers down. Show them to a colleague. Make sure the problem is real, specific, and worth solving before you move on.

---

### Step 2: Core Component Design
### (Designing What Goes In and What Comes Out)

---

#### What It Means

Now that you know exactly what problem you are solving, it is time to design the solution. Step 2 is the engineering stage — where you move from "I understand the problem" to "I know exactly what this skill will do and how it will do it."

Think of this step like designing a form at a government office. When you go to renew your passport or register a business, there is a carefully designed form waiting for you. Someone put a lot of thought into that form: What information do we need to collect? What documents must be attached? What rules must be followed? What does the final output (your passport, your certificate) look like? Step 2 of Skill Engineering is exactly this kind of careful, structured design thinking.

The goal is to define four things with enough precision that a complete stranger could build this skill from your design document alone.

---

#### Design 1 — Input Parameters: What Information Goes In?

Input parameters are the pieces of information that must be provided every time someone uses the skill. Think of them as the fields on your form. Some fields are mandatory (you cannot submit the form without them). Some fields are optional (they help, but the form can be processed without them).

**Required Inputs** — information that must be provided every single time. If this information is missing, the skill cannot produce a meaningful output.

**Optional Inputs** — information that improves the output when provided, but the skill has sensible default values if they are not provided.

*Example: A sales proposal skill might look like this:*

| Input Parameter | Type | Required? | Notes |
|---|---|---|---|
| `client_name` | Text | Required | Full name of the client organization |
| `industry` | Text | Required | Client's industry sector |
| `pain_points` | Text | Required | Problems the client mentioned in the meeting |
| `products_discussed` | Text | Required | Which of your products were discussed |
| `proposal_length` | Number | Optional | Default: 10 pages |
| `language_style` | Choice | Optional | Formal / Friendly — Default: Formal |
| `include_pricing` | Boolean | Optional | Default: No |

Notice how every input is named clearly, typed precisely, and has a defined default where applicable. This level of specificity is what separates a professional Skill design from a rough idea.

---

#### Design 2 — Execution Flow: What Steps Does the Skill Follow?

The execution flow is the step-by-step process the AI will follow to transform your inputs into your output. Think of it as the cooking method in your recipe. You need at minimum 5 to 7 clear steps. Each step should have a clear purpose, and the steps should build on each other logically.

*Example: Execution flow for a client research report skill:*

1. **Receive and validate inputs** — Check that all required inputs are present. If anything is missing, request it before proceeding.
2. **Analyze client context** — Based on the client's industry and stated pain points, identify the business challenges they are likely facing.
3. **Match solutions to needs** — Cross-reference the products discussed against the identified pain points. Identify the strongest alignment points.
4. **Generate proposal structure** — Create a chapter-by-chapter outline based on the standard proposal template (see references/).
5. **Write detailed content** — Develop each section with specific, factual content drawn from the inputs. Never invent information not provided.
6. **Run quality validation** — Check that all quality rules pass (see Quality Validation Rules section). Fix any issues automatically.
7. **Deliver formatted output** — Present the final document in the required format, clearly structured and ready for review.

Each step is actionable, specific, and connected to the next. This is what makes the output consistent regardless of who invokes the skill.

---

#### Design 3 — Output Specification: What Does the Final Result Look Like?

Before you build anything, you must know exactly what success looks like. Your output specification answers that question precisely.

Define these four things:

- **File format:** What format is the output? (Markdown, Word document, structured text, PDF-ready format)
- **Document structure:** What sections or chapters does the output contain? List every heading.
- **Length requirements:** What is the minimum acceptable length? (Example: minimum 1,500 words for a client proposal)
- **Style requirements:** What tone, vocabulary level, or formatting rules apply? (Example: Use numbered headings, write in third person, avoid technical jargon)

**The Important Rule About Templates:**
One of the most common beginner mistakes is pasting the entire output template inside the SKILL.md file. This makes the file enormous, hard to read, and painful to maintain. Instead, follow this professional practice:

- Save the output template as a separate file in the `references/` folder
- In SKILL.md, write: *"Refer to references/report-template.md for the complete output structure"*
- This keeps your SKILL.md lean, clean, and easy to update independently

When the template changes, you update one file. When the skill logic changes, you update another. Clean separation makes maintenance much easier.

---

#### Design 4 — Quality Validation Rules: How Do You Know if It's Good Enough?

This is the section most beginners skip — and it is one of the most valuable. Quality validation rules are specific, checkable conditions that the output must meet before it is delivered. Think of them as the inspection checklist in your restaurant kitchen before the plate goes out.

The rules must be **specific and binary** — each rule either passes or fails. Vague rules like "ensure quality" or "make it professional" are useless. Nobody can check whether those rules passed or failed.

*Example of WRONG quality rules:*
- "Make sure the proposal is well-written"
- "Ensure the document is comprehensive"
- "Confirm the output is professional"

*Example of CORRECT quality rules:*

| Rule | Pass Condition | Fail Condition | Fix if Fails |
|---|---|---|---|
| Section completeness | All 7 required sections are present | Any section is missing | Generate the missing section before delivery |
| Minimum length | Document is at least 1,500 words | Document is shorter than 1,500 words | Expand the shortest section first |
| Client name usage | Client name appears in every section heading | Client name is missing from any heading | Add client name to all section headings |
| No invented information | Every claim in the document traces back to a provided input | Any claim cannot be traced to provided inputs | Remove or flag the unverified claim |

Notice how each rule is observable and actionable. This is the difference between quality assurance and wishful thinking.

---

#### Common Mistake to Avoid

The most common design mistake is **hardcoding** — making inputs too specific to one situation instead of keeping them flexible enough for all situations.

*Example of WRONG design (hardcoded):*
> "Generate a 10-page proposal for ABC Healthcare recommending our patient management system for their three hospital locations."

This skill works for exactly one client, one product, and one scenario. It is useless for everything else.

*Example of CORRECT design (parameterized):*
> "Generate a {proposal_length}-page proposal for {client_name} in the {industry} sector, recommending {products_discussed} to address the following pain points: {pain_points}."

This skill works for any client, any product, any industry, any length. The variables in curly brackets become your input parameters. This single Skill file serves your entire organization forever.

The golden rule: **any specific detail that changes between uses should be a variable, not hardcoded text.**

---

### Step 3: Building Your Skill File (SKILL.md)
### (Writing the Recipe Card)

---

#### What It Means

You have identified your problem. You have designed your solution. Now comes the step most people think of as "the hard part" — actually creating the Skill file. But here is the secret: if you did Step 1 and Step 2 properly, Step 3 is surprisingly straightforward. You are not inventing anything new. You are simply organizing what you already know into a standard format.

The main file is always called **SKILL.md**. The "MD" stands for Markdown — a simple text format that is easy to read, easy to write, and universally supported by AI tools. Think of it as a very detailed, very well-organized recipe card. It does not require any programming knowledge. It does not require special software. You can write it in any text editor, including Notepad if you wanted to.

What makes SKILL.md powerful is not the format itself — it is the **structure**. Every professional skill file follows the same 10-section standard. This means any AI, any tool, and any colleague can pick up your SKILL.md and immediately understand what the skill does, how to use it, and what to expect from it.

---

#### The Physical Structure of a Skill

Every skill lives in its own dedicated folder. Here is what the folder structure looks like:

```
your-skill-name/
├── SKILL.md              ← Required. This is your recipe card.
├── scripts/              ← Optional. For Python scripts or automation tools.
│   └── generate_report.py
├── references/           ← Optional. For templates and reference documents.
│   └── report-template.md
└── assets/               ← Optional. For images, logos, or visual resources.
    └── company-logo.png
```

The only file that is absolutely required is SKILL.md. Everything else is optional and organized into clearly named subfolders. This structure keeps things clean and makes it easy to find anything.

For a beginner's first skill, you will probably only need SKILL.md and a references folder for your output template. The scripts folder is for more advanced skills that involve automation or data processing. You do not need to worry about that now.

---

#### The 10 Sections of SKILL.md

Every professional SKILL.md file contains these 10 sections, in this order. Each section serves a specific purpose, and skipping any of them creates gaps that will cause problems later.

**Section 1: Basic Information**
The metadata of your skill. This includes the skill name, version number, author name, creation date, last update date, and the job roles this skill is designed for. This section takes less than 5 minutes to write and saves enormous confusion later when multiple people are managing multiple skills.

*Example:*
```
Skill Name: Client Research Report Generator
Version: v1.0
Author: Sales Team
Created: 2026-05-22
Last Updated: 2026-05-22
Applicable Roles: Sales Consultant, Account Manager, Business Development
```

**Section 2: Functional Description**
A plain-language explanation of what this skill does and why it is valuable. Write this as if explaining to someone who has never heard of the skill. Two to four sentences is usually enough. Include the specific problem it solves and the measurable value it provides.

*Example: "This skill generates a structured client research report following every sales discovery meeting. It reduces report writing time from 2-3 hours to under 15 minutes while ensuring all key insights are captured consistently and professionally."*

**Section 3: Input Parameters**
The complete table of inputs you designed in Step 2. Every input should be listed with its name, data type, whether it is required or optional, and any default values. This section is what a user consults before invoking the skill. It should be so clear that a first-time user knows exactly what to provide.

**Section 4: Role Settings**
This section tells the AI what character or expertise to embody when executing this skill. The AI will perform better when it has a clear professional identity to inhabit. A skill for writing patient summaries might instruct the AI to act as "an experienced clinical documentation specialist with 15 years of hospital experience." A skill for writing marketing copy might say "act as a senior brand strategist who specializes in B2B technology companies."

This section dramatically improves output quality and is one of the most powerful techniques in Skill Engineering. Give the AI a specific, credible identity and it will behave accordingly.

**Section 5: Execution Flow**
The step-by-step instructions you designed in Step 2. Each step should be numbered and clearly written. Include not just what to do but how to handle exceptions and edge cases. The more detail you put here, the more consistent your outputs will be.

**Section 6: Output Specification**
The exact description of what the final output should look like. Include file format, structural requirements, length minimums, and style rules. Reference your template file here rather than pasting the template content directly.

**Section 7: Quality Validation Rules**
The checkable pass/fail rules you designed in Step 2. Present them as a table or numbered list. Each rule should be specific enough that even a person who has never used this skill before can verify whether it passes or fails.

**Section 8: Usage Examples**
Concrete examples showing how to invoke this skill correctly. Show at least two examples — one for a common use case and one for an edge case. This is your user manual. When someone is confused about how to use the skill, this section is where they will look first.

**Section 9: Constraints and Notes**
The rules, warnings, and important notes that apply to this skill. What should never be done? What common mistakes should users avoid? What are the known limitations? What external dependencies exist? Write this section as if you are briefing a new team member on everything they need to know to use the skill responsibly.

**Section 10: Version History**
A chronological log of every change made to this skill, starting with the initial creation. This section is small when the skill is new and grows over time. It is the proof of your skill's evolution and reliability. We will talk much more about this in Step 5.

---

#### The Important Rule About Templates

We mentioned this in Step 2, but it bears repeating because it is one of the most commonly broken rules in Skill Engineering: **Never paste your entire output template directly into SKILL.md.**

Why does this matter? Because when SKILL.md becomes huge and cluttered, it becomes hard to maintain, slow to load, and confusing to read. The skill logic and the output template are two separate concerns. Keeping them in separate files means you can update one without touching the other.

The professional practice is simple:
1. Save your output template as `references/output-template.md`
2. In SKILL.md Section 6, write: *"Refer to references/output-template.md for the complete document structure and formatting requirements."*
3. Done. Your SKILL.md stays clean and focused.

---

#### How to Build It in Practice

Here is the most important thing a beginner needs to know about building SKILL.md: **you do not type every word yourself.**

You write a **skill development prompt** — a structured description explaining what you want the skill to do, who it is for, what goes in, what comes out, and what rules it must follow. This prompt draws directly from the work you did in Steps 1 and 2.

You give that prompt to an AI tool. The AI builds the complete, properly formatted SKILL.md for you — all 10 sections, correctly structured, professionally written. The process typically takes 5 to 15 minutes of conversation with the AI.

Then **you review it.** You check that the execution flow makes sense. You verify that the quality rules are specific enough. You confirm that the role settings are appropriate. You adjust anything that is not quite right.

This combination — your domain expertise guiding the AI's construction ability — produces skills that are both practically accurate and technically well-structured. The AI knows how to format a skill file correctly. You know whether the content inside it is correct. Together, you produce something better than either could alone.

---

### Step 4: Testing Your Skill Properly
### (Making Sure the Recipe Actually Works)

---

#### What It Means

You have built your skill file. It looks good on paper. But looking good and working well are two very different things. Step 4 is where you find out which one you actually have.

Think of this phase like a restaurant doing a test run — sometimes called a "soft opening" — before inviting real customers. During a soft opening, the chefs cook every dish on the menu. The manager tastes everything. The waitstaff practices their service flow. Problems that were invisible during planning become obvious once the kitchen is actually running. This is exactly the purpose of testing your skill.

Testing gives you three critical things: **confidence** that the skill works as intended, **evidence** that you can show to others, and **discovery** of problems you did not anticipate during design. All three are valuable. All three are only available through testing.

---

#### The 4 Levels of Testing

Professional Skill Engineers do not just run the skill once and declare it finished. They test systematically, at four levels, each one probing a different aspect of the skill's reliability.

**Level 1: Functionality Test — The Foundation**

This is your most basic, most essential test. Run the skill with a complete, standard set of inputs — exactly the kind of inputs a normal user would provide in a normal situation. Then check the output against your specification.

Ask these questions about the output:
- Are all required sections present?
- Is the minimum word count met?
- Does the structure match the template?
- Are all quality validation rules passed?
- Does the content make logical sense?

If the answer to all of these is yes, congratulations — your skill works at a basic level. If any answer is no, you have found your first improvement item. Write it down. Do not fix it yet. Keep testing first.

This is your **minimum requirement**. A skill that fails the functionality test is not ready to share with anyone. A skill that passes it is ready for the next level of testing.

**Level 2: Quality Validation Test — Does the Guardrail Work?**

Your SKILL.md contains quality validation rules. This test checks whether those rules actually do their job. To test them, you intentionally break things.

- Provide incomplete inputs and see if the skill catches the problem
- Provide contradictory inputs and see how the skill handles the conflict
- Deliberately trigger a known quality failure and see if the skill detects and fixes it automatically

This test is counterintuitive for beginners. You are trying to find failures, not avoid them. Every failure you find during testing is a failure that will not reach a real user. Every problem you catch here is a problem you get to fix in a controlled environment rather than a stressful professional situation.

If your quality validation rules work correctly, the skill should either fix the problem automatically or clearly alert the user that something is missing. If the skill just silently produces poor output, your rules are not strong enough — and you have learned something important.

**Level 3: Boundary Case Test — The Edge Cases**

Real-world users are creative in unexpected ways. They will use your skill in situations you did not plan for. The boundary case test prepares you for this reality.

Try unusual, extreme, or surprising inputs:
- A client name that is a very long string (something like "International Consortium for Advanced Technology Development Ltd.")
- An industry that your skill has never been designed for (perhaps "deep-sea fish farming" or "mobile circus entertainment")
- Pain points that are extremely vague or contradictory
- Optional inputs that are missing entirely

A well-designed skill handles these situations gracefully. It does not crash, produce garbled output, or make embarrassing mistakes. It adapts to the unusual input and still produces something reasonable, even if it is simpler than usual.

If your skill falls apart on boundary cases, you have found things to improve in your execution flow and input validation rules.

**Level 4: Reusability Test — Does It Scale?**

The whole purpose of building an AI Skill rather than just having a one-time AI conversation is reusability. Level 4 tests whether that promise is real.

Take your skill and run it with an entirely different set of inputs. Different client. Different industry. Different pain points. Different context altogether. Ask yourself: does the output maintain consistent quality? Does it feel like it was produced by the same reliable system? Or does quality drop dramatically when the scenario changes?

If the skill produces consistently high-quality output across multiple different scenarios, it has passed the reusability test. It is genuinely reusable. If quality varies significantly, something in your design needs attention — probably either the execution flow logic or the output specification.

---

#### What to Record During Testing

Testing is only valuable if you capture what you learn. After each test run, record:

- **What worked correctly** — specific positive observations, not just "it was good"
- **What failed or produced poor results** — specific descriptions of the failure
- **Any error messages** — exact text, if applicable
- **Ideas for improvement** — what would make this better?

Keep this record organized. Each test output document, with your annotations, becomes part of your evidence file for this skill.

---

#### Why Testing Matters for Your Evidence Chain

There is another reason testing is important beyond simply ensuring quality: **your test results are your proof.**

In professional settings, you will often need to demonstrate that a skill works — to a manager, to a client, to a new team member. If you have a folder of test outputs showing the skill performing correctly across multiple scenarios, that proof is immediately available and convincing.

Save all test outputs in a dedicated folder. Many Skill Engineers use a naming convention like:
```
5-skill-execution-outcomes/
├── test-01-standard-case-output.md
├── test-02-missing-input-handling.md
├── test-03-boundary-case-longname.md
└── test-04-different-industry-reuse.md
```

Each file in this folder is a piece of evidence. Together they build a compelling picture of a skill that works reliably across real-world conditions. Over time, this evidence chain becomes one of the most valuable parts of your professional portfolio.

---

#### A Quick Note on First-Run Expectations

One important truth for beginners: **your first run will almost certainly produce something imperfect.** This is completely normal and expected. Even the most experienced Skill Engineers produce skills that need refinement after the first test. The point of testing is not to confirm that everything is perfect. The point is to find what needs improvement — systematically, before it becomes someone else's problem.

If your first test run reveals three problems, that is a success. You found three things to fix. That is far better than discovering them after sharing the skill with your entire team.

---

### Step 5: Improving with Version History
### (Getting Better Over Time)

---

#### What It Means

Your skill passed the functionality test. It mostly works. You are probably feeling good about it — and you should. Completing a working first version is a real achievement. But here is the truth that separates good Skill Engineers from excellent ones: **version 1.0 is never the best version.**

Every skill has room to improve. Every use in the real world reveals something new. A word count that is slightly too short. A quality rule that is slightly too strict. A section that everyone finds confusing. A boundary case you never anticipated. These discoveries are not failures — they are opportunities. And Step 5 is how you turn those opportunities into a skill that genuinely gets better over time.

Think of version history like the update system on your phone. When an app is released, it works. But after millions of people use it, the developers discover problems they never saw in testing. So they release an update: version 1.1. Then another: version 1.2. Then a major redesign: version 2.0. Each version is better than the last because it incorporates real learning from real use.

Your AI Skill follows exactly the same model.

---

#### How Version Numbers Work

Version numbers follow a simple, universally understood convention:

- **v1.0** — Your first complete, working version. The milestone of "it works."
- **v1.1** — A small improvement or bug fix. Something minor that you discovered and corrected.
- **v1.2** — Another small improvement. Perhaps you expanded a section or tightened a quality rule.
- **v1.x** — Continue incrementing for each small refinement.
- **v2.0** — A major redesign. New structure, significant new capability, or fundamentally improved approach.

The rule of thumb: if the fundamental structure and purpose of the skill stays the same, increment the minor version number. If you are redesigning the skill substantially, increment the major version number.

There is no rush to reach v2.0. A skill at v1.8 with eight carefully documented improvements is more trustworthy than a skill that skipped from v1.0 to v2.0 with no explanation of what changed.

---

#### The Golden Rule of Iteration

This rule is so important that we are going to put it on its own line so it is impossible to miss:

> **Every fix MUST be written back into the skill file.**

This seems obvious when you read it. But in practice, it is the rule that beginners most frequently break — and the consequences are significant.

Here is what often happens: A user runs the skill, finds a problem, explains the problem to the AI in conversation, the AI fixes it in that conversation, the output comes out correctly, and the user moves on. Problem solved, right?

Wrong. The skill file was never updated. The next time someone uses that skill — or the next time you use it yourself — the same problem appears again. Because the skill file still contains the original error. The fix existed only in a conversation that is now closed and forgotten.

The correct workflow is:
1. Find the problem
2. Describe the problem to the AI clearly
3. Tell the AI to fix the problem AND update the skill file
4. Verify the fix worked in a new test
5. Record the change in the version history section of SKILL.md

This workflow ensures that every improvement is permanent, documented, and available to everyone who uses the skill going forward.

---

#### How to Iterate Properly — Step by Step

When a test reveals a problem or when real-world use reveals something that could be better, follow this five-step iteration process:

**Step 1: Identify the problem clearly.**
Be specific. "The output quality is sometimes bad" is not useful. "Section 3 consistently falls below 200 words when the client is from a niche industry" is useful. The more precisely you can describe the problem, the more precisely it can be fixed.

**Step 2: Describe the problem to the AI in writing.**
Write out the problem clearly before asking for a fix. Include an example of the problem occurring. Include what the correct behavior should be.

**Step 3: Tell the AI to fix AND update the skill file simultaneously.**
A common mistake is asking the AI to fix the problem in conversation and then separately asking it to update the file. Instead, say: "Please fix this problem and update SKILL.md to version 1.1 with the correction applied and a version history entry added."

**Step 4: Verify the fix worked.**
Run the skill again with the same inputs that previously caused the problem. Confirm that the problem no longer occurs. Also run a standard test to make sure the fix did not accidentally break something else.

**Step 5: Archive the evidence.**
Save the new test output to your 5-skill-execution-outcomes/ folder. This creates a before-and-after record showing the improvement.

---

#### Example Version History Table

Here is what a healthy version history section looks like after a skill has been through several improvement cycles:

| Version | Date | What Changed |
|---|---|---|
| v1.0 | 2026-05-21 | Initial version created. Core functionality tested and confirmed. |
| v1.1 | 2026-05-22 | Fixed: Chapter 3 word count falling below minimum for niche industries. Added expansion instruction for low-content scenarios. |
| v1.2 | 2026-05-23 | Added: Industry terminology adaptation. Skill now adjusts technical vocabulary based on the client's stated industry. |
| v1.3 | 2026-05-28 | Fixed: Quality rule for client name usage was too strict for multi-entity clients. Relaxed rule to check at section level only. |
| v2.0 | 2026-06-01 | Major redesign: Replaced single-section output with structured 7-chapter format. New references/report-template-v2.md added. Previous template archived. |

Notice how every entry answers three questions: **when** did this change happen, **what exactly** was changed, and **why** was it changed. This is the difference between a version history and a changelog — it tells a story of learning and improvement.

---

#### Why This Matters for Your Career

A skill with a well-maintained version history is not just a tool. It is a professional portfolio piece. It demonstrates something specific and impressive about you:

- You think **systematically** about your work
- You **document** your decisions and changes professionally
- You **learn from mistakes** and fix them rather than repeating them
- Your work **gets better over time** through deliberate iteration
- Other people can **trust and build on** your work because it is transparent

In an environment where everyone is just using AI casually and getting inconsistent results, being the person who builds, maintains, and improves documented AI Skills is a genuine professional differentiator. It signals the same qualities as writing good code, maintaining good documentation, or running good processes — it says that you take your work seriously and you think about the long term.

---

#### The Compound Effect

Here is the final concept for this chapter, and perhaps the most important one to keep in mind as you build your first skill.

Each individual improvement is small. Fixing a word count issue saves a few minutes of rework. Adding terminology adaptation improves relevance slightly. Tightening a quality rule reduces one type of error. Individually, none of these feel dramatic.

But here is what happens over time: **small improvements compound.**

After 10 iterations, your skill is noticeably better than version 1.0. The rough edges have been sanded smooth. The edge cases have been handled. The quality rules have been calibrated against real-world use.

After 25 iterations, your skill is dramatically better. A new colleague picking it up for the first time can produce excellent output without needing to understand all the domain expertise that went into building it.

After 50 iterations, your skill has crossed a threshold into something that can genuinely be described as professional-grade. It handles edge cases gracefully. It enforces high quality standards automatically. It produces consistent, reliable, high-quality output across a wide range of real-world scenarios.

This is how individual expertise becomes organizational knowledge. This is how one person's hard-won professional insights get shared with an entire team, department, or organization. This is why Skill Engineering matters.

Every version update is one more step in that journey.

---

### Chapter Summary

We have covered a lot of ground in this chapter. Let us bring it together clearly.

The **5-Step Method** is your complete framework for building an AI Skill from scratch. The five steps are:

**Step 1: Scene Recognition and Analysis**
Identify a specific, repeating, valuable problem in your work. Use the 5 Signals to evaluate whether it is worth building. Answer the 3 Questions to define the problem precisely. Never skip this step — it is the foundation everything else rests on.

**Step 2: Core Component Design**
Design the four components of your skill before you write a single line of SKILL.md. Define your input parameters (what goes in), your execution flow (what happens inside), your output specification (what comes out), and your quality validation rules (how you know it is good enough). Use variables, not hardcoded values.

**Step 3: Building Your SKILL.md File**
Create the 10-section Skill file using the standard format. Keep templates in the references/ folder rather than inside SKILL.md. Use an AI tool to help you build the file — you bring the domain expertise, the AI brings the structural knowledge. Review and refine until it accurately reflects your design.

**Step 4: Testing Your Skill Properly**
Run all four levels of testing: Functionality Test, Quality Validation Test, Boundary Case Test, and Reusability Test. Record what you find. Save all test outputs as evidence. Expect imperfection in v1.0 — that is what the tests are for.

**Step 5: Improving with Version History**
Every problem found is an opportunity. Fix it, update the skill file, and record the change in version history. Follow the Golden Rule: always write fixes back into the skill file. Track versions with clear, informative descriptions. Let your skill compound over time.

Together, these five steps turn a vague idea into a professional, reusable, documented, continuously improving AI Skill. This is the method used by skill engineers at organizations worldwide. And now you know it too.

---

### What's Coming in Chapter 3

You now understand the full theory behind AI Skill Engineering. You know what a skill is, why it matters, and exactly how to build one using the 5-Step Method. That is real knowledge — but theory is only half the story.

**In Chapter 3, we will build our first real skill together.**

Not a simplified example. Not a demo. A genuine, working AI Skill that you can actually use in your job starting the day you finish reading.

We will go through the entire 5-Step Method in practice, step by step, from a blank page to a fully tested, documented, version-controlled skill — in approximately 30 minutes. Every decision will be explained as we make it. Every question that would naturally occur to a first-time builder will be addressed before you have a chance to feel stuck.

No prior experience required. No technical background needed. Just bring a real task from your own work — something you do regularly that takes too long — and by the end of Chapter 3, you will have turned it into a skill.

**Chapter 3: Let's Build Your First Real Skill Together.**

---

*Chapter 2 Complete — The 5-Step Method Made Simple*
*Next: Chapter 3 — Building Your First Skill From Scratch*

---
