# Chapter 4: Using and Testing Skills

## Two things this chapter teaches

First, how to invoke a skill so it runs the way you intend. Second, how to test a skill so you can trust it. Testing is the step that separates a hobby prompt from an engineered skill, and it is the step most people skip.

## Invoking a skill

To invoke a skill, you name it and supply its inputs. In most tools the pattern looks like this, typed to the agent:

```
Use the meeting_notes_summarizer skill.
meeting_date: 2026-06-18
participants: Alex Morgan (Account Manager), Priya Nair (Consultant)
meeting_topic: Discovery call
raw_notes: <paste your rough notes here>
```

The agent then loads the skill, checks the input contract, and follows the process. If a required input is missing, a well built skill asks for it before generating anything, exactly as the `skill_runner.py` script demonstrated in Chapter 3.

A practical habit: invoke skills in a fresh conversation, not the one where you wrote or discussed the skill. Leftover context from the writing session can quietly fill gaps that a real user would hit. Testing fresh reveals those gaps.

## The testing pyramid

Test in three widening layers.

1. The normal case. One clear, ordinary input that should plainly succeed. This confirms the skill works at all.
2. The missing case. An input with a required field left out. This confirms the skill asks rather than invents.
3. The unusual case. An input at the edge of what the skill was meant for. This shows you where the skill bends and where its limits are.

Passing all three does not mean the skill is perfect. It means the skill is dependable across the range you tested, which is what reliability actually means.

## The golden test set

For any skill you will keep, build a golden test set: a small folder of fixed test cases that never change. This lets you answer a question that is otherwise impossible to answer by eye: when I improve the skill, did I break something that used to work?

A golden test set looks like this:

```
my-skill/
  SKILL.md
  tests/
    test-01-normal/
      input.md        The fixed input, never edited.
      expected.md     A checklist of what the output must contain.
    test-02-edge/
      input.md
      expected.md
    TEST-LOG.md        Results per version.
```

The `expected.md` is not a full expected output, because AI output varies between runs. Instead it is a pass or fail checklist of measurable criteria, for example:

```
- [ ] Contains exactly 5 chapters
- [ ] Action items are in a table with owner and deadline
- [ ] Total length exceeds 1800 words
- [ ] No placeholder text such as [INSERT] remains
```

## Regression testing: the professional habit

Here is the rule that makes a skill trustworthy over time:

Every time you change a skill's version, re run all tests and record the results in `TEST-LOG.md` before you commit the change.

If version 1.2 fails a test that version 1.1 passed, that is a regression. You fix it before publishing. The log looks like this:

```
| Date       | Version | Test 01 | Test 02 | Notes                          |
|------------|---------|---------|---------|--------------------------------|
| 2026-07-02 | v1.1    | Pass    | Pass    | Baseline                       |
| 2026-07-09 | v1.2    | Pass    | Fail    | Indicator count dropped; fixed |
```

Almost nobody in the AI skills space does this yet. A repository that contains `tests/` folders and a `TEST-LOG.md` signals real engineering discipline, and it is the kind of detail that reviewers and hiring panels notice.

## Judging output quality

When you check a skill's output, judge it against the skill's own declared output and constraints, not against a vague sense of "good." Ask:

- Did it produce the declared output shape?
- Did it honor every constraint?
- Did it use only the inputs supplied, without inventing facts?
- Would a second run on the same input produce output of the same shape and quality?

If the answer to any of these is no, the fix goes into the skill file, and the version goes up.

## Common failure modes and their fixes

- The skill invents missing information. Fix: strengthen the input contract so the skill stops and asks.
- The output shape drifts between runs. Fix: make the Output section more precise, and add an Example the agent can imitate.
- The skill is used at the wrong moment. Fix: sharpen the description so it says clearly when to use the skill.
- An improvement broke an old behavior. Fix: this is why the golden test set exists; catch it in the log and repair before publishing.

## Key terms from this chapter

- Invoke: to name a skill and supply its inputs so the agent runs it.
- Testing pyramid: testing the normal case, the missing case, and the unusual case.
- Golden test set: a fixed folder of test cases with pass or fail checklists.
- Regression: a change that breaks a behavior that previously worked.

## What is coming next

Part 1 is complete. You understand skills, agents, how to build a skill, and how to test one. Part 2 turns to the tools you will do this work in. Chapter 5 begins with WorkBuddy.
