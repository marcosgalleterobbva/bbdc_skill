# bbdc CLI Command Inventory

Source: `/Users/O000142/Projects/bb-cli/bbdc_cli/__main__.py`

`*` marks required option/argument.

| Group | Command | Function | Parameters |
|---|---|---|---|
| pr | `pr activities` | `pr_activities` | `--project/-p*, --repo/-r*, <pr_id>*, --from-id, --from-type, --limit, --max-items, --json` |
| pr | `pr approve` | `pr_approve` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr changes` | `pr_changes` | `--project/-p*, --repo/-r*, <pr_id>*, --change-scope, --since-id, --until-id, --with-comments/--no-with-comments, --limit, --max-items, --json` |
| pr | `pr comment` | `pr_comment` | `--project/-p*, --repo/-r*, <pr_id>*, --text/-t*` |
| pr | `pr commit-message` | `pr_commit_message` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr commits` | `pr_commits` | `--project/-p*, --repo/-r*, <pr_id>*, --with-counts/--no-with-counts, --avatar-size, --avatar-scheme, --limit, --max-items, --json` |
| pr | `pr create` | `pr_create` | `--project/-p*, --repo/-r*, --from-branch*, --to-branch*, --title*, --description, --reviewer, --draft/--no-draft, --json` |
| pr | `pr decline` | `pr_decline` | `--project/-p*, --repo/-r*, <pr_id>*, --version, --comment, --json` |
| pr | `pr delete` | `pr_delete` | `--project/-p*, --repo/-r*, <pr_id>*, --version, --json` |
| pr | `pr diff` | `pr_diff` | `--project/-p*, --repo/-r*, <pr_id>*, --context-lines, --whitespace` |
| pr | `pr diff-file` | `pr_diff_file` | `--project/-p*, --repo/-r*, <pr_id>*, <file_path>*, --since-id, --until-id, --src-path, --diff-type, --context-lines, --whitespace, --with-comments/--no-with-comments, --avatar-size, --avatar-scheme` |
| pr | `pr diff-stats` | `pr_diff_stats` | `--project/-p*, --repo/-r*, <pr_id>*, <file_path>*, --since-id, --until-id, --src-path, --whitespace` |
| pr | `pr for-commit` | `pr_for_commit` | `--project/-p*, --repo/-r*, <commit_id>*, --limit, --max-items, --json` |
| pr | `pr get` | `pr_get` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr list` | `pr_list` | `--project/-p*, --repo/-r*, --state, --direction, --limit, --max-items, --json` |
| pr | `pr merge` | `pr_merge` | `--project/-p*, --repo/-r*, <pr_id>*, --version, --message, --strategy, --auto-merge/--no-auto-merge, --auto-subject, --json` |
| pr | `pr merge-base` | `pr_merge_base` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr merge-check` | `pr_merge_check` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr patch` | `pr_patch` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr rebase` | `pr_rebase` | `--project/-p*, --repo/-r*, <pr_id>*, --version, --json` |
| pr | `pr rebase-check` | `pr_rebase_check` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr reopen` | `pr_reopen` | `--project/-p*, --repo/-r*, <pr_id>*, --version, --json` |
| pr | `pr unapprove` | `pr_unapprove` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr unwatch` | `pr_unwatch` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr | `pr update` | `pr_update` | `--project/-p*, --repo/-r*, <pr_id>*, --version, --title, --description, --reviewer, --draft/--no-draft, --json` |
| pr | `pr watch` | `pr_watch` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr auto-merge | `pr auto-merge cancel` | `pr_auto_merge_cancel` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr auto-merge | `pr auto-merge get` | `pr_auto_merge_get` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr auto-merge | `pr auto-merge set` | `pr_auto_merge_set` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr blockers | `pr blockers add` | `pr_blockers_add` | `--project/-p*, --repo/-r*, <pr_id>*, --text/-t*, --json` |
| pr blockers | `pr blockers delete` | `pr_blockers_delete` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --version` |
| pr blockers | `pr blockers get` | `pr_blockers_get` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*` |
| pr blockers | `pr blockers list` | `pr_blockers_list` | `--project/-p*, --repo/-r*, <pr_id>*, --states, --count, --limit, --max-items, --json` |
| pr blockers | `pr blockers update` | `pr_blockers_update` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --text, --severity, --state, --version, --json` |
| pr comments | `pr comments add` | `pr_comments_add` | `--project/-p*, --repo/-r*, <pr_id>*, --text/-t*` |
| pr comments | `pr comments apply-suggestion` | `pr_comments_apply_suggestion` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --suggestion-index*, --comment-version, --pr-version, --commit-message, --json` |
| pr comments | `pr comments delete` | `pr_comments_delete` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --version` |
| pr comments | `pr comments get` | `pr_comments_get` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*` |
| pr comments | `pr comments list` | `pr_comments_list` | `--project/-p*, --repo/-r*, <pr_id>*, --path*, --from-hash, --to-hash, --diff-types, --states, --anchor-state, --limit, --max-items, --json` |
| pr comments | `pr comments react` | `pr_comments_react` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --emoticon*` |
| pr comments | `pr comments unreact` | `pr_comments_unreact` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --emoticon*` |
| pr comments | `pr comments update` | `pr_comments_update` | `--project/-p*, --repo/-r*, <pr_id>*, <comment_id>*, --text, --severity, --state, --version, --json` |
| pr participants | `pr participants add` | `pr_participants_add` | `--project/-p*, --repo/-r*, <pr_id>*, --user/-u*, --role, --json` |
| pr participants | `pr participants list` | `pr_participants_list` | `--project/-p*, --repo/-r*, <pr_id>*, --limit, --max-items, --json` |
| pr participants | `pr participants remove` | `pr_participants_remove` | `--project/-p*, --repo/-r*, <pr_id>*, <user>*` |
| pr participants | `pr participants search` | `pr_participants_search` | `--project/-p*, --repo/-r*, --filter, --role, --direction, --limit, --max-items, --json` |
| pr participants | `pr participants status` | `pr_participants_status` | `--project/-p*, --repo/-r*, <pr_id>*, <user>*, --status*, --last-reviewed-commit, --version, --json` |
| pr review | `pr review complete` | `pr_review_complete` | `--project/-p*, --repo/-r*, <pr_id>*, --comment, --last-reviewed-commit, --status, --json` |
| pr review | `pr review discard` | `pr_review_discard` | `--project/-p*, --repo/-r*, <pr_id>*` |
| pr review | `pr review get` | `pr_review_get` | `--project/-p*, --repo/-r*, <pr_id>*` |
| root | `doctor` | `doctor` | `` |
