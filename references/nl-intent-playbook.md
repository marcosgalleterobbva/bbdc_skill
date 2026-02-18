# bbdc Natural-Language Intent Playbook

Use this playbook to map user requests into concrete `bbdc` commands.

## Required Context
- PR workflows require: `project`, `repo`
- PR item operations usually require: `pr_id` (except repo-level list/search commands)
- Account profile/settings may require: `user_slug` (or env fallback)
- Batch commands require: `--file` JSON list (or `-` with stdin)

## Intent Routing

| User intent pattern | Command template | Required fields |
|---|---|---|
| "list open PRs" / "show incoming PRs" | `<bbdc-cmd> pr list -p <PROJECT> -r <REPO> --state OPEN --direction INCOMING --json` | `project`, `repo` |
| "show my account info" / "who am I in bitbucket" | `<bbdc-cmd> account me` | none |
| "show my recently accessed repos" | `<bbdc-cmd> account recent-repos --json` | none |
| "show my ssh keys" | `<bbdc-cmd> account ssh-keys --json` | none |
| "show my gpg keys" | `<bbdc-cmd> account gpg-keys --json` | none |
| "show my profile details" | `<bbdc-cmd> account user --user-slug <USER_SLUG>` | `user_slug` (or env fallback) |
| "show my account settings" | `<bbdc-cmd> account settings --user-slug <USER_SLUG>` | `user_slug` (or env fallback) |
| "get PR 123" / "show PR details" | `<bbdc-cmd> pr get -p <PROJECT> -r <REPO> <PR_ID>` | `project`, `repo`, `pr_id` |
| "create PR from X to Y" | `<bbdc-cmd> pr create -p <PROJECT> -r <REPO> --from-branch <SRC> --to-branch <DST> --title "<TITLE>" --description "<DESC>" --reviewer <USER>` | `project`, `repo`, `from_branch`, `to_branch`, `title` |
| "approve PR 123" | `<bbdc-cmd> pr approve -p <PROJECT> -r <REPO> <PR_ID>` | `project`, `repo`, `pr_id` |
| "complete review for PR 123 as approved" | `<bbdc-cmd> pr review complete -p <PROJECT> -r <REPO> <PR_ID> --status APPROVED --comment "<TEXT>" --json` | `project`, `repo`, `pr_id` |
| "decline PR 123" | `<bbdc-cmd> pr decline -p <PROJECT> -r <REPO> <PR_ID> --comment "<TEXT>" --json` | `project`, `repo`, `pr_id` |
| "merge PR 123" | `<bbdc-cmd> pr merge -p <PROJECT> -r <REPO> <PR_ID> --message "<MSG>" --json` | `project`, `repo`, `pr_id` |
| "check if PR 123 can merge" | `<bbdc-cmd> pr merge-check -p <PROJECT> -r <REPO> <PR_ID>` | `project`, `repo`, `pr_id` |
| "check if PR 123 can rebase" | `<bbdc-cmd> pr rebase-check -p <PROJECT> -r <REPO> <PR_ID>` | `project`, `repo`, `pr_id` |
| "rebase PR 123" | `<bbdc-cmd> pr rebase -p <PROJECT> -r <REPO> <PR_ID> --json` | `project`, `repo`, `pr_id` |
| "add reviewer alice to PR 123" | `<bbdc-cmd> pr participants add -p <PROJECT> -r <REPO> <PR_ID> --user <USER> --role REVIEWER --json` | `project`, `repo`, `pr_id`, `user` |
| "set alice as approved on PR 123" | `<bbdc-cmd> pr participants status -p <PROJECT> -r <REPO> <PR_ID> <USER> --status APPROVED --json` | `project`, `repo`, `pr_id`, `user` |
| "list comments for file in PR 123" | `<bbdc-cmd> pr comments list -p <PROJECT> -r <REPO> <PR_ID> --path <FILE_PATH> --json` | `project`, `repo`, `pr_id`, `path` |
| "add comment to PR 123" | `<bbdc-cmd> pr comments add -p <PROJECT> -r <REPO> <PR_ID> --text "<TEXT>"` | `project`, `repo`, `pr_id`, `text` |
| "show blockers on PR 123" | `<bbdc-cmd> pr blockers list -p <PROJECT> -r <REPO> <PR_ID> --json` | `project`, `repo`, `pr_id` |
| "approve these PRs: 1,2,3" | `<bbdc-cmd> pr batch approve -p <PROJECT> -r <REPO> -f <FILE.json> --json` | `project`, `repo`, JSON items with `pr_id` |
| "merge these PRs" | `<bbdc-cmd> pr batch merge -p <PROJECT> -r <REPO> -f <FILE.json> --json` | `project`, `repo`, JSON items with `pr_id` |

## Clarification Rules
- If `project` or `repo` is missing for PR intents, ask for both in one message.
- If `pr_id` is missing for PR-scoped intents, ask for it before generating commands.
- If a profile/settings intent has no `user_slug` and no env fallback, ask for `user_slug`.
- If a request is ambiguous between single and batch, ask whether to run one PR or many.
- If high-risk (merge/rebase/decline/delete or batch mutating), confirm intent before generating commands.

## Codex Runtime Model (BBVA)
- Never execute `bbdc` in Codex.
- Always provide exact commands for the user to run locally.
- Ask for pasted output (JSON or terminal output).
- Resume analysis/next commands from the user-provided output.

## Safe Defaults
- Prefer read-only commands when the request can be satisfied without mutation.
- Omit `--version` unless the user explicitly provides it; CLI auto-fetches when supported.
- For exploratory queries, include `--limit` and `--max-items` to constrain results.
