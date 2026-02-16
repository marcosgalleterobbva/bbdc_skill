# bbdc Source Behavior Notes

## Table of Contents
- [Core assumptions](#core-assumptions)
- [Validation and enums](#validation-and-enums)
- [Auto-version behavior](#auto-version-behavior)
- [Pagination behavior](#pagination-behavior)
- [Raw vs JSON responses](#raw-vs-json-responses)
- [Special REST routes](#special-rest-routes)
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

These routes are built from `BITBUCKET_SERVER` directly (which already ends with `/rest`).

## Error semantics
For HTTP errors (`status >= 400`), CLI attempts to extract:
- `errors[0].message`
- or `message`

Returned message format:
- `HTTP <status> for <METHOD> <url>: <detail>`

Network errors raise:
- `Request failed: <requests exception>`
