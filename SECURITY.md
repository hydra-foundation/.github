# Security policy

## Reporting a vulnerability

Use GitHub's private vulnerability reporting, which is enabled on both
repositories that take reports:

- **[Report in `hydra`](https://github.com/hydra-foundation/hydra/security/advisories/new)**
  — for anything in a `hydrakit/*` package.
- **[Report in `app`](https://github.com/hydra-foundation/app/security/advisories/new)**
  — for the skeleton.

That opens a private advisory only you and I can read, and it keeps the whole
exchange in one place. If you would rather not use it, email
**william.hleucka@gmail.com** instead.

Either way, please do not open a public issue for a security problem.

Useful things to include, as far as you have them: the affected package and
version, what an attacker can do with it, and the smallest reproduction you can
manage.

This is a personal project maintained by one person, so treat any timeline as
best-effort. You will get an acknowledgement, and a fix will go out in the next
release once there is one.

## What is in scope

The packages published from this organization: `hydrakit/*` on Packagist, and
the `app` skeleton. The areas most worth your attention are the ones that
handle untrusted input or make decisions about identity:

| Package | Why it matters |
| --- | --- |
| `auth` | Authentication and the session-backed guard. |
| `authorization` | The gate that decides what an identity may do. |
| `csrf` | Synchronizer-token CSRF protection and its constant-time compare. |
| `session` | Session lifecycle, cookie handling, and regeneration. |
| `http` | Request parsing, routing, and the middleware pipeline. |
| `database` | Query construction and parameter binding. |
| `view` | Output escaping in templates. |

## What is not

The package repositories other than `app` are generated mirrors of the
monorepo. A finding about one of them is a finding about `hydra`; there is no
separate code to fix.

Reports that amount to "an application can configure this insecurely" are
usually documentation problems rather than vulnerabilities, but send them
anyway if the safe path is not the obvious one — a framework that makes the
insecure choice easy is a real defect.

## Supported versions

Pre-1.0 and experimental: only the latest release gets fixes. There are no
maintained branches behind it.
