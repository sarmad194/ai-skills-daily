# Expected Output Criteria — Test 02 (Healthcare)
> Pass/fail checklist. The skill output MUST satisfy ALL criteria to pass.
> AI output wording will vary between runs — that is normal. These criteria check structure and substance, not exact wording.

## Structural Criteria

- [ ] **C1 — Chapter count:** Output contains exactly 5 chapters, numbered and titled.
- [ ] **C2 — Chapter order:** Chapters follow the standard sequence — (1) Client Current Business Status and Background, (2) Pain Point Diagnosis, (3) Solution Approach and Value Proposition, (4) Value Benefits, (5) Implementation Path and Next Step Recommendations.
- [ ] **C3 — Total length:** Output exceeds 1,800 words.
- [ ] **C4 — No placeholders:** No leftover placeholder text such as [INSERT], [TODO], XXX, or unfilled brackets anywhere in the output.

## Content Criteria

- [ ] **C5 — Pain point coverage:** All 7 input pain points appear in Chapter 2, grouped by business domain (e.g., patient experience / systems & data / clinical documentation / compliance & security) rather than listed flat.
- [ ] **C6 — Input data fidelity:** At least 6 of the following specific figures from the input appear correctly in the report: 1,200 beds; 6,500 daily visits; 42 departments; 172 minutes; 8 minutes consultation; 35% over-60 patients; 900 daily questions; 40-minute lab delay; 3.1 hours documentation; 22% incomplete records; 2.4 million rejections; 90-minute target; 95% completeness target; 70% rejection reduction target.
- [ ] **C7 — Quantitative indicators:** Chapter 4 contains at least 9 quantitative value indicators tied to the client's stated targets.
- [ ] **C8 — Value proposition depth:** Chapter 3 contains at least 150 words of solution narrative that explicitly addresses BOTH patient journey redesign AND AI-assisted documentation with physician review.
- [ ] **C9 — Industry terminology:** Report uses healthcare terminology appropriately (e.g., HIS/LIS/PACS/EMR, triage, outpatient journey, discharge summary, reimbursement compliance) — not generic corporate language. Critically, the report must reflect the security constraint: on-premise/private-network deployment and health data compliance must be mentioned.
- [ ] **C10 — Actionable next steps:** Chapter 5 contains a phased implementation path with at least 3 phases AND at least 3 concrete next-step recommendations, including the required security review as an explicit step.

## Cross-Test Criterion (Reusability)

- [ ] **C11 — Terminology adaptation:** Compared with the Test 01 government output, this report demonstrably adapts terminology and framing to healthcare (this validates the v1.1 industry-terminology-adaptation feature).

## Result

- **Pass:** All 11 criteria checked.
- **Fail:** Any criterion unchecked — record failed criteria IDs in TEST-LOG.md notes.
