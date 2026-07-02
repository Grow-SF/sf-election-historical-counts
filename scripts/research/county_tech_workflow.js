export const meta = {
  name: 'county-tech-research',
  description: 'Fan out one resumable research agent per jurisdiction for the county counting-tech dataset',
  phases: [{ title: 'Research' }],
}

const WORKLIST = [
  {slug:"los-angeles-ca",name:"Los Angeles County",state:"CA",hints:"e-pollbooks (KNOWiNK 2020, VSAP); ASV?"},
  {slug:"orange-ca",name:"Orange County",state:"CA",hints:"e-pollbooks (Tenex 2020, VCA); no ASV"},
  {slug:"san-diego-ca",name:"San Diego County",state:"CA",hints:"e-pollbooks; ASV?"},
  {slug:"santa-clara-ca",name:"Santa Clara County",state:"CA",hints:"e-pollbooks (VCA)"},
  {slug:"sacramento-ca",name:"Sacramento County",state:"CA",hints:"VCA 2018"},
  {slug:"san-mateo-ca",name:"San Mateo County",state:"CA",hints:"VCA pilot 2018"},
  {slug:"napa-ca",name:"Napa County",state:"CA",hints:"VCA pilot 2018"},
  {slug:"madera-ca",name:"Madera County",state:"CA",hints:"VCA pilot 2018"},
  {slug:"nevada-ca",name:"Nevada County",state:"CA",hints:"VCA pilot 2018"},
  {slug:"fresno-ca",name:"Fresno County",state:"CA",hints:"e-pollbooks 2020"},
  {slug:"san-luis-obispo-ca",name:"San Luis Obispo County",state:"CA",hints:"e-pollbooks 2026"},
  {slug:"placer-ca",name:"Placer County",state:"CA",hints:"Sign-Scan-Go (AB 626)"},
  {slug:"riverside-ca",name:"Riverside County",state:"CA",hints:"ASV (pilot 2025, production 2026)"},
  {slug:"san-bernardino-ca",name:"San Bernardino County",state:"CA",hints:"ASV"},
  {slug:"san-francisco-ca",name:"San Francisco",state:"CA",hints:"CONTROL — no e-pollbook, no ASV"},
  {slug:"pennsylvania-knowink",name:"Pennsylvania (KNOWiNK counties)",state:"PA",hints:"national vignette — e-pollbooks"},
  {slug:"wisconsin-badgerbooks",name:"Wisconsin (Badger Books)",state:"WI",hints:"national vignette — e-pollbooks"},
  {slug:"new-york-epb",name:"New York (post-2019 e-pollbooks)",state:"NY",hints:"national vignette"},
]

const RECORD = {
  type:'object', required:['jurisdiction','state','tech','metrics'],
  properties:{
    jurisdiction:{type:'string'}, state:{type:'string'},
    tech:{type:'array', items:{type:'object', required:['type','status','evidence_url','confidence']}},
    metrics:{type:'array', items:{type:'object', required:['metric','year','value','source_url','confidence']}},
    notes:{type:'string'},
  },
}

const prompt = (j) => `You are researching ONE jurisdiction for the Long Count county dataset: ${j.name} (${j.state}). Hints: ${j.hints}.

STEP 0 — RESUME CHECK: run \`python3 scripts/research/validate_county_tech.py data/research/county-tech/${j.slug}.json\`. If it prints "OK", the record already exists and is valid — read that file and return its exact contents as your final message. Do NOT re-research.

Otherwise, research from PRIMARY sources and build the record:

TECH — record ALL four types ("not-adopted" WITH evidence is a finding, not a gap):
- epollbook (electronic pollbook / digital roster), asv (automated signature-verification software/scanner — humans comparing by eye = not-adopted), sign-scan-go (in-vote-center mail-ballot signature-verify + scan), vote-center (Voter's Choice Act model).
- Each: status (adopted|not-adopted|unknown); adopted_year = year of the FIRST ELECTION conducted with it (NOT the board-vote/contract-award date — put that in note); vendor if known; evidence_url (primary); confidence.
- Sources: CA SoS Voter's Choice Act adoption list, SoS "Voting Technology by County" / certified systems, the county Registrar's Election Administration Plan + press releases, Verified Voting.

METRICS — one row per (metric, year); cover recent even-year generals + the latest odd-year:
- oneweek_pct: % counted within 7 days, as CalVoter publishes it. ALWAYS check California Voter Foundation "Ballot Processing" (https://calvoter.org/content/ballot-processing) FIRST — the canonical comparable metric. (Its denominator is ballots-counted-to-date; record as published; chart-read values are confidence "primary" but say "chart-read" in note.)
- electionnight_pct: first-post-poll-close-report ballots ÷ certified final ballots. Needs the certified-final denominator; if unavailable, value = null.
- days_to_90: days until >=90% of certified final counted (needs per-day canvass totals; usually null).
- NEVER substitute a different denominator (e.g. "% of registered voters") for a missing metric — use value null, confidence "none", and a note.

Every value/status carries confidence: primary | secondary | estimated | none. A non-null value MUST have a source_url and confidence != none.

STEP WRITE — write the record to data/research/county-tech/${j.slug}.json in EXACTLY this schema:
{"jurisdiction":"","state":"","tech":[{"type":"","status":"","adopted_year":null,"first_election":"","vendor":"","evidence_url":"","confidence":"","note":""}],"metrics":[{"metric":"","year":0,"value":null,"denominator":"","source_url":"","confidence":"","note":""}],"notes":""}

STEP VALIDATE — run \`python3 scripts/research/validate_county_tech.py data/research/county-tech/${j.slug}.json\` and fix until it prints "OK". Then return the record as your final message.`

log(`fanning out ${WORKLIST.length} jurisdictions`)
const results = await parallel(
  WORKLIST.map((j) => () =>
    agent(prompt(j), { label: j.slug, phase: 'Research', schema: RECORD, agentType: 'general-purpose' })
      .then((rec) => ({ slug: j.slug, ok: !!rec }))
      .catch(() => ({ slug: j.slug, ok: false }))
  )
)
const done = results.filter((r) => r && r.ok).map((r) => r.slug)
const failed = WORKLIST.map((j) => j.slug).filter((s) => !done.includes(s))
log(`research done: ${done.length}/${WORKLIST.length}; failed/skipped: ${failed.join(', ') || 'none'}`)
return { done, failed }