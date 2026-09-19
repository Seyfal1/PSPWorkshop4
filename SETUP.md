# Setup and baseline

Open this folder in your editor and open a terminal in it. Commands below use
normal Git in either PowerShell or a macOS/Linux terminal.

## 1 Check tools

```text
git --version
```

macOS/Linux:
```text
python3 --version
python3 -m unittest discover -s tests -v
```

Windows:
```text
py --version
py -m unittest discover -s tests -v
```

Use Python 3.10 or newer. Expected baseline: 3 tests pass. These check valid
bookings only. The function still lacks both requested validation rules.
No virtual environment or package installation is required.

## 2 Check Git and identity

```text
git status
git log -1 --oneline
git tag --list
```

Expected branch: `main`, clean working tree, tag `workshop-start`.
Configure your own name and email locally before making commits. Replace the
quoted examples; these settings affect this repository only.

```text
git config user.name "Your Name"
git config user.email "your-approved-email@example.com"
```

If Git reports that this is not a repository, the owner alone should initialise:
```text
git init -b main
git config user.name "Your Name"
git config user.email "your-approved-email@example.com"
git add .
git commit -m "Establish Topic 4 workshop baseline"
git tag workshop-start
```

## 3 Establish one shared repository per pair

Partner A is the repository owner for setup. Use a new empty private repository
on the tutor-approved host; do not add a README, licence or gitignore there.
Give partner B appropriate collaborator access through the host's normal process.
Replace REPOSITORY_URL with the actual clone URL, without angle brackets.

Partner A, from this starter folder:
```text
git remote add origin REPOSITORY_URL
git push -u origin main
git push origin workshop-start
```

Partner B, from a parent folder where `topic4-pair` does not already exist:
```text
git clone REPOSITORY_URL topic4-pair
cd topic4-pair
git config user.name "Your Name"
git config user.email "your-approved-email@example.com"
```

Partner B must use this clone for the activity, not a separately initialised
starter. Use the host's approved sign-in method; never put tokens in project files.
If access fails, record it and use `docs/local-fallback.md` with the tutor.

## 4 Record the baseline

Both partners run tests in their own working copy and record:
```text
git status
git rev-parse HEAD
```

Record the actual results, commit identifier and chosen sharing route. Keep
evidence separately until integration so the log does not create an extra conflict.

Next: complete `docs/scenarios.md`, then your assigned partner brief. Both
feature branches start from `workshop-start`. Do not merge either into main yet.
