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

and add the md in your README.md file

```markdown
[Change the duck](https://github.com/username/projetname/issues/new?title=%F0%9F%A6%86%20Quack)
```

for the visitor can change the duck 🦆

for example:

```markdown
<div align="center">
<!--DUCK-->
<!--/DUCK-->

Submit the issue to change the duck

> :warning: The duck will be changed only if the title is `🦆 Quack` :warning:


[Change the duck](https://github.com/username/projetname/issues/new?title=%F0%9F%A6%86%20Quack)

</div>
```

> the perfect markdown for the duck 🦆

⚠️**WARNING**⚠️ : this action need Read and write permissions (Settings > Actions > General) and for initial setup you need to create a issue with the title `🦆 Quack` to init the duck

## Example usage

```yaml
name : duck pandemic
on:
  issues:
    types: [opened]
jobs:
    duck:
        runs-on: ubuntu-22.04
        steps:
        - uses: actions/checkout@v3
        - name: duck
          uses: tot0p/duckpandemic@v1.1.0
```

## Result
<div align="center">

<!--DUCK-->
### Duck changed by [cheikhhhhh](https://github.com/cheikhhhhh)
[![Duck](https://random-d.uk/api/69.jpg)](https://github.com/tot0p/duckpandemic/issues/new?title=%F0%9F%A6%86%20Quack)
<!--/DUCK-->

Submit the issue to change the duck

> :warning: The duck will be changed only if the title is `🦆 Quack` :warning:


[Change the duck](https://github.com/tot0p/duckpandemic/issues/new?title=%F0%9F%A6%86%20Quack)

</div>