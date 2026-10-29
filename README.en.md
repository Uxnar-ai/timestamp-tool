# ts — paste epoch numbers, get readable times

> Paste timestamps one per line from a log and get 「2026-10-30 06:08:00 Fri + UTC + 2 hours ago」. Works backwards too: give it a date and get seconds and milliseconds.

English | [中文](README.md)

## What it is

The annoying part of reading logs is `1793311291` — you cannot tell by eye whether that was minutes or months ago.

This page does exactly one thing: paste and find out. Each line is identified first. Pure digits are classified by length — 10 digits as seconds, 13 as milliseconds, 11 and 12 scaled accordingly, 15+ truncated to the first 13 (which covers microseconds and nanoseconds). Anything else is parsed as a date; both `2026-10-30 06:08:00` and ISO strings with `Z` work.

Every line reports local time with weekday, UTC, how long ago it was (2 hours ago / 3 days ago), and both the seconds and milliseconds forms. On the date side the hyphens are swapped for slashes and parsed again — that is to accommodate the older habit of writing `2026-10-30 06:08:00` as local time, which would otherwise be read as UTC and be off by eight hours.

The header shows a live 「now」 with copy buttons for seconds and milliseconds. The sample data is computed at load time, so it always reads 「2 hours ago / 5 minutes ago」 instead of a wall of 「12 months ago」.

## Features

- One per line, batch converted
- Detects 10-digit seconds, 13-digit ms, 11–12 digits, microseconds, nanoseconds
- Reverse conversion: date or ISO string to seconds and milliseconds
- Every line shows local time with weekday, UTC, and relative time
- Live 「now」 in the header with copy buttons for both units
- Unrecognised lines are flagged instead of silently skipped
- Auto light/dark plus manual toggle

## Stack

Python 3.12 · Flask 3.1 · 原生 JS

## Run

```bash
pip install -r requirements.txt
python app.py  # 默认 127.0.0.1:8890
```

## About

Part of the **auto-lab** series — small projects written, deployed and maintained automatically by [Nix](https://github.com/Uxnar-ai) on a self-hosted server.

Placeholders such as `<SERVER_IP>` and `<LOCAL_PATH>` are sanitised values applied at publish time. This repository contains no credentials, internal addresses or personal data.

## License

MIT
