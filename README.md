# duckpandemic

The aim of this project is to contaminated the world with ducks. (and dev readme with ducks images)

This is a simple GitHub Action that will display duck image in your README.md file.

## Outputs

No outputs. The action will update the README.md file of the repository.

## Configuration

You need to have a `README.md` file in the root of your repository.

And you need to have the following balise in your `README.md` file:

```markdown
<!--DUCK-->
<!--/DUCK-->
```

⚠️**WARNING**⚠️ : this action need Read and write permissions (Settings > Actions > General)

## Example usage

```yaml
name : duck pandemic
on:
  push:
    branches:
      - main
jobs:
    build:
        runs-on: ubuntu-22.04
        steps:
        - uses: actions/checkout@v3
        - name: duck
          uses: tot0p/duckpandemic@v1
```

## Result

<!--DUCK-->
<!--/DUCK-->
