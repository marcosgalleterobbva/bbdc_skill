# bbdc CLI Command Inventory

Source: `bbdc_cli/__main__.py`

`*` marks required option/argument.

| Group | Command | Function | Parameters |
|---|---|---|---|
| account | `account gpg-keys` | `account_gpg_keys` | `--user, --limit, --max-items, --json` |
| account | `account me` | `account_me` | `--user-slug, --include-profile/--no-include-profile, --include-settings/--no-include-settings, --limit, --max-items` |
| account | `account recent-repos` | `account_recent_repos` | `--limit, --max-items, --json` |
| account | `account settings` | `account_settings` | `--user-slug` |
| account | `account ssh-keys` | `account_ssh_keys` | `--user, --limit, --max-items, --json` |
| account | `account user` | `account_user` | `--user-slug` |
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
| pr batch | `pr batch approve` | `pr_batch_approve` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch comment` | `pr_batch_comment` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch commit-message` | `pr_batch_commit_message` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch create` | `pr_batch_create` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch decline` | `pr_batch_decline` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch delete` | `pr_batch_delete` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch get` | `pr_batch_get` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch merge` | `pr_batch_merge` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch merge-base` | `pr_batch_merge_base` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch merge-check` | `pr_batch_merge_check` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch rebase` | `pr_batch_rebase` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch rebase-check` | `pr_batch_rebase_check` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch reopen` | `pr_batch_reopen` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch unapprove` | `pr_batch_unapprove` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch unwatch` | `pr_batch_unwatch` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch update` | `pr_batch_update` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch | `pr batch watch` | `pr_batch_watch` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch auto-merge | `pr batch auto-merge cancel` | `pr_batch_auto_merge_cancel` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch auto-merge | `pr batch auto-merge get` | `pr_batch_auto_merge_get` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch auto-merge | `pr batch auto-merge set` | `pr_batch_auto_merge_set` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch blockers | `pr batch blockers add` | `pr_batch_blockers_add` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch blockers | `pr batch blockers delete` | `pr_batch_blockers_delete` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch blockers | `pr batch blockers get` | `pr_batch_blockers_get` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch blockers | `pr batch blockers update` | `pr_batch_blockers_update` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments add` | `pr_batch_comments_add` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments apply-suggestion` | `pr_batch_comments_apply_suggestion` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments delete` | `pr_batch_comments_delete` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments get` | `pr_batch_comments_get` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments react` | `pr_batch_comments_react` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments unreact` | `pr_batch_comments_unreact` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch comments | `pr batch comments update` | `pr_batch_comments_update` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch participants | `pr batch participants add` | `pr_batch_participants_add` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch participants | `pr batch participants remove` | `pr_batch_participants_remove` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch participants | `pr batch participants status` | `pr_batch_participants_status` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch review | `pr batch review complete` | `pr_batch_review_complete` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch review | `pr batch review discard` | `pr_batch_review_discard` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
| pr batch review | `pr batch review get` | `pr_batch_review_get` | `--file/-f*, --project/-p, --repo/-r, --defaults, --concurrency/-c, --continue-on-error/--stop-on-error, --json` |
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
| root | `doctor` | `doctor` | `--json` |
