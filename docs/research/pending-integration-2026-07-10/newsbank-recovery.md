# NewsBank recovery run — Sacramento Bee / Fresno Bee / San Jose Mercury News, 2012/2014/2016 June primaries

Run started 2026-07-10. Isolated Chrome per runbook: port 9224,
`--user-data-dir=/tmp/newsbank-iso-profile`, off-screen window position,
throttling disabled. Launch verified no focus theft (FRONT_BEFORE == FRONT_AFTER).

Targets:
1. Sacramento Bee 2012-06-06, 2014-06-04 (Sacramento County; 2016-06-08 if time)
2. Fresno Bee 2012-06-06, 2014-06-04 (Fresno County)
3. San Jose Mercury News 2012-06-06 (Santa Clara County; would replace an 80.06 next-day ceiling)

## Session state

- `/tmp/newsbank-iso-profile` did NOT exist before this run (fresh profile,
  no carried-over ezproxy session from a prior run).
- Ran `session_probe.js` (copied to scratch as `session_probe_9224.js`,
  port adapted to 9224) against a known docref
  (`news/0EB4F969E1C867F6`, WORLDNEWS).
- Result: **AUTH WALL**. Page title: "SFPL — Articles & Databases Access
  (Login)". Body snippet: "Skip to main content | Articles and Databases -
  Authentication | The San Francisco Public Library offers a rich collection
  of online resources. Library card holders have immediate access to
  articles i..."
- Per the manual-credentials rule: did not surface any window, did not
  attempt any credential entry. Stopping here per protocol.

## Status: NEEDS_LOGIN — no targets attempted yet (blocked before target 1)

Chrome left running at :9224 with the fresh (now auth-walled) profile so the
login window can be surfaced on request via `window_login.js` (port-adapted).
Not yet killed — will kill only after either completing the run or on
explicit instruction, to avoid losing this profile's cookie jar mid-login.
