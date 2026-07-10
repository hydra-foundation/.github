<div align="center">

# Hydra Foundation

**A modular PHP framework built on PSR contracts — small packages, sharp boundaries, no magic.**

[![PHP](https://img.shields.io/badge/PHP-8.2%2B-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![PSR](https://img.shields.io/badge/PSR-3%20·%207%20·%2011%20·%2014%20·%2015%20·%2017-4F5B93)](https://www.php-fig.org/psr/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)

</div>

---

Hydra is a PHP framework assembled from independent, single-purpose packages. Each
codes against an interface rather than its neighbours, and the split between
**framework mechanism** and **application policy** is deliberate: the core defines
contracts, the packages supply mechanism, and your app wires them together at the
composition root.

## Packages

The dependency graph flows downward — `core` knows nothing of the layers above it.

| Package | Role |
| --- | --- |
| [**`hydrakit/core`**](https://github.com/hydra-foundation/core) | Application object, container and service-provider contracts, typed environment loading. Interfaces only. |
| [**`hydrakit/http`**](https://github.com/hydra-foundation/http) | PSR-7 / PSR-15 HTTP layer: request lifecycle, routing, middleware pipeline. |
| [**`hydrakit/nyholm`**](https://github.com/hydra-foundation/nyholm) | Nyholm PSR-7 / PSR-17 adapter — the default message and factory implementation. |
| [**`hydrakit/php-di`**](https://github.com/hydra-foundation/php-di) | PHP-DI PSR-11 adapter — the default container. |
| [**`hydrakit/kernel`**](https://github.com/hydra-foundation/kernel) | Default composition root and HTTP plumbing. |
| [**`hydrakit/session`**](https://github.com/hydra-foundation/session) | Session handling as PSR-15 middleware. |
| [**`hydrakit/database`**](https://github.com/hydra-foundation/database) | Thin PDO-based data layer. |
| [**`hydrakit/validation`**](https://github.com/hydra-foundation/validation) | Zero-dependency input validation. |
| [**`hydrakit/view`**](https://github.com/hydra-foundation/view) | Native PHP templating. |
| [**`hydrakit/log`**](https://github.com/hydra-foundation/log) | PSR-3 logger. |
| [**`hydrakit/event`**](https://github.com/hydra-foundation/event) | PSR-14 event dispatcher and listener provider. |
| [**`hydrakit/auth`**](https://github.com/hydra-foundation/auth) | Authentication over the HTTP and session packages. |
| [**`hydrakit/authorization`**](https://github.com/hydra-foundation/authorization) | Ability-based authorization on top of `auth`. |
| [**`hydrakit/csrf`**](https://github.com/hydra-foundation/csrf) | CSRF protection as middleware. |
| [**`hydrakit/console`**](https://github.com/hydra-foundation/console) | CLI surface, powered by Symfony Console. |
| [**`hydrakit/app`**](https://github.com/hydra-foundation/app) | Application skeleton — the composition root every project starts from. |

## Principles

- **PSR all the way down.** HTTP messages, containers, middleware, logging, events,
  and factories speak the [PHP-FIG](https://www.php-fig.org/) standards.
- **Contracts over concretes.** Packages depend on interfaces; the app binds the
  implementations. Swapping one out is a one-line change at the composition root.
- **Mechanism vs. policy.** The framework provides the *how*; your application owns
  the *what*.
- **Explicit beats implicit.** No facades, no auto-discovery. If a service is
  available, you can point to the line that bound it.
