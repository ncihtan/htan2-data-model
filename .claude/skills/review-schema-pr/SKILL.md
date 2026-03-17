---
name: review-schema-pr
description: Review a PR that modifies LinkML schema YAML files. Use when reviewing pull requests to this repo.
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Agent
context: fork
argument-hint: [pr-number]
---

# HTAN Schema PR Review

The full review checklist and severity labels are in `CLAUDE.md` (the "PR Review"
section) — that file is always in context, so the rules are already loaded.
Apply them directly. Do not invent additional categories or labels.
