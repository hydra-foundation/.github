<div align="center">

# Hydra Foundation

[![PHP](https://img.shields.io/badge/PHP-8.2%2B-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![PSR](https://img.shields.io/badge/PSR-3%20·%207%20·%2011%20·%2014%20·%2015%20·%2017-4F5B93)](https://www.php-fig.org/psr/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)

</div>

A collection of experimental PHP packages for my PHP framework, Hydra.


## Packages

| Package | Role |
| --- | --- |
| [**`core`**](https://github.com/hydra-foundation/core) | Application object, container and service-provider contracts, typed environment loading. Interfaces only. |
| [**`http`**](https://github.com/hydra-foundation/http) | PSR-7 / PSR-15 HTTP layer: request lifecycle, routing, middleware pipeline. |
| [**`nyholm`**](https://github.com/hydra-foundation/nyholm) | Nyholm PSR-7 / PSR-17 adapter — the default message and factory implementation. |
| [**`php-di`**](https://github.com/hydra-foundation/php-di) | PHP-DI PSR-11 adapter — the default container. |
| [**`kernel`**](https://github.com/hydra-foundation/kernel) | Default composition root and HTTP plumbing. |
| [**`session`**](https://github.com/hydra-foundation/session) | Session handling as PSR-15 middleware. |
| [**`database`**](https://github.com/hydra-foundation/database) | Thin PDO-based data layer. |
| [**`validation`**](https://github.com/hydra-foundation/validation) | Zero-dependency input validation. |
| [**`view`**](https://github.com/hydra-foundation/view) | Native PHP templating. |
| [**`log`**](https://github.com/hydra-foundation/log) | PSR-3 logger. |
| [**`event`**](https://github.com/hydra-foundation/event) | PSR-14 event dispatcher and listener provider. |
| [**`auth`**](https://github.com/hydra-foundation/auth) | Authentication over the HTTP and session packages. |
| [**`authorization`**](https://github.com/hydra-foundation/authorization) | Ability-based authorization on top of `auth`. |
| [**`csrf`**](https://github.com/hydra-foundation/csrf) | CSRF protection as middleware. |
| [**`console`**](https://github.com/hydra-foundation/console) | CLI surface, powered by Symfony Console. |
| [**`app`**](https://github.com/hydra-foundation/app) | Application skeleton — the composition root every project starts from. |

## Principles

- **PSR all the way down.** HTTP messages, containers, middleware, logging, events,
  and factories speak the [PHP-FIG](https://www.php-fig.org/) standards.
- **Contracts over concretes.** Packages depend on interfaces; the app binds the
  implementations. Swapping one out is a one-line change at the composition root.
