# Focus-Safe Browser Launching Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make it impossible for agent browser work to steal the user's focus, while keeping the SFPL/NewsBank credential flow workable.

**Architecture:** One sanctioned launcher script that only permits headless Chrome; session persistence via a dedicated profile so the single interactive login (a user-scheduled, expected event) carries into any number of headless workers afterward; runbook and prompt-boilerplate updates so no agent invents its own launch path again.

**Tech Stack:** bash + puppeteer-core (already in `scripts/archive-recovery/package.json`), Chrome headless "new" mode.

## Global Constraints

- Zero unscheduled visible windows or focus changes, ever. The three documented failure modes are all banned at the launcher level: `open -a` (routes to the user's running Chrome), direct-binary headful exec (async self-activation; an lsappinfo before/after check has a race and proves nothing), and leaving any headful Chrome running unattended (a parked login page grabbed focus later).
- Chrome headless "new" mode is the only agent-launched browser mode.
- The one visible event allowed is the login ceremony: user-initiated, announced, and torn down immediately after login.
- Credentials are never automated (runbook rule).
- No em dashes in new prose.

## Why this works (the design in three sentences)

Headless "new" Chrome creates no window and cannot take focus, and it fully supports profiles, cookies, and modern sites. SFPL ezproxy sessions live in cookies inside a `--user-data-dir` profile, so one interactive login into a dedicated profile makes every subsequent headless run on that profile authenticated, until the session expires. Chrome locks a profile to one running instance, so the launcher serializes access (login ceremony and workers never overlap).

---

### Task 1: the sanctioned launcher + session probe

**Files:**
- Create: `scripts/research/iso_chrome.sh` (the ONLY sanctioned launch path)
- Create: `scripts/research/iso_probe.js` (headless session-validity probe)
- Test: `tests/test_iso_chrome.py` (offline shell-contract tests)

**Interfaces:**
- Produces: `iso_chrome.sh <headless|login|stop|status> [--profile NAME]`.
  - `headless`: prints a ready `browserURL` (`http://127.0.0.1:<port>`) after launching `"…/Google Chrome" --headless=new --remote-debugging-port=<free port 9230+> --user-data-dir="$HOME/.cache/sf-election-iso/<NAME>"` as a detached subprocess; refuses to start if the profile is locked by another instance.
  - `login`: the ceremony. Refuses to run unless `ISO_CHROME_LOGIN_ACK=yes` is set (the human-in-the-loop latch: an agent can only run it when the controller relays the user's explicit go). Launches VISIBLE Chrome on the same profile at the SFPL login URL, prints "log in, then run: iso_chrome.sh stop", and does nothing else.
  - `stop`: kills only instances holding this profile (pattern-matched on the user-data-dir path).
  - `status`: reports profile lock state and whether a debug port answers.
- `iso_probe.js <browserURL>`: connects with puppeteer-core, loads the runbook's known docref, exits 0 if authenticated, 3 if it sees the auth-wall signature text ("Articles and Databases"), never renders anything visible.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_iso_chrome.py
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "research" / "iso_chrome.sh"


def run(*args, env=None):
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True,
                          text=True, env=env)


def test_login_refuses_without_ack():
    r = run("login")
    assert r.returncode != 0
    assert "ISO_CHROME_LOGIN_ACK" in r.stderr


def test_headless_arg_wiring_dry_run():
    r = run("headless", "--dry-run")
    assert r.returncode == 0
    assert "--headless=new" in r.stdout
    assert "open -a" not in r.stdout
    assert "user-data-dir" in r.stdout


def test_unknown_command_fails():
    assert run("dance").returncode != 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_iso_chrome.py -q`
Expected: FAIL (script missing).

- [ ] **Step 3: Implement `iso_chrome.sh` and `iso_probe.js`**

The script: strict bash (`set -euo pipefail`); subcommands as above; `--dry-run` on `headless` prints the exact command without executing (this is what the tests and future audits check); port selection scans 9230-9250 for a free port; the headless launch backgrounds via `nohup … &` and waits for the debug port to answer before printing `browserURL`; `login` checks the ack latch, echoes the ceremony instructions, and launches visible Chrome in the foreground of ITS OWN invocation (the user runs or approves this; agents cannot set the latch themselves). `iso_probe.js` per the interface, modeled on the port-parameterized copy of `session_probe.js` used earlier (auth-wall text match from the archive-recovery runbook).

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_iso_chrome.py -q`
Expected: 3 passed. Then a live smoke check: `bash scripts/research/iso_chrome.sh headless` followed by `node scripts/research/iso_probe.js <printed url>` (expect exit 3, auth wall, since the fresh profile is unauthenticated), then `iso_chrome.sh stop`, and confirm `lsappinfo front` never changed during the sequence (record before/after in the report; with headless=new there is no window to activate, this is a belt-and-suspenders observation, not the safety argument).

- [ ] **Step 5: Commit**

```bash
git add scripts/research/iso_chrome.sh scripts/research/iso_probe.js tests/test_iso_chrome.py
git commit -m "feat(research): focus-safe sanctioned browser launcher (headless-only + login ceremony latch)"
```

---

### Task 2: make the sanctioned path the only path

**Files:**
- Modify: `docs/archive-recovery-runbook.md` (prerequisites section: replace the raw headful launch instructions with iso_chrome.sh usage; the login ceremony documented as the one visible event)
- Modify: `docs/research/RUNBOOK.md` (section 4 tool table + section 6.7: browser escalation ends at headless iso_chrome, then FLAG; delete the Claude-in-Chrome suggestion for subagents)
- Modify: `.claude/skills/newsbank-election-recovery/SKILL.md` (launch instructions point at iso_chrome.sh; add the ceremony flow)

**Interfaces:**
- Consumes: Task 1's launcher CLI, exactly as specified.

- [ ] **Step 1: Update the three documents** — each references `iso_chrome.sh` subcommands verbatim, states the three banned launch modes with one-line reasons, and describes the ceremony flow: user says go, controller sets the ack latch for a single `login` invocation, user logs in, `stop`, then headless workers reuse the profile.
- [ ] **Step 2: Audit for stragglers** — `grep -rn "remote-debugging-port\|open -a\|MacOS/Google Chrome" scripts docs .claude/skills --include='*.md' --include='*.js' --include='*.cjs' --include='*.sh'` and update every instruction that still shows a raw launch (the reference implementations in scripts/archive-recovery/ may keep their `puppeteer.connect` lines since they consume a browserURL, but their header comments must point at iso_chrome.sh).
- [ ] **Step 3: Run `uv run pytest -q` (guard), commit**

```bash
git add -A
git commit -m "docs: all browser work routes through the focus-safe launcher"
```

---

## Definition of Done

- `iso_chrome.sh` exists, tested, and is referenced by every browser-touching document and skill.
- A full NewsBank session is demonstrably possible with exactly one visible, user-approved window: ceremony login, then headless workers on the shared profile.
- No document anywhere instructs a raw headful launch.
