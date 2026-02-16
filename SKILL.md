---
name: bbdc-cli
description: Execute and troubleshoot Bitbucket Data Center pull-request workflows with the bbdc CLI. Use when tasks mention bbdc, Bitbucket Data Center, pull-request lifecycle operations (list/create/update/merge/review/comments/blockers), repository participant management, PR diffs/patches, or when translating natural-language Bitbucket requests into exact shell commands.
---

# Bbdc CLI

## Overview
Use this skill to translate Bitbucket Data Center requests into `bbdc` shell commands, execute them safely, and summarize results.

Prefer this skill whenever the user asks for pull-request operations in Bitbucket DC through CLI calls.

## Quick Start
1. Resolve the executable:
   - Prefer `bbdc` if present in `PATH`.
   - Fallback to `python -m bbdc_cli`.
2. Validate auth and base URL before workflows:
   - Run `<bbdc-cmd> doctor`.
3. Choose mode:
   - Read-only inspection: use list/get/diff/activities style commands.
   - Mutating operation: create/update/review/merge/rebase/delete with confirmation-sensitive handling.

## Execution Rules
- Always require `BITBUCKET_SERVER` and `BITBUCKET_API_TOKEN`.
- Require `BITBUCKET_SERVER` to end with `/rest`.
- Prefer `--json` for commands that support it, then summarize into concise Markdown for the user.
- Use narrow pagination (`--limit`, `--max-items`) for exploratory calls.
- For mutating operations, describe the command and expected effect before execution.
- Treat `merge`, `rebase`, `decline`, and `delete` as high-risk operations.

## Command Routing
Use `references/command-map.md` for grouped commands and examples.

If the source CLI changed or command details are uncertain, regenerate a live command table from source:

```bash
python scripts/generate_command_inventory.py \
  --source /Users/O000142/Projects/bb-cli/bbdc_cli/__main__.py
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
