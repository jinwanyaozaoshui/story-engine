# Story Engine Behavioral Evaluation Cases

This file defines inputs, expected rules, and pass criteria only. It does not claim that any model has already passed. Real model/agent results must be recorded after an actual run.

## SE-T001 — should-trigger

**Input**

> I only have one idea: an ordinary person suddenly gains a strange ability and gets pulled into anomalous events in a city. Can this develop into a sustainable story?

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-RC-001`

**Expected behavior**

- Treat the input as incomplete; identify quick diagnosis or idea completion mode; do not turn unknown details into canon; provide minimal missing fields or candidate directions marked as assumptions/suggestions.

**Forbidden behavior**

- Invent the protagonist's job, organization, power details, or ending as confirmed fact.
- Announce that a complete plot engine is already established.
- Ask a long questionnaire before offering any diagnosis.

**Pass criteria**

- Story Engine is triggered.
- `SE-RC-001` is used.
- Output acknowledges insufficient evidence or unverifiable items.
- Output uses assumption or suggestion labels.
- Unknown canon is not presented as confirmed.

## SE-T002 — should-trigger

**Input**

> The protagonist must obtain a sealed document within three days or an ally will be expelled from the organization. The document is inside a restricted facility. The protagonist can enter in disguise or ask a former classmate for help, but both choices leave traces. The document is obtained, but the facility records the protagonist as suspicious.

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-RC-001`

**Expected behavior**

- Identify activation/goal, inaction cost, constraints, costly choices, settlement, and persistent residue.

**Forbidden behavior**

- Ignore the time limit.
- Treat obtaining the document as the only outcome.
- Omit the suspicious-person public-label residue.

**Pass criteria**

- Story Engine is triggered.
- `SE-RC-001` is used.
- The three-day document objective is identified as the current goal.
- The ally's expulsion is identified as the cost of inaction.
- The restricted facility and traces are identified as constraints.
- Disguise and asking the former classmate are identified as choices.
- The suspicious-person label is identified as persistent residue.

## SE-T003 — should-trigger

**Input**

> Stage 1: the protagonist saves a witness, owes an organization a favor, and is remembered by an opponent. Stage 2: the protagonist travels to another city for a new incident after a stranger sends a commission; the witness, the favor, and the opponent's pursuit do not affect the investigation.

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-RC-001, SE-F-001`

**Expected behavior**

- Run the delete-previous-stage test; notice Stage 2 survives almost unchanged; flag restart/continuity risk without declaring the work failed; propose a continuity repair.

**Forbidden behavior**

- Treat changing cities as automatic restart.
- Turn a risk rule into a quality verdict.
- Ignore the witness, favor, or opponent as inherited residue.

**Pass criteria**

- Story Engine is triggered.
- `SE-F-001` is used.
- A delete-previous-stage test appears.
- Stage 2 is judged to remain mostly intact without Stage 1.
- The risk wording is not a hard verdict.
- A repair uses at least one inherited residue item.

## SE-T004 — should-trigger

**Input**

> I have three consecutive events. Each begins with receiving a task, entering a dangerous location, finding a victim clue, using the same ability to solve the obstacle, receiving a reward, and getting another task. Only the location and enemy names change. Is this too formulaic?

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-F-002`

**Expected behavior**

- Compare the three cycles; separate stable genre promise, productive variation, and formulaic risk; in this input, flag relatively high repetition risk.

**Forbidden behavior**

- Treat dangerous-location tasks themselves as a failure.
- Treat renamed locations/enemies as meaningful structural change by themselves.
- Ignore that the same solution keeps working.

**Pass criteria**

- Story Engine is triggered.
- `SE-F-002` is used.
- Output distinguishes genre promise, productive variation, and formulaic risk.
- Major structural variables are identified as highly isomorphic.
- Genre repetition is not automatically equated with failure.

## SE-T005 — should-trigger

**Input**

> By day, the protagonist runs a small shop and must pay rent and retain employees; at night, the protagonist investigates anomalous incidents. A special object obtained at night improves shop security but attracts regulatory inspection. Employees begin to suspect the protagonist is hiding something, affecting the next decision.

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-RC-004, SE-F-003`

**Expected behavior**

- Identify the functions of the reality and hidden lines, show hidden-to-reality return flow, and use multi-engine function checks without treating temporary imbalance as automatic failure.

**Forbidden behavior**

- Treat the special object as a reward only.
- Ignore rent, employees, or regulatory inspection.
- Declare any dual-line structure imbalanced by default.

**Pass criteria**

- Story Engine is triggered.
- `SE-RC-004` and `SE-F-003` are used.
- Both reality and hidden goals are identified.
- Hidden results are shown feeding back into reality.
- No hard failure verdict is issued solely because there are multiple lines.

## SE-T006 — should-trigger

**Input**

> In the ending, the protagonist closes the long-term threat. The remaining work is to settle survivors, handle exposure consequences, repay promises, and decide whether to keep a dangerous device. The story is preparing to end.

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-RC-001`

**Expected behavior**

- Recognize terminal closure; do not demand another objective; instead examine settlement, consequences, responsibility, relationships, public labels, and medium/location state.

**Forbidden behavior**

- Require another mission.
- Call stopping the loop an engine failure.
- Ignore settlement and promises as consequences.

**Pass criteria**

- Story Engine is triggered.
- Terminal closure is identified.
- No new objective is required.
- At least three terminal residue categories are checked.

## SE-T007 — should-not-trigger

**Input**

> Please polish this prose so the sentences are more elegant and literary.

**Expected trigger**

- expected_trigger: `false`
- expected_rules: `none`

**Expected behavior**

- Do not use Story Engine as the primary tool; identify the request as prose/style work. Story Engine may only assist with structure if requested.

**Forbidden behavior**

- Run all eight rule cards.
- Rewrite the request into a stage-engine task.
- Claim a prose-specialist skill is installed when it is not known.

**Pass criteria**

- Story Engine is not the primary trigger.
- No specific Story Engine rule is used as the main workflow.
- The request is correctly identified as prose/style work.

## SE-T008 — should-not-trigger

**Input**

> Design a complete character arc in which the protagonist moves from insecurity to self-acceptance, including inner flaw, relationship repair, and emotional turning points.

**Expected trigger**

- expected_trigger: `false`
- expected_rules: `none`

**Expected behavior**

- Do not use Story Engine as the primary workflow; identify the request as full character-arc design. Story Engine can only assist with structural consequences and choice costs.

**Forbidden behavior**

- Replace full character-arc design with plot-engine diagnosis.
- Present invented backstory as confirmed fact.
- Rewrite the user's request merely to force a Story Engine trigger.

**Pass criteria**

- Story Engine is not the primary trigger.
- No specific Story Engine rule is used as the main workflow.
- Story Engine's role is described as structural assistance only.

## SE-T009 — edge

**Input**

> I want the protagonist to change professions and enter a new region. Does that automatically mean the story restarts?

**Expected trigger**

- expected_trigger: `true`
- expected_rules: `SE-F-001`

**Expected behavior**

- Trigger boundary diagnosis; explain that a new profession or map does not automatically equal restart; inspect inherited residue from the previous stage.

**Forbidden behavior**

- Automatically diagnose restart.
- Say the protagonist must not change profession or region.
- Ignore identity, access, resources, responsibility, relationships, knowledge, public labels, and medium/location state.

**Pass criteria**

- Story Engine is triggered.
- `SE-F-001` is used.
- The answer explicitly rejects automatic restart judgment.
- The eight residue categories are checked or requested.
