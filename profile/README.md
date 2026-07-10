<div align="center">

# Hydra Foundation

**A modular PHP framework built on PSR contracts — small packages, sharp boundaries, no magic.**

[![PHP](https://img.shields.io/badge/PHP-8.2%2B-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![PSR](https://img.shields.io/badge/PSR-3%20·%207%20·%2011%20·%2014%20·%2015%20·%2017-4F5B93)](https://www.php-fig.org/psr/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)

</div>

---

Hydra is a PHP framework assembled from independent packages. Each one does a single
job, depends on as little as possible, and codes against an interface rather than its
neighbours. The split between **framework mechanism** and **application policy** is
deliberate: the core defines contracts and orchestration, the packages supply the
mechanism, and your app wires them together at the composition root.

## Packages

The dependency graph flows downward — `core` knows nothing of the layers above it.

| Package | Role |
| --- | --- |
| [**`hydrakit/core`**](https://github.com/hydra-foundation/core) | The foundation: application object, container & service-provider contracts, typed environment loading. Defines interfaces only — concretes are bound by the app. |
| [**`hydrakit/http`**](https://github.com/hydra-foundation/http) | PSR-7 / PSR-15 HTTP layer — request lifecycle, routing, and the middleware pipeline. |
| [**`hydrakit/nyholm`**](https://github.com/hydra-foundation/nyholm) | Nyholm PSR-7 / PSR-17 adapter — the default message and factory implementation. |
| [**`hydrakit/php-di`**](https://github.com/hydra-foundation/php-di) | PHP-DI PSR-11 adapter — the default container binding `core`'s contracts. |
| [**`hydrakit/kernel`**](https://github.com/hydra-foundation/kernel) | Default composition root and HTTP plumbing — the framework-side wiring `app` builds on. |
| [**`hydrakit/session`**](https://github.com/hydra-foundation/session) | Session handling exposed through PSR-15 middleware. |
| [**`hydrakit/database`**](https://github.com/hydra-foundation/database) | A thin PDO-based data layer. |
| [**`hydrakit/validation`**](https://github.com/hydra-foundation/validation) | Zero-dependency input validation. |
| [**`hydrakit/view`**](https://github.com/hydra-foundation/view) | Native PHP templating — no compile step, no new syntax. |
| [**`hydrakit/log`**](https://github.com/hydra-foundation/log) | A PSR-3 logger. |
| [**`hydrakit/event`**](https://github.com/hydra-foundation/event) | A PSR-14 event dispatcher and listener provider. |
| [**`hydrakit/auth`**](https://github.com/hydra-foundation/auth) | Authentication, built on the HTTP and session packages. |
| [**`hydrakit/authorization`**](https://github.com/hydra-foundation/authorization) | Ability-based authorization on top of `auth`. |
| [**`hydrakit/csrf`**](https://github.com/hydra-foundation/csrf) | CSRF protection delivered as middleware. |
| [**`hydrakit/console`**](https://github.com/hydra-foundation/console) | The CLI surface, powered by Symfony Console. |
| [**`hydrakit/app`**](https://github.com/hydra-foundation/app) | The application skeleton — the composition root every Hydra project starts from. |

## Principles

- **PSR all the way down.** Containers, HTTP messages, middleware, logging, and factories
  speak the [PHP-FIG](https://www.php-fig.org/) standards, so packages compose with the
  wider ecosystem and with each other.
- **Contracts over concretes.** Packages depend on interfaces. The app binds the
  implementations. Swapping one out is a one-line change at the composition root.
- **Mechanism vs. policy.** The framework provides the *how*; your application owns the
  *what*. The two never bleed into each other.
- **Explicit beats implicit.** No facades, no auto-discovery surprises. If a service is
  available, you can point to the line that bound it.

## Getting started

Every project begins from the [`hydrakit/app`](https://github.com/hydra-foundation/app) skeleton:

```bash
cp .env.example .env             # defaults run as-is for local dev
composer install                 # resolves the framework packages
php bin/console key:generate     # writes a fresh APP_KEY

composer start                   # serve at http://localhost:8000
```

Open **http://localhost:8000** and you'll see *Welcome to Hydra*. A full Docker stack
(PHP-FPM, nginx, MariaDB, Redis) is available too — see the app README.

## Requirements

- **PHP 8.2+**
- **Composer**
- Optional: **Docker** + Compose for the full local stack
