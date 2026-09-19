# Activity 2 Resolve and verify integration

Both feature branches must be committed and pushed before beginning. Partner A
operates the integration commands first; partner B checks both requirements.
Swap roles for the pull-request walkthrough. Each learner records their role.

This workshop uses an integration branch before the pull request. The e-learning
showed another valid direction: bringing main into a feature branch. Here main
remains at the baseline until the combined change is reviewed.

## 1 Create the integration branch

Partner A starts with a clean working tree:
```text
git fetch origin
git switch -c integration/booking-rules workshop-start
git merge --ff-only origin/feature/minimum-check
git merge origin/feature/capacity-check
```

Expected: the first merge fast-forwards; the second reports a conflict in
`booking.py`. The different test files combine automatically. If either branch
is missing, confirm the partner pushed it and fetch again. Do not recreate a
partner's branch with unrelated history.

## 2 Inspect before editing

```text
git status
git diff
```

Record the conflict extract. For this merge, HEAD contains the minimum check
and the incoming branch contains the capacity check. These labels describe
direction, not correctness. Explain what keeping only either side would lose.

Agree the intended result: a request is allowed only when the requested quantity
is at least one AND no greater than available capacity. Write one return
expression that implements both requirements and remove the conflict markers.
Do not put two return statements one after another; the second will be unreachable.

## 3 Verify the combined behaviour

Run the full suite (macOS/Linux):
```text
python3 -m unittest discover -s tests -v
```
Windows:
```text
py -m unittest discover -s tests -v
```

Expected: 9 tests pass. Check that both new test files are present. Record actual
results for negative, zero, minimum-valid, exact-capacity, above-capacity and
no-capacity cases. If tests fail, investigate and correct the implementation;
do not weaken the tests to make them pass.

## 4 Complete the paused merge

```text
git add booking.py
git diff --cached
git diff --cached --check
git status
git commit -m "Merge booking rules preserving minimum and capacity requirements"
git push -u origin integration/booking-rules
git log --oneline --graph --all --decorate
git rev-parse HEAD
```

Inspect the automatically staged test addition as well as the resolved file.
The staged diff compares with the current HEAD, not with the original baseline.
The later pull request shows the overall proposed change to main.

If you need to step back BEFORE completing the merge commit, ask the tutor and
use `git merge --abort`. This attempts to restore the pre-merge state. It does
not undo a completed merge commit. Do not use reset --hard or force-push to
recover the exercise. Keep any needed conflict notes before aborting.

## 5 Basic pull request

On the host, create a pull request with base/destination `main` and source
`integration/booking-rules`. Partner A owns the branch; partner B leads review.
Include purpose, both requirements, actual verification results and limitations.
Use `docs/review-checklist.md` and inspect all changed files.

There is no CI configuration in this starter. Local test evidence must not be
described as a passing hosted check. Follow any host-required controls.

Correct review findings and rerun affected checks before merging. For this
exercise choose the host's merge-commit option where available to retain the
branch history. If policy only permits another method, follow it and record the
method; do not weaken repository protection.

## 6 Verify the merged main

After the hosted merge, each learner updates their local repository:
```text
git switch main
git pull --ff-only origin main
git rev-parse HEAD
git log --oneline --graph --all --decorate
git status
```

Run the full test command again on main. Expected: 9 tests pass. If a fast-forward
update is refused, stop and inspect local history with the tutor rather than
forcing it. Record the final commit and actual test results. Retain the branches
until evidence has been captured.

Local fallback: follow the substitute merge steps in `docs/local-fallback.md`;
mark hosted pull-request creation and approval as not performed.
