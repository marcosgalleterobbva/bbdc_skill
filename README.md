# bbdc-cli Codex Skill

Codex skill for operating the `bbdc` Bitbucket Data Center CLI from natural-language requests.

## What teammates need
1. Install CLI:
   - `pipx install bbdc-cli` (recommended), or `pip install bbdc-cli`
2. Configure environment:
   - `BITBUCKET_SERVER` (must end with `/rest`)
   - `BITBUCKET_API_TOKEN`
   - Optional for account profile/settings commands: `BITBUCKET_USER_SLUG`

BBVA token note:
- Teams commonly use Project/Repository HTTP access tokens.
- Those tokens can return `401` for some user-account endpoints (`ssh-keys`, `gpg-keys`, `user`, `settings`).
3. Install this skill under local Codex skills directory as `bbdc-cli`.

## Recommended distribution model
- Keep this skill in its own git repo.
- Ask teammates to clone/copy it into `$CODEX_HOME/skills/bbdc-cli`.
- Release the CLI independently on PyPI (`bbdc-cli` package).

This keeps:
- command behavior/versioning in the PyPI package,
- natural-language routing and Codex-specific instructions in the skill repo.

## Keeping skill and CLI aligned
When commands change in `bbdc_cli/__main__.py`, refresh inventory:

```bash
python3 scripts/generate_command_inventory.py \
  --source <PATH_TO_BBDC_CLI_MAIN> \
  --output references/generated-command-inventory.md
```

Option guardrail:
- Validate flags against `references/generated-command-inventory.md` before suggesting commands.
- Do not suggest `account me --json`; `account me` already returns JSON and has no `--json` option.

## Validate setup
After install, from Codex ask:
- "Use bbdc-cli to list open PRs in project X repo Y."
- "Use bbdc-cli to show my authenticated account info."

Skill should return mapped commands such as `bbdc pr ...` or `bbdc account ...` for the user to run locally.

## Known Codex limitation
For this BBVA setup, assume Codex runtimes cannot execute `bbdc` reliably against Bitbucket due to network constraints.

Expected skill behavior:
1. Never execute `bbdc` in Codex.
2. Provide exact `bbdc` commands for the user to run in their terminal.
3. Continue once the user shares command output.
