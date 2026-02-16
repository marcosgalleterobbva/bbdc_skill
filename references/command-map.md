# bbdc Command Map

## Table of Contents
- [Environment and bootstrap](#environment-and-bootstrap)
- [Top-level commands](#top-level-commands)
- [PR lifecycle commands](#pr-lifecycle-commands)
- [PR subgroups](#pr-subgroups)
- [High-impact commands](#high-impact-commands)
- [Example command templates](#example-command-templates)

## Environment and bootstrap
Required variables:
- `BITBUCKET_SERVER` (must end with `/rest`)
- `BITBUCKET_API_TOKEN`

Recommended startup check:
- `<bbdc-cmd> doctor`

## Top-level commands
- `doctor`
- `pr ...`

## PR lifecycle commands
- `pr list`
- `pr get`
- `pr create`
- `pr update`
- `pr merge-check`
- `pr merge`
- `pr decline`
- `pr reopen`
- `pr approve`
- `pr unapprove`
- `pr watch`
- `pr unwatch`
- `pr delete`
- `pr for-commit`

## PR subgroups
Participants:
- `pr participants list`
- `pr participants add`
- `pr participants remove`
- `pr participants status`
- `pr participants search`

Comments:
- `pr comments add`
- `pr comments list`
- `pr comments get`
- `pr comments update`
- `pr comments delete`
- `pr comments apply-suggestion`
- `pr comments react`
- `pr comments unreact`

Blockers:
- `pr blockers list`
- `pr blockers add`
- `pr blockers get`
- `pr blockers update`
- `pr blockers delete`

Review workflow:
- `pr review get`
- `pr review complete`
- `pr review discard`

Auto-merge workflow:
- `pr auto-merge get`
- `pr auto-merge set`
- `pr auto-merge cancel`

Diff and inspection:
- `pr activities`
- `pr changes`
- `pr commits`
- `pr diff`
- `pr diff-file`
- `pr diff-stats`
- `pr patch`
- `pr merge-base`
- `pr commit-message`
- `pr rebase-check`
- `pr rebase`

## High-impact commands
Treat these as destructive or state-altering operations:
- `pr merge`
- `pr rebase`
- `pr decline`
- `pr delete`
- `pr comments apply-suggestion`
- `pr blockers update`
- `pr comments delete`

## Example command templates
List open incoming PRs:
```bash
<bbdc-cmd> pr list -p <PROJECT> -r <REPO> --state OPEN --direction INCOMING
```

Create draft PR with reviewers:
```bash
<bbdc-cmd> pr create -p <PROJECT> -r <REPO> \
  --from-branch <SRC> --to-branch <DST> \
  --title "<TITLE>" --description "<DESCRIPTION>" \
  --reviewer <USER1> --reviewer <USER2> --draft
```

Set participant status:
```bash
<bbdc-cmd> pr participants status -p <PROJECT> -r <REPO> <PR_ID> <USER> \
  --status APPROVED
```

Run file-scoped comment query:
```bash
<bbdc-cmd> pr comments list -p <PROJECT> -r <REPO> <PR_ID> --path <FILE_PATH>
```

Stream patch:
```bash
<bbdc-cmd> pr patch -p <PROJECT> -r <REPO> <PR_ID>
```
