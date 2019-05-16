# format-sql mirror

This project is a mirror of [format-sql](https://github.com/paetzke/format-sql) for [pre-commit](https://github.com/pre-commit/pre-commit)

## Using format-sql with pre-commit

Install format-sql

```sh
pip install format-sql
```

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
- repo: https://github.com/tchoedak/pre-commit-sql-format
  rev: v0.0.1
  hooks:
    - id: format-sql
```
