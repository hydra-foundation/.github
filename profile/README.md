<div align="center">

# Hydra

[![Tests](https://github.com/hydra-foundation/hydra/actions/workflows/tests.yml/badge.svg)](https://github.com/hydra-foundation/hydra/actions/workflows/tests.yml)
[![Split](https://github.com/hydra-foundation/hydra/actions/workflows/split.yml/badge.svg)](https://github.com/hydra-foundation/hydra/actions/workflows/split.yml)
[![Latest release](https://img.shields.io/packagist/v/hydrakit/app?label=release)](https://packagist.org/packages/hydrakit/app)

[![PHP](https://img.shields.io/badge/PHP-8.2%2B-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![PSR](https://img.shields.io/badge/PSR-3%20·%207%20·%2011%20·%2014%20·%2015%20·%2017-4F5B93)](https://www.php-fig.org/psr/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)

</div>

A collection of experimental PHP packages that form the foundation of my PHP
framework, Hydra.

> **Experimental.** A personal project, built in the open for my own use.
> Breaking changes are expected between any two versions, without notice.

## Start here

```bash
composer create-project hydrakit/app my-app
```

That is the skeleton, with every `hydrakit/*` package resolved from Packagist.
To work on the framework itself rather than with it, clone the monorepo below.

## Where the code lives

**[`hydra`](https://github.com/hydra-foundation/hydra)** is the development
monorepo: every package's source, one test suite, one release. It is where
issues and pull requests belong.

The sixteen package repositories in this organization are **generated**. A
split workflow republishes each `packages/*` directory to its own repository on
every push and every tag, which is what keeps `composer require hydrakit/http`
working from Packagist. They are outputs: issues are disabled, a pull request
against one cannot be merged, and a direct push is overwritten by the next
split.

**[`app`](https://github.com/hydra-foundation/app)** is the exception. It is a
real repository, not a mirror, and is developed there.

## Packages

Each links into the monorepo, where that package's source lives. Install any of
them with `composer require hydrakit/<name>`.

<!-- packages:start -->
| Package | Role |
| --- | --- |
| [**`core`**](https://github.com/hydra-foundation/hydra/tree/main/packages/core) | Application object, container and service-provider contracts, and typed environment loading. Interfaces only. |
| [**`http`**](https://github.com/hydra-foundation/hydra/tree/main/packages/http) | PSR-7/PSR-15 HTTP layer: request lifecycle, routing, and middleware pipeline. |
| [**`nyholm`**](https://github.com/hydra-foundation/hydra/tree/main/packages/nyholm) | Nyholm PSR-7/PSR-17 adapter: the default message and factory implementation for Hydra. |
| [**`php-di`**](https://github.com/hydra-foundation/hydra/tree/main/packages/php-di) | PHP-DI PSR-11 adapter: the default container for Hydra. |
| [**`kernel`**](https://github.com/hydra-foundation/hydra/tree/main/packages/kernel) | Hydra's default composition root and HTTP plumbing, kept in one place instead of copied per app. |
| [**`session`**](https://github.com/hydra-foundation/hydra/tree/main/packages/session) | Session handling as PSR-15 middleware, behind split data and lifecycle interfaces. |
| [**`database`**](https://github.com/hydra-foundation/hydra/tree/main/packages/database) | A thin PDO data-access seam and a raw-SQL migration runner. |
| [**`validation`**](https://github.com/hydra-foundation/hydra/tree/main/packages/validation) | Zero-dependency input validation: per-field rules, stateless, shareable. |
| [**`view`**](https://github.com/hydra-foundation/hydra/tree/main/packages/view) | Native PHP templating with template inheritance and escape-by-convention safety. No compile step. |
| [**`log`**](https://github.com/hydra-foundation/hydra/tree/main/packages/log) | A minimal PSR-3 logger that writes one plain-text line per record to a stream. |
| [**`event`**](https://github.com/hydra-foundation/hydra/tree/main/packages/event) | A minimal PSR-14 event dispatcher and listener provider. |
| [**`auth`**](https://github.com/hydra-foundation/hydra/tree/main/packages/auth) | Authentication for Hydra: identity only, behind a swappable guard. |
| [**`authorization`**](https://github.com/hydra-foundation/hydra/tree/main/packages/authorization) | Ability-based authorization for Hydra, on top of hydrakit/auth. |
| [**`csrf`**](https://github.com/hydra-foundation/hydra/tree/main/packages/csrf) | Synchronizer-token CSRF protection as PSR-15 middleware. |
| [**`console`**](https://github.com/hydra-foundation/hydra/tree/main/packages/console) | The generic console commands every Hydra app needs, powered by Symfony Console. |
| [**`admin`**](https://github.com/hydra-foundation/hydra/tree/main/packages/admin) | A composable admin backend for Hydra apps: declare a module, get routes and htmx screens. |
| [**`app`**](https://github.com/hydra-foundation/app) | The application skeleton every Hydra project starts from. |
<!-- packages:end -->

## Principles

- **PSR all the way down.** HTTP messages, containers, middleware, logging, events,
  and factories speak the [PHP-FIG](https://www.php-fig.org/) standards.
- **Contracts over concretes.** Packages depend on interfaces; the app binds the
  implementations. Swapping one out is a one-line change at the composition root.
- **One package, one job.** A package that needs a concrete vendor gets an adapter
  of its own, so the seam stays swappable and the dependency stays optional.
