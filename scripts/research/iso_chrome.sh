#!/usr/bin/env bash
# iso_chrome.sh - the ONLY sanctioned launcher for agent-driven Chrome work.
#
# Focus-safe by construction: headless "new" mode creates no window and
# cannot take or steal focus. The one visible exception is the `login`
# ceremony, gated behind an explicit human-set ack latch so no agent can
# trigger it on its own. See
# docs/superpowers/plans/2026-07-10-focus-safe-browser.md and
# docs/archive-recovery-runbook.md for the full design and rationale.
#
# Usage: iso_chrome.sh <headless|login|stop|status> [--profile NAME] [--dry-run]
#
# Banned launch modes, and why (never reintroduce these):
#   - `open -a "Google Chrome" ...`   routes to the user's own running Chrome.
#   - a headful binary exec           can self-activate asynchronously; a
#     (backgrounded)                  before/after focus check has a race
#                                      and proves nothing.
#   - a headful Chrome left running   an unattended login page can grab
#     unattended                      focus later, with nobody watching.
set -euo pipefail

CHROME_BIN="${ISO_CHROME_BIN:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
PROFILE_ROOT="${ISO_CHROME_PROFILE_ROOT:-$HOME/.cache/sf-election-iso}"
PORT_START="${ISO_CHROME_PORT_START:-9230}"
PORT_END="${ISO_CHROME_PORT_END:-9250}"
# The runbook's known docref (see session_probe.js) - going through ezproxy
# to a real resource is what triggers the SFPL login flow when unauthenticated.
LOGIN_URL="${ISO_CHROME_LOGIN_URL:-https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/0EB4F969E1C867F6}"

usage() {
  echo "usage: iso_chrome.sh <headless|login|stop|status> [--profile NAME] [--dry-run]" >&2
}

CMD="${1:-}"
if [[ $# -gt 0 ]]; then
  shift
fi

PROFILE_NAME="default"
DRY_RUN=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile)
      if [[ $# -lt 2 ]]; then
        echo "--profile requires a value" >&2
        exit 1
      fi
      PROFILE_NAME="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

PROFILE_DIR="$PROFILE_ROOT/$PROFILE_NAME"
PID_FILE="$PROFILE_DIR/.iso_chrome.pid"
PORT_FILE="$PROFILE_DIR/.iso_chrome.port"

# Matches only Chrome processes launched against THIS profile's
# --user-data-dir, so stop/status/lock-checks never touch anyone else's
# Chrome (including the user's own running browser).
profile_pids() {
  pgrep -f -- "user-data-dir=${PROFILE_DIR}(\$| )" 2>/dev/null || true
}

profile_locked() {
  [[ -n "$(profile_pids)" ]]
}

free_port() {
  local p
  for ((p = PORT_START; p <= PORT_END; p++)); do
    if ! lsof -nP -iTCP:"$p" -sTCP:LISTEN >/dev/null 2>&1; then
      echo "$p"
      return 0
    fi
  done
  return 1
}

wait_for_port() {
  local port="$1" tries=50
  while (( tries-- > 0 )); do
    if curl -s -o /dev/null "http://127.0.0.1:$port/json/version"; then
      return 0
    fi
    sleep 0.3
  done
  return 1
}

headless_cmd_str() {
  local port="$1"
  printf '%s' "\"$CHROME_BIN\" --headless=new --remote-debugging-port=$port --user-data-dir=\"$PROFILE_DIR\" --no-first-run --no-default-browser-check --disable-background-timer-throttling --disable-renderer-backgrounding --disable-backgrounding-occluded-windows"
}

cmd_headless() {
  if (( DRY_RUN )); then
    headless_cmd_str "$PORT_START"
    echo
    exit 0
  fi

  mkdir -p "$PROFILE_DIR"

  if profile_locked; then
    echo "refusing: profile '$PROFILE_NAME' is locked by another instance (pid $(profile_pids))" >&2
    exit 1
  fi

  local port
  port="$(free_port)" || { echo "no free port in $PORT_START-$PORT_END" >&2; exit 1; }

  nohup "$CHROME_BIN" --headless=new --remote-debugging-port="$port" \
    --user-data-dir="$PROFILE_DIR" --no-first-run --no-default-browser-check \
    --disable-background-timer-throttling --disable-renderer-backgrounding \
    --disable-backgrounding-occluded-windows \
    > "$PROFILE_DIR/.iso_chrome.log" 2>&1 &
  local pid=$!
  disown "$pid" 2>/dev/null || true
  echo "$pid" > "$PID_FILE"
  echo "$port" > "$PORT_FILE"

  if ! wait_for_port "$port"; then
    echo "chrome did not answer on debug port $port within timeout" >&2
    exit 1
  fi

  echo "http://127.0.0.1:$port"
}

cmd_login() {
  if [[ "${ISO_CHROME_LOGIN_ACK:-}" != "yes" ]]; then
    echo "refusing: login is the one visible-window ceremony and requires an explicit human go. Set ISO_CHROME_LOGIN_ACK=yes for exactly this single invocation (an agent may not set this latch itself; only the controller may, on the user's word)." >&2
    exit 1
  fi

  mkdir -p "$PROFILE_DIR"

  if profile_locked; then
    echo "refusing: profile '$PROFILE_NAME' is locked by another instance (pid $(profile_pids)); run 'stop' first" >&2
    exit 1
  fi

  echo "launching visible Chrome for the login ceremony on profile '$PROFILE_NAME'..." >&2
  echo "log in, then run: iso_chrome.sh stop --profile $PROFILE_NAME" >&2

  # Direct binary exec (never `open -a`), in the foreground of THIS
  # invocation only - the human runs or approves this single call, and the
  # window goes away the moment they close it or run `stop`.
  exec "$CHROME_BIN" --user-data-dir="$PROFILE_DIR" --no-first-run --no-default-browser-check "$LOGIN_URL"
}

cmd_stop() {
  local pids
  pids="$(profile_pids)"
  if [[ -z "$pids" ]]; then
    echo "no instance running on profile '$PROFILE_NAME'"
    rm -f "$PID_FILE" "$PORT_FILE"
    exit 0
  fi

  kill $pids 2>/dev/null || true
  sleep 0.5
  pids="$(profile_pids)"
  if [[ -n "$pids" ]]; then
    kill -9 $pids 2>/dev/null || true
  fi

  rm -f "$PID_FILE" "$PORT_FILE"
  echo "stopped profile '$PROFILE_NAME'"
}

cmd_status() {
  if profile_locked; then
    echo "profile '$PROFILE_NAME': locked (pid $(profile_pids))"
  else
    echo "profile '$PROFILE_NAME': unlocked"
  fi

  if [[ -f "$PORT_FILE" ]]; then
    local port
    port="$(cat "$PORT_FILE")"
    if curl -s -o /dev/null "http://127.0.0.1:$port/json/version"; then
      echo "debug port $port: answering"
    else
      echo "debug port $port: not answering"
    fi
  else
    echo "debug port: none recorded"
  fi
}

case "$CMD" in
  headless) cmd_headless ;;
  login) cmd_login ;;
  stop) cmd_stop ;;
  status) cmd_status ;;
  "")
    usage
    exit 1
    ;;
  *)
    echo "unknown command: $CMD" >&2
    usage
    exit 1
    ;;
esac
