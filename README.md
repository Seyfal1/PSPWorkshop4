# Topic 4 Branching strategies

Improve a simplified booking function through separate branches, a controlled
conflict and a basic pull request. Explain how the final version preserves
both requirements and why a branching strategy fits a delivery scenario.

Start with `SETUP.md`. No previous workshop files or third-party Python
packages are needed. Use Python 3.10 or newer, Git, an editor and a terminal.
Hosted work additionally needs a repository account and an agreed sharing route.

## Project map

- `booking.py`: intentionally incomplete booking rule.
- `tests/`: three existing tests; their success does not prove all requirements.
- `activity-templates/`: partner tests to copy into `tests/` on separate branches.
- `docs/partner-a.md` and `docs/partner-b.md`: separate change requirements.
- `docs/integration.md`: conflict, pull request and final verification walkthrough.
- `docs/scenarios.md`: strategy comparison activity.
- `docs/evidence-log.md`: record your own actual results and decisions.
- `docs/review-checklist.md`: short review prompts.
- `docs/local-fallback.md`: the same Git exercise without a hosted service.

## Teaching scope

Inputs are integers and capacity is non-negative. A valid booking requires at
least one place and cannot exceed capacity. Type validation, persistence and
concurrency are outside scope. This is not a production booking system.

Run tests from the project root with `python3 -m unittest discover -s tests -v`
on macOS/Linux, or `py -m unittest discover -s tests -v` on Windows.
Do not run discovery in `activity-templates`; these are deliberately separate
from the active baseline tests. Copy only your assigned test file during Activity 1.

All test counts in the guides are expected outcomes. Record what you actually
observe. Each learner should retain their own evidence log or handout; avoid
editing the shared evidence file on both feature branches during the exercise.
