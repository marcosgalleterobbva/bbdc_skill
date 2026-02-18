# bbdc Source Behavior Notes

## Table of Contents
- [Core assumptions](#core-assumptions)
- [Validation and enums](#validation-and-enums)
- [Auto-version behavior](#auto-version-behavior)
- [Pagination behavior](#pagination-behavior)
- [Authenticated account behavior](#authenticated-account-behavior)
- [Codex runtime behavior](#codex-runtime-behavior)
- [Raw vs JSON responses](#raw-vs-json-responses)
- [Special REST routes](#special-rest-routes)
- [Batch execution behavior](#batch-execution-behavior)
- [Error semantics](#error-semantics)

## Core assumptions
- Base API uses `BITBUCKET_SERVER/api/latest/...`.
- `BITBUCKET_SERVER` must end with `/rest`.
- `BITBUCKET_API_TOKEN` is sent as `Authorization: Bearer <token>`.

## Validation and enums
Strict values enforced in code:
- Role: `AUTHOR`, `REVIEWER`, `PARTICIPANT`
- Participant status: `UNAPPROVED`, `NEEDS_WORK`, `APPROVED`
- Comment state: `OPEN`, `RESOLVED`
- Comment severity: `NORMAL`, `BLOCKER`

When a value is invalid, CLI exits with a `BBError` explaining allowed values.

## Auto-version behavior
If omitted, CLI auto-fetches version fields for commands that need concurrency tokens.

PR version auto-fetch used by:
- `pr decline`
- `pr reopen`
- `pr merge`
- `pr update`
- `pr rebase`
- `pr delete`
- `pr comments apply-suggestion` (PR version)

Comment version auto-fetch used by:
- `pr comments update`
- `pr comments delete`
- `pr comments apply-suggestion` (comment version)
- `pr blockers update`
- `pr blockers delete`

## Pagination behavior
Paged endpoints use `start`, `limit`, and `nextPageStart`.

Default caps in command implementations:
- `--limit 50`
- `--max-items 200`

## Authenticated account behavior
`account me` aggregates:
- `account recent-repos` (`/api/latest/profile/recent/repos`)
- `account ssh-keys` (`/ssh/latest/keys`)
- `account gpg-keys` (`/gpg/latest/keys`)
- `account me` has no `--json` flag and already prints JSON output by default.

For BBVA HTTP access tokens:
- Some user-account endpoints may return `401`.
- `account me` is designed to return partial results with `errors` and `notes` instead of failing immediately.

User profile/settings retrieval (`account user`, `account settings`, optional in `account me`) resolves slug in this order:
1. `--user-slug`
2. `BITBUCKET_USER_SLUG`
3. `BITBUCKET_USERNAME`
4. `BITBUCKET_USER`

## Codex runtime behavior
For this BBVA deployment, Codex agent runtimes should be treated as unable to execute `bbdc` against Bitbucket.

Typical failure signature:
- `Request failed: HTTPSConnectionPool(... NameResolutionError ... Failed to resolve ...)`

Recommended handling in the skill:
- Never execute `bbdc` in Codex.
- Always provide command-only guidance and ask the user to run commands locally.
- Continue once command output is provided by the user.

When user output includes `HTTP 401` on account endpoints:
- Explain that Project/Repository HTTP access tokens have narrower scope than PAT for user-account data.
- Treat this as expected token-scope behavior.

## Raw vs JSON responses
Some commands intentionally print raw text if the endpoint is non-JSON:
- `pr diff`
- `pr diff-file`
- `pr patch`

Most other commands return JSON objects/arrays.

## Special REST routes
Not all operations use `/api/latest`.

Implemented through `request_rest`:
- Reactions:
  - `comment-likes/latest/projects/.../reactions/...`
- Rebase:
  - `git/latest/projects/.../pull-requests/<id>/rebase`
- SSH keys:
  - `ssh/latest/keys`
- GPG keys:
  - `gpg/latest/keys`

These routes are built from `BITBUCKET_SERVER` directly (which already ends with `/rest`).

## Batch execution behavior
Batch commands are under `pr batch ...` and share a common executor:
- Input is a JSON list from `--file` (or stdin with `-`).
- `--project` and `--repo` act as defaults, merged into each item.
- `--defaults` supports extra default fields (JSON literal or `@path`).
- `--concurrency` controls worker pool size.
- `--continue-on-error` is enabled by default.
- `--json` emits an aggregate JSON payload with per-item outcomes.

## Error semantics
For HTTP errors (`status >= 400`), CLI attempts to extract:
- `errors[0].message`
- or `message`

Returned message format:
- `HTTP <status> for <METHOD> <url>: <detail>`

Network errors raise:
- `Request failed: <requests exception>`
