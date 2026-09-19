# Partner B Activity 1

Requirement: Reject requested quantities above available capacity. A request equal to capacity remains valid.

Do not add the minimum-quantity condition yet. Partner A is implementing it. Both rules will be combined in Activity 2. Keep the function signature
and docstring unchanged to focus the deliberate conflict on the return statement.

## Create your branch

Start with a clean working tree. Both partners must branch from the shared tag:
```text
git switch -c feature/capacity-check workshop-start
```

In your editor, copy `activity-templates/test_capacity.py` to
`tests/test_capacity.py`. Leave the template unchanged. Run the test suite
BEFORE changing booking.py. Expected: 6 tests run, with 2 failures exposing your
missing rule. Record the actual output. These failures are intentional.

macOS/Linux:
```text
python3 -m unittest discover -s tests -v
```
Windows:
```text
py -m unittest discover -s tests -v
```

Change only the return statement in `booking.py` to implement your assigned rule.
Run the tests again. Expected: all 6 pass. Explain why this does not establish
that the other partner's requirement is met.

## Inspect, commit and share

```text
git diff
git add booking.py tests/test_capacity.py
git diff --cached
git diff --cached --check
git commit -m "Implement capacity booking validation with tests"
git push -u origin feature/capacity-check
git status
git rev-parse HEAD
```

The push uses the remote established during setup, including the local fallback
remote if selected. Record the commit identifier and explain your check results.
Do not merge into main. Tell your partner when the branch is available.

Stretch: identify an input that passes your branch but violates the other rule.
After both partners have pushed, open `docs/integration.md`.
