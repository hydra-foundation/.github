<div align="center">

# Hydra Foundation

**A modular PHP framework built on PSR contracts — small packages, sharp boundaries, no magic.**

[![PHP](https://img.shields.io/badge/PHP-8.2%2B-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![PSR](https://img.shields.io/badge/PSR-3%20·%207%20·%2011%20·%2015%20·%2017-4F5B93)](https://www.php-fig.org/psr/)
[![License](https://img.shields.io/badge/license-MIT-blue)](#)

</div>

---

Hydra is a PHP framework assembled from independent packages. Each one does a single
job, depends on as little as possible, and codes against an interface rather than its
neighbours. The split between **framework mechanism** and **application policy** is
deliberate: the core defines contracts and orchestration, the packages supply the
mechanism, and your app wires them together at the composition root.

Nothing is hidden. There is no global state to reach for, no service that materializes
by convention. Everything is bound explicitly into a PSR-11 container and resolved from
there.

## Packages

The dependency graph flows downward — `core` knows nothing of the layers above it.

| Package | Role |
| --- | --- |
| [**`hydra/core`**](https://github.com/hydra-foundation/core) | The foundation: application object, container & service-provider contracts, typed environment loading. Defines interfaces only — concretes are bound by the app. |
| [**`hydra/http`**](https://github.com/hydra-foundation/http) | PSR-7 / PSR-15 HTTP layer — request lifecycle, routing, and the middleware pipeline. |
| [**`hydra/session`**](https://github.com/hydra-foundation/session) | Session handling exposed through PSR-15 middleware. |
| [**`hydra/database`**](https://github.com/hydra-foundation/database) | A thin PDO-based data layer. |
| [**`hydra/kernel`**](https://github.com/hydra-foundation/kernel) | Default composition root and HTTP plumbing. |
| [**`hydra/validation`**](https://github.com/hydra-foundation/validation) | Zero-dependency input validation. |
| [**`hydra/view`**](https://github.com/hydra-foundation/view) | Native PHP templating — no compile step, no new syntax. |
| [**`hydra/event`**](https://github.com/hydra-foundation/event) | A PSR-14 event dispatcher. |
| [**`hydra/log`**](https://github.com/hydra-foundation/log) | A PSR-3 logger. |
| [**`hydra/auth`**](https://github.com/hydra-foundation/auth) | Authentication, built on the HTTP and session packages. |
| [**`hydra/authorization`**](https://github.com/hydra-foundation/authorization) | Ability-based authorization on top of `auth`. |
| [**`hydra/csrf`**](https://github.com/hydra-foundation/csrf) | CSRF protection delivered as middleware. |
| [**`hydra/console`**](https://github.com/hydra-foundation/console) | The CLI surface, powered by Symfony Console. |
| [**`hydra/app`**](https://github.com/hydra-foundation/app) | The application skeleton — the composition root every Hydra project starts from. |

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

Every project begins from the [`hydra/app`](https://github.com/hydra-foundation/app) skeleton:

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

---

<div align="center">
<sub>Built with PHP. No magic — just contracts.</sub>
</div>
