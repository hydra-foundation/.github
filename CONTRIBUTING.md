# Contributing

Development happens in one place:
**[hydra-foundation/hydra](https://github.com/hydra-foundation/hydra)**.

If you arrived here from a package repository — `core`, `http`, `session`, or
any of the other fourteen — that repository is **generated**. A split workflow
republishes each `packages/*` directory from the monorepo on every push and
every tag, which is what keeps `composer require hydrakit/*` working from
Packagist. Issues are disabled there, a pull request against one cannot be
merged, and a commit pushed directly to one is overwritten by the next split.
None of that is a judgement on the change; there is simply nowhere for it to
land. Open it against the monorepo instead.

`hydra-foundation/app`, the skeleton, is a real repository and takes changes
directly.

## Before you open a pull request

This is an experimental personal project. Breaking changes land between any two
versions, and the design is still moving, so an issue describing the problem is
usually a better first step than a patch — it avoids work that a pending
redesign would throw away.

## Working on the monorepo

```bash
git clone git@github.com:hydra-foundation/hydra.git
cd hydra
composer install
vendor/bin/phpunit --order-by=random
```

The suite runs every package in one process, so state leaking between packages
through `putenv()`, `$_ENV` or static properties is a real failure mode. That is
why the order is randomised; run it that way locally too, because CI will.

Before pushing:

```bash
composer qa        # phpstan, php-cs-fixer, phpunit
```

CI runs the suite on PHP 8.2 through 8.5, plus static analysis and style. All
four version jobs are required.

## Conventions

- **Packages depend on interfaces.** A package that needs a concrete vendor gets
  an adapter package of its own, the way `nyholm` and `php-di` fill the PSR-7
  and PSR-11 seams. Keep the dependency optional and the seam swappable.
- **Comments are sparse.** Say it in the name, the type, or the exception
  message. A comment earns its place by explaining something the code cannot.
- **Tests come with the change.** Each package has its own `tests/` directory
  and its own testsuite entry.
