---
name: bbdc-cli
description: Execute and troubleshoot Bitbucket Data Center workflows with the bbdc CLI. Use when tasks mention bbdc, Bitbucket Data Center, pull-request lifecycle operations (list/create/update/merge/review/comments/blockers), authenticated-account lookups (recent repos, SSH/GPG keys, profile/settings), repository participant management, PR diffs/patches, or when translating natural-language Bitbucket requests into exact shell commands.
---

# Bbdc CLI

## Overview
Use this skill to translate natural-language Bitbucket Data Center requests into `bbdc` commands, execute safely, and return concise results.

Prefer this skill for pull request lifecycle work, authenticated account lookups, participants/reviewers, comments/blockers, rebase/merge checks, and batch PR workflows.

## Quick Start
1. Resolve the executable:
   - Prefer `bbdc` if present in `PATH`.
   - Fallback to `python -m bbdc_cli`.
2. Validate auth and base URL before workflows:
   - Run `<bbdc-cmd> doctor`.
3. Choose mode:
   - Read-only inspection: use list/get/diff/activities style commands.
   - Mutating operation: create/update/review/merge/rebase/delete with confirmation-sensitive handling.

## Natural-Language Workflow
1. Classify the request:
   - Account lookup vs PR workflow.
   - Single PR vs multi-PR batch.
   - Read-only vs state-changing.
2. Extract required slots:
   - PR workflows: `project`, `repo` (and usually `pr_id`).
   - Account workflows: optional `user_slug` for profile/settings.
   - PR-targeted: `pr_id`.
   - Command-specific fields (reviewers, comment text, status, branch names, etc.).
3. If required slots are missing, ask focused follow-up questions before running commands.
4. Build the narrowest command that satisfies the user request.
5. For mutating commands:
   - Show the exact command and expected effect before execution.
6. After execution, return:
   - Command run.
   - Key IDs/state changes.
   - One verification command when useful.

## Execution Rules
- Always require `BITBUCKET_SERVER` and `BITBUCKET_API_TOKEN`.
- Require `BITBUCKET_SERVER` to end with `/rest`.
- Prefer `--json` for commands that support it, then summarize into concise Markdown for the user.
- Use narrow pagination (`--limit`, `--max-items`) for exploratory calls.
- For mutating operations, describe the command and expected effect before execution.
- Treat `merge`, `rebase`, `decline`, and `delete` as high-risk operations.
- Treat `pr batch ...` mutating commands as high-risk operations.

## Command Routing
Use `references/command-map.md` for grouped commands and examples.
Use `references/nl-intent-playbook.md` for intent-to-command templates.

If the source CLI changed or command details are uncertain, regenerate a live command table from source:

```bash
python scripts/generate_command_inventory.py \
  --source <PATH_TO_BBDC_CLI_MAIN>
```

For full command coverage (including `pr batch ...`), refresh:

```bash
python scripts/generate_command_inventory.py \
  --source <PATH_TO_BBDC_CLI_MAIN> \
  --output references/generated-command-inventory.md
```

## Mutating Workflow Pattern
1. Fetch current state if needed (`pr get`, `participants list`, `comments get`).
2. If versioned endpoint is involved, allow auto-version behavior by omitting `--version` unless the user supplies one.
3. Execute the command.
4. Return:
   - Exact command run.
   - Key resulting IDs/URL/state.
   - Any follow-up command needed for verification.

## Common Tasks
- List open PRs:
  - `<bbdc-cmd> pr list -p <PROJECT> -r <REPO> --state OPEN --direction INCOMING`
- Create PR:
  - `<bbdc-cmd> pr create -p <PROJECT> -r <REPO> --from-branch <SRC> --to-branch <DST> --title "..." --reviewer <USER>`
- Review completion:
  - `<bbdc-cmd> pr review complete -p <PROJECT> -r <REPO> <PR_ID> --status APPROVED`
- File comments:
  - `<bbdc-cmd> pr comments list -p <PROJECT> -r <REPO> <PR_ID> --path <FILE_PATH>`
- Rebase check:
  - `<bbdc-cmd> pr rebase-check -p <PROJECT> -r <REPO> <PR_ID>`
- Batch approve:
  - `<bbdc-cmd> pr batch approve -p <PROJECT> -r <REPO> -f <FILE.json>`
- Account snapshot:
  - `<bbdc-cmd> account me`
- Account SSH keys:
  - `<bbdc-cmd> account ssh-keys --json`
- Account GPG keys:
  - `<bbdc-cmd> account gpg-keys --json`

## Output Normalization
When users ask for summaries, convert PR JSON into a Markdown table:

```bash
<bbdc-cmd> pr list -p <PROJECT> -r <REPO> --json \
  | python scripts/pr_json_report.py
```

## Troubleshooting
Use `references/source-behavior.md` for:
- strict enum values,
- version and comment-version auto-fetch behavior,
- endpoints implemented through `request_rest`,
- error semantics returned by the CLI.
