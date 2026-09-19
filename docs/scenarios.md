# Strategy comparison Fifteen-minute activity

Compare a lightweight feature-branch workflow, trunk-based development and Gitflow.
These overlap: trunk-based development can use very short-lived feature branches.
Judge integration habits and release requirements rather than branch names alone.

## Scenario A Hosted booking service
Six developers support one production version. They deliver small changes daily,
automated checks take six minutes, and reviewers are available every working day.
Larger features must remain unavailable to users until ready.

## Scenario B Installed desktop product
Eight developers prepare quarterly releases with a two-week acceptance period.
Next-version development continues during acceptance. Two older versions remain
supported and occasionally need urgent fixes. Review and testing capacity are finite.

## Scenario C Student application
Four learners work at different times. They need attributable contributions,
basic review and one demonstrable submission. Only local tests are currently available.
Some group members can review work only twice a week.

## Pair task
Choose one scenario. Spend three minutes identifying constraints, five comparing
two credible approaches, four writing a decision and three sharing it.

Record:
1. The proposed approach and two relevant scenario facts.
2. A credible alternative and why it is less suitable or needs adaptation.
3. One risk and a practical control.
4. One missing fact that could change your choice.
5. Evidence you would collect to evaluate the approach.

A monthly deployment does not require monthly integration. More branch categories
do not guarantee reliability. Review delays, change size and the reach of a change
all matter. There may be more than one defensible answer.
