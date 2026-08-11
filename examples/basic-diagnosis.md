# Example: Basic Stage Diagnosis

## Input

> The protagonist must obtain a sealed document within three days or an ally will be expelled from the organization. The document is stored inside a restricted facility. The protagonist can enter in disguise or ask a former classmate for help, but either route leaves an identity trace. The document is recovered, but the facility flags the protagonist as suspicious.

## Story Engine analysis

- `[CONFIRMED]` Current goal: obtain the document within three days.
- `[CONFIRMED]` Cost of inaction: the ally is expelled.
- `[CONFIRMED]` Constraints: restricted facility, three-day deadline, both paths leave traces.
- `[CONFIRMED]` Costly choices: disguise / ask the former classmate.
- `[CONFIRMED]` Settlement: the document is obtained.
- `[CONFIRMED]` Persistent residue: the facility marks the protagonist as suspicious, changing public-label/identity risk.
- `[UNVERIFIABLE]` No next-stage pull is supplied yet.

## Suggested repair

- `[SUGGESTION]` Make the next-stage entry depend directly on the suspicious-person label—for example restricted access, investigation, or a debt to the former classmate that must be used to bypass a new constraint.
