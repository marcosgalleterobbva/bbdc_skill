# bbdc-cli Codex Skill

Codex skill for operating the `bbdc` Bitbucket Data Center CLI from natural-language requests.

## What teammates need
1. Install CLI:
   - `pipx install bbdc-cli` (recommended), or `pip install bbdc-cli`
2. Configure environment:
   - `BITBUCKET_SERVER` (must end with `/rest`)
   - `BITBUCKET_API_TOKEN`
   - Optional for account profile/settings commands: `BITBUCKET_USER_SLUG`
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

## Validate setup
After install, from Codex ask:
- "Use bbdc-cli to list open PRs in project X repo Y."
- "Use bbdc-cli to show my authenticated account info."

Skill should run:
- `bbdc doctor`
- followed by mapped commands such as `bbdc pr ...` or `bbdc account ...`.
