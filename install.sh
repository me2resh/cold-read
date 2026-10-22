#!/usr/bin/env bash
# Install Cold Read into an agent's skills directory.
# Usage: ./install.sh [claude|codex|all|<directory>]
# Any agent that supports the Agent Skills format (a folder with SKILL.md) can use the same folder:
# point it at the folder, or copy the folder into that agent's skills directory.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-all}"
copy() { mkdir -p "$1"; rm -rf "$1/cold-read"; mkdir -p "$1/cold-read"; cp -R "$HERE/SKILL.md" "$HERE/references" "$HERE/examples" "$1/cold-read/"; echo "installed: $1/cold-read"; }
case "$TARGET" in
  claude) copy "$HOME/.claude/skills" ;;
  codex)  copy "$HOME/.codex/skills" ;;
  all)    copy "$HOME/.claude/skills"; copy "$HOME/.codex/skills" ;;
  *)      copy "$TARGET" ;;
esac
cat <<'MSG'
Cursor: copy .cursor/rules/cold-read.mdc into your project's .cursor/rules/ (or the whole folder into ~/.cursor/skills/ if your version supports skills).
Copilot: copy .github/copilot-instructions.md into your project, or append its text to yours.
Other agents: add the AGENTS.md text to your agent's instructions file and keep SKILL.md plus references/ where the agent can read them.
MSG
