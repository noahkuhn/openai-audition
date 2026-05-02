#!/usr/bin/env python3
"""Export a Codex Desktop session JSONL into a markdown transcript."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture a Codex Desktop JSONL session as markdown."
    )
    parser.add_argument(
        "--source",
        type=Path,
        help="Explicit rollout JSONL file. Defaults to latest session for cwd.",
    )
    parser.add_argument(
        "--latest-cwd",
        type=Path,
        default=Path.cwd(),
        help="Find the newest Codex session whose session_meta cwd matches this path.",
    )
    parser.add_argument(
        "--sessions-root",
        type=Path,
        default=Path.home() / ".codex" / "sessions",
        help="Codex sessions root. Defaults to ~/.codex/sessions.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        help="Output directory. Defaults to source-material/private/codex-sessions or evidence/transcripts.",
    )
    parser.add_argument(
        "--public",
        action="store_true",
        help="Write to evidence/transcripts instead of private source material.",
    )
    parser.add_argument(
        "--include-tools",
        action="store_true",
        help="Include summarized tool calls. Tool outputs are still omitted.",
    )
    return parser.parse_args()


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def read_session_meta(path: Path) -> dict[str, Any]:
    for item in iter_jsonl(path):
        if item.get("type") == "session_meta":
            payload = item.get("payload")
            if isinstance(payload, dict):
                return payload
    return {}


def normalize_path(path: Path | str | None) -> str:
    if path is None:
        return ""
    try:
        return str(Path(path).expanduser().resolve())
    except OSError:
        return str(Path(path).expanduser())


def find_latest_session(sessions_root: Path, cwd: Path) -> tuple[Path, dict[str, Any]]:
    wanted_cwd = normalize_path(cwd)
    candidates = sorted(
        sessions_root.glob("**/rollout-*.jsonl"),
        key=lambda item: item.stat().st_mtime,
        reverse=True,
    )
    for candidate in candidates:
        meta = read_session_meta(candidate)
        if normalize_path(meta.get("cwd")) == wanted_cwd:
            return candidate, meta
    raise SystemExit(f"No Codex session found for cwd: {wanted_cwd}")


def content_to_text(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()
    if not isinstance(content, list):
        return ""

    parts: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        text = item.get("text")
        if isinstance(text, str):
            parts.append(text.strip())
    return "\n\n".join(part for part in parts if part).strip()


def function_call_summary(payload: dict[str, Any]) -> str:
    name = payload.get("name", "tool")
    arguments = payload.get("arguments")
    details = ""
    if isinstance(arguments, str):
        try:
            parsed = json.loads(arguments)
            if isinstance(parsed, dict):
                cmd = parsed.get("cmd")
                if isinstance(cmd, str):
                    details = f": `{cmd}`"
                elif parsed:
                    details = f": `{json.dumps(parsed, sort_keys=True)[:240]}`"
        except json.JSONDecodeError:
            details = f": `{arguments[:240]}`"
    return f"Tool call: `{name}`{details}"


def extract_events(path: Path, include_tools: bool) -> list[tuple[str, str]]:
    events: list[tuple[str, str]] = []
    for item in iter_jsonl(path):
        if item.get("type") != "response_item":
            continue
        payload = item.get("payload")
        if not isinstance(payload, dict):
            continue

        payload_type = payload.get("type")
        if payload_type == "message":
            role = str(payload.get("role", "message")).title()
            text = content_to_text(payload.get("content"))
            if text:
                events.append((role, text))
        elif include_tools and payload_type == "function_call":
            events.append(("Tool", function_call_summary(payload)))
    return events


def output_name(meta: dict[str, Any], source: Path) -> str:
    timestamp = str(meta.get("timestamp") or source.stem.replace("rollout-", ""))
    date_part = timestamp[:10] if len(timestamp) >= 10 else "unknown-date"
    time_part = ""
    if "T" in timestamp:
        time_part = timestamp.split("T", 1)[1][:5].replace(":", "")
    session_id = str(meta.get("id") or source.stem.split("-")[-1])[:8]
    bits = ["codex-session", date_part]
    if time_part:
        bits.append(time_part)
    bits.append(session_id)
    return "-".join(bits) + ".md"


def render_markdown(
    source: Path,
    meta: dict[str, Any],
    events: list[tuple[str, str]],
    public: bool,
) -> str:
    session_id = meta.get("id", "unknown")
    timestamp = meta.get("timestamp", "unknown")
    cwd = meta.get("cwd", "unknown")
    visibility = "public draft" if public else "private raw export"

    lines = [
        f"# Codex Session {timestamp}",
        "",
        f"- Session ID: `{session_id}`",
        f"- CWD: `{cwd}`",
        f"- Source: `{source}`",
        f"- Visibility: `{visibility}`",
        "",
        "Review before publishing. Remove secrets, private context, noisy tool output, and irrelevant system material.",
        "",
        "## Transcript",
        "",
    ]

    for role, text in events:
        lines.append(f"### {role}")
        lines.append("")
        lines.append(text)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    if args.source:
        source = args.source.expanduser().resolve()
        meta = read_session_meta(source)
    else:
        source, meta = find_latest_session(args.sessions_root.expanduser(), args.latest_cwd)

    out_dir = args.out_dir
    if out_dir is None:
        out_dir = Path(
            "evidence/transcripts"
            if args.public
            else "source-material/private/codex-sessions"
        )
    out_dir.mkdir(parents=True, exist_ok=True)

    events = extract_events(source, include_tools=args.include_tools)
    if not events:
        raise SystemExit(f"No message events found in {source}")

    out_path = out_dir / output_name(meta, source)
    out_path.write_text(
        render_markdown(source, meta, events, public=args.public),
        encoding="utf-8",
    )
    print(out_path)


if __name__ == "__main__":
    main()
