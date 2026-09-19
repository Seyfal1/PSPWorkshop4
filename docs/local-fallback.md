# Local fallback without a repository host

Use this route when host access is unavailable. It exercises real Git branches,
sharing through a local bare repository, conflict resolution and testing. It
does not constitute a hosted pull request.

Two learners can take turns on one machine. If working remotely without a sharing
route, one learner can operate while the partner observes; record the limitation.
A learner may also simulate both roles locally and label this as individual work.

## Establish the local remote

Use an untouched starter extraction and open its `topic4-starter` folder. If
`.git` was omitted, follow SETUP.md to establish the baseline first. Ensure the
sibling names `topic4-local-remote.git` and `topic4-partner-b` do not already exist.

```text
git init --bare --initial-branch=main ../topic4-local-remote.git
git remote add origin ../topic4-local-remote.git
git push -u origin main
git push origin workshop-start
git clone ../topic4-local-remote.git ../topic4-partner-b
```

If the starter already has an origin from an attempted hosted setup, use a fresh
extraction for this fallback; do not replace the existing remote blindly.

Partner A uses the starter folder. Partner B opens the sibling `topic4-partner-b`
folder in a separate editor window and terminal. Each sets their own repository-
local Git identity using SETUP.md. Commit identity belongs to the actual operator.
Follow the two partner briefs in these separate working copies, then integration.md
through step 4. All pushes and fetches now use the local remote and need no network.

## Substitute for the hosted pull request

Inspect the proposed change together from partner A's integration branch:
```text
git diff main...integration/booking-rules
git log --oneline --graph --all --decorate
```

Use the review checklist and record the discussion as a local peer walkthrough.
After verification and review, partner A completes the local merge:
```text
git switch main
git merge --no-ff integration/booking-rules -m "Integrate reviewed booking rules"
git push origin main
```

Partner B then runs:
```text
git switch main
git pull --ff-only origin main
```

Both run the full test suite on main, record the final commit and retain evidence.
Expected: 9 tests pass. Mark hosted pull request and hosted approval as not
performed. A later hosted exercise can complete those steps.
