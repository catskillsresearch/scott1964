# Vendored PalomarPolicy snapshot

Source: https://github.com/PalomarRegistry/PalomarPolicy
Commit: `4ed67de4fd69df383badb7857dff97e2fb734ab0`

This directory is a plain-file copy of the Palomar editorial contract
(prompts, rubric, CONTRIBUTING, classification guide, review schema).
It is **not** a git submodule.

## Sync

`scripts/palomar_policy_sync.py` checks upstream `main` before
editorial preflight and refreshes this tree when a newer commit exists.

## Revert a bad upstream pull

Before committing audit results:

```bash
git checkout -- vendor/palomar-policy vendor/PALOMAR_POLICY_PIN
```

Use `scripts/palomar_preflight.sh --no-policy-sync` to audit against the
currently committed snapshot without contacting upstream.
