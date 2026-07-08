#!/usr/bin/env python3
"""Build data/elections_master.csv — the master list of San Francisco elections,
1849–present, with a flag for whether we've recovered an election-night count.

Three compiled sources (2026-06-18, web research, see README "Missing from the
record"):
  P1  1907–2025  — DataSF Ballot-Propositions DB (88s2-6ua9) + SFPL voter-pamphlet
                   collection + SF Dept. of Elections past-elections list.
  P2A 1849–1906  — CA statewide generals (Pres/Gov + state ticket): Wikipedia +
                   JoinCalifornia + CA Blue Book / Statement of Vote.
  P2B 1856–1907  — SF municipal/charter/special: Daily Alta (CDNC) + SF Municipal
                   Reports Registrar tables + Wikipedia mayoral pages + FoundSF.

The `recovered` column is computed against packages/data/elections.json so it never
drifts from the dataset.
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# --- P1: 1907–2025 (date, kind) -------------------------------------------------
P1 = [
 ("1907-11-05","Municipal"),("1908-05-11","Special"),("1908-11-03","General"),
 ("1908-11-12","Special"),
 # 1909-06-22 was a 9-proposition bond special, not a primary (the direct
 # primary law was in litigation; CDNC recovery 2026-07-08), and a second
 # Geary bond special followed two days later, absent from all prior indexes
 ("1909-06-22","Special"),("1909-06-24","Special"),("1909-11-02","General"),
 ("1909-12-30","Special"),("1911-11-07","Municipal"),("1912-03-28","Special"),
 # 1912-03-29: initiative-ordinance special held the day after the Civic
 # Center bond special (invalidated pre-election; 31,968 cast per the Call)
 ("1912-03-29","Special"),
 ("1912-11-05","General"),("1912-12-10","Special"),("1913-04-22","Special"),
 ("1913-08-26","Special"),("1914-11-03","General"),("1915-03-16","Special"),
 ("1915-04-20","Special"),("1916-11-07","General"),("1917-10-30","Special"),
 ("1917-11-06","Municipal"),("1918-11-05","General"),("1920-11-02","General"),
 ("1921-03-08","Special"),("1922-11-07","General"),("1922-11-21","Special"),
 ("1923-11-06","Municipal"),("1924-10-07","Special"),("1924-11-04","General"),
 ("1925-11-03","Municipal"),("1926-11-02","General"),("1927-06-14","Special"),
 ("1927-11-08","Municipal"),("1928-05-01","Special"),("1928-08-28","Primary"),
 ("1928-11-06","General"),("1929-11-05","Municipal"),("1930-08-26","Primary"),
 ("1930-11-04","General"),("1931-02-06","Special"),("1931-03-26","Special"),
 ("1931-11-03","Municipal"),("1932-05-03","Special"),("1932-08-30","Primary"),
 ("1932-11-08","General"),("1933-04-11","Special"),("1933-06-27","Special"),
 ("1933-11-07","Municipal"),("1933-12-19","Special"),("1934-11-06","General"),
 ("1935-05-02","Special"),("1935-11-05","Municipal"),("1936-11-03","General"),
 ("1937-03-09","Special"),("1937-11-02","Municipal"),("1938-09-27","Special"),
 ("1938-11-08","General"),("1939-05-19","Special"),("1939-11-07","Municipal"),
 ("1940-05-07","Special"),("1940-11-05","General"),("1941-11-04","Municipal"),
 ("1942-06-09","Special"),("1942-11-03","General"),("1943-04-20","Special"),
 ("1943-11-02","Municipal"),("1944-05-16","Primary"),("1944-11-07","General"),
 ("1945-11-06","Municipal"),("1946-07-16","Recall"),("1946-11-05","General"),
 ("1947-11-04","Municipal"),("1948-06-01","Primary"),("1948-11-02","General"),
 ("1949-11-08","Municipal"),("1950-06-06","Primary"),("1950-11-07","General"),
 ("1951-11-06","Municipal"),("1952-06-03","Primary"),("1952-11-04","General"),
 ("1953-11-03","Municipal"),("1954-06-08","Primary"),("1954-11-02","General"),
 ("1955-11-08","Municipal"),("1956-06-05","Primary"),("1956-11-06","General"),
 ("1957-11-05","Municipal"),("1958-06-03","Primary"),("1958-11-04","General"),
 ("1959-11-03","Municipal"),("1960-06-07","Primary"),("1960-11-08","General"),
 ("1961-11-07","Municipal"),("1962-06-05","Primary"),("1962-11-06","General"),
 ("1963-11-05","Municipal"),("1964-06-02","Primary"),("1964-11-03","General"),
 ("1965-11-02","Municipal"),("1966-06-07","Primary"),("1966-11-08","General"),
 ("1967-11-07","Municipal"),("1968-06-04","Primary"),("1968-11-05","General"),
 ("1969-11-04","Municipal"),("1970-06-02","Primary"),("1970-11-03","General"),
 ("1971-11-02","Municipal"),("1972-06-06","Primary"),("1972-11-07","General"),
 ("1973-11-06","Municipal"),("1974-06-04","Primary"),("1974-11-05","General"),
 ("1975-11-04","Municipal"),("1976-06-08","Primary"),("1976-11-02","General"),
 ("1977-08-02","Special"),("1977-11-08","Municipal"),("1978-06-06","Primary"),
 ("1978-11-07","General"),("1979-11-06","Municipal"),("1980-06-03","Primary"),
 ("1980-08-19","Special"),("1980-11-04","General"),("1981-11-03","Municipal"),
 ("1982-06-08","Primary"),("1982-11-02","General"),("1983-04-26","Recall"),
 ("1983-11-08","Municipal"),("1984-06-05","Primary"),("1984-11-06","General"),
 ("1985-11-05","Municipal"),("1986-06-03","Primary"),("1986-11-04","General"),
 ("1987-06-02","Special"),("1987-11-03","Municipal"),("1987-12-08","Runoff"),
 ("1988-06-07","Primary"),("1988-11-08","General"),("1989-11-07","Municipal"),
 ("1990-06-05","Primary"),("1990-11-06","General"),("1991-11-05","Municipal"),
 ("1991-12-10","Runoff"),("1992-06-02","Primary"),("1992-11-03","General"),
 ("1993-06-15","Special"),("1993-11-02","General"),("1994-06-07","Primary"),
 ("1994-11-08","General"),("1995-11-07","Municipal"),("1995-12-12","Runoff"),
 ("1996-03-26","Primary"),("1996-11-05","General"),("1997-06-03","Special"),
 ("1997-11-04","Municipal"),("1998-06-02","Primary"),("1998-11-03","General"),
 ("1999-11-02","Municipal"),("1999-12-14","Runoff"),("2000-03-07","Primary"),
 ("2000-11-07","General"),("2000-12-12","Runoff"),("2001-11-06","Municipal"),
 ("2001-12-11","Runoff"),("2002-03-05","Primary"),("2002-11-05","General"),
 ("2002-12-10","Runoff"),("2003-10-07","Special"),("2003-11-04","Municipal"),
 ("2003-12-09","Runoff"),("2004-03-02","Primary"),("2004-11-02","General"),
 ("2005-11-08","Special"),("2006-06-06","Primary"),("2006-11-07","General"),
 ("2007-11-06","Municipal"),("2008-02-05","Primary"),("2008-04-08","Primary"),
 ("2008-06-03","Primary"),("2008-11-04","General"),("2009-05-19","Special"),
 ("2009-11-03","Municipal"),("2010-06-08","Primary"),("2010-11-02","General"),
 ("2011-11-08","Municipal"),("2012-06-05","Primary"),("2012-11-06","General"),
 ("2013-11-05","Municipal"),("2014-06-03","Primary"),("2014-11-04","General"),
 ("2015-11-03","Municipal"),("2016-06-07","Primary"),("2016-11-08","General"),
 ("2018-06-05","Primary"),("2018-11-06","General"),("2019-11-05","Municipal"),
 ("2020-03-03","Primary"),("2020-11-03","General"),("2021-09-14","Recall"),
 ("2022-02-15","Special"),("2022-04-19","Special"),("2022-06-07","Primary"),
 ("2022-11-08","General"),("2024-03-05","Primary"),("2024-11-05","General"),
 ("2025-09-16","Recall"),("2025-11-04","Special"),
 # added: real elections the proposition-based sources skipped (we hold data for them)
 ("1910-11-08","General"),   # Gov. Hiram Johnson general (no SF prop that year)
 ("1975-12-11","Runoff"),    # Moscone–Barbagelata mayoral runoff
 ("1987-04-07","Special"),   # Special Congressional Election
 ("2026-06-02","Primary"),   # upcoming June 2026 primary
]

# --- P2A: CA statewide generals 1849–1906 (date, kind, top office) ---------------
P2A = [
 ("1849-11-13","General","Governor + Legislature + ratify 1849 Constitution"),
 ("1850-10-07","General","State officers + Legislature"),
 ("1851-09-03","Gubernatorial","Governor"),("1852-11-02","Presidential","President"),
 ("1853-09-07","Gubernatorial","Governor"),("1854-09-06","General","Congress-at-large + Legislature"),
 ("1855-09-05","Gubernatorial","Governor"),("1856-11-04","Presidential","President"),
 ("1857-09-02","Gubernatorial","Governor"),("1858-09-01","General","Legislature + Controller"),
 ("1859-09-07","Gubernatorial","Governor"),("1860-11-06","Presidential","President"),
 ("1861-09-04","Gubernatorial","Governor"),("1862-09-03","General","Supt. Public Instruction + Legislature"),
 ("1863-09-02","Gubernatorial","Governor"),("1864-11-08","Presidential","President + Congress"),
 # 1865 general was held Wednesday Sept 6, not Sept 5 (Alta masthead check,
 # CDNC recovery 2026-07-08)
 ("1865-09-06","General","Legislature"),("1867-09-04","Gubernatorial","Governor"),
 ("1867-10-16","General","Supt. Public Instruction"),("1868-11-03","Presidential","President + Congress"),
 ("1871-09-06","Gubernatorial","Governor"),("1871-10-18","General","Supt. Public Instruction"),
 ("1872-11-05","Presidential","President + Congress"),("1873-09-03","General","Legislature"),
 ("1875-09-01","Gubernatorial","Governor"),("1875-10-20","General","Supt. Public Instruction"),
 ("1876-11-07","Presidential","President + Congress"),("1877-09-05","General","Legislature"),
 ("1878-06-19","Special","Delegates to the 1878-79 state Constitutional Convention"),
 ("1879-05-07","Special","Ratification of the 1879 Constitution"),
 ("1879-09-03","Gubernatorial","Governor (1879 Constitution)"),
 ("1880-11-02","Presidential","President + Congress + Legislature"),
 ("1882-11-07","Gubernatorial","Governor + state officers"),
 ("1884-11-04","Presidential","President + Congress + Legislature"),
 ("1886-11-02","Gubernatorial","Governor + state officers"),
 ("1888-11-06","Presidential","President + Congress + Legislature"),
 ("1890-11-04","Gubernatorial","Governor + state officers"),
 ("1892-11-08","Presidential","President + Congress + Legislature"),
 ("1894-11-06","Gubernatorial","Governor + state officers"),
 ("1896-11-03","Presidential","President + Congress + Legislature"),
 ("1898-11-08","Gubernatorial","Governor + state officers"),
 ("1900-11-06","Presidential","President + Congress + Legislature"),
 ("1902-11-04","Gubernatorial","Governor + state officers"),
 ("1904-11-08","Presidential","President + Congress + Legislature"),
 ("1906-11-06","Gubernatorial","Governor + state officers"),
]

# --- P2B: SF municipal/charter/special 1856–1907 (date, kind, what, conf) --------
# conf: H exact, A approx (month/cycle), U date unknown (year placeholder)
P2B = [
 ("1856-11-04","Municipal","Mayor (Burr) + city offices — 1st under Consolidation Act","H"),
 ("1857-09-04","Municipal","City/county offices","A"),
 ("1858-07-01","Municipal","Annual city offices — exact date unknown","U"),
 ("1859-09-07","Municipal","Mayor (Teschemacher) + city offices","H"),
 ("1861-05-21","Municipal","Mayor (Teschemacher re-elected)","H"),
 ("1863-05-19","Municipal","Mayor (Coon)","H"),("1865-05-16","Municipal","Mayor (Coon re-elected)","H"),
 ("1867-09-04","Municipal","Mayor (McCoppin)","H"),("1869-09-01","Municipal","Mayor (Selby)","H"),
 ("1871-09-06","Municipal","Mayor (Alvord)","H"),("1873-09-03","Municipal","Mayor (Otis)","H"),
 ("1875-09-01","Municipal","Mayor (Bryant)","H"),("1877-09-05","Municipal","Mayor (Bryant re-elected)","H"),
 ("1879-09-03","Municipal","Mayor (Kalloch) — 1st under 1879 Constitution","H"),
 ("1880-03-30","Charter","Board of Freeholders (draft new charter) — registrar cumulative table (vol47 p.277): 30,877 votes","H"),
 ("1880-09-08","Charter","Proposed new charter — REJECTED; dated Sept 8 1880 by the registrar cumulative table (vol47 p.277): 23,398 votes","H"),
 ("1881-09-07","Municipal","Mayor (Blake) — last September municipal","H"),
 ("1882-11-07","Municipal","Mayor (Bartlett) — 1st November municipal","H"),
 ("1883-03-03","Charter","Proposed new charter — REJECTED; dated March 3 1883 by the registrar cumulative table (vol47 p.277): 18,764 votes","H"),
 ("1884-03-18","Special","Assemblyman (special) — registrar cumulative table (vol47 p.277): 2,655 votes","H"),
 ("1884-11-04","Municipal","Mayor (Bartlett re-elected)","H"),
 ("1886-11-02","Municipal","Mayor (Pond)","H"),
 ("1887-04-12","Charter","Amendments and proposed charter — REJECTED; dated April 12 1887 by the registrar cumulative table (vol47 p.277): 25,959 votes","H"),
 ("1888-11-06","Municipal","Mayor (Pond re-elected)","H"),
 ("1890-11-04","Municipal","Mayor (Sanderson)","H"),("1892-11-08","Municipal","Mayor (Ellert)","H"),
 ("1894-11-06","Municipal","Mayor (Sutro)","H"),("1896-11-03","Municipal","Mayor (Phelan)","H"),
 ("1897-12-27","Charter","Board of Freeholders (draft new charter)","H"),
 ("1898-05-26","Charter","New (1898/1900) Charter RATIFIED","H"),
 ("1898-11-08","Municipal","Mayor (Phelan re-elected), consolidated onto the state ballot (no separate Nov 1 municipal election; Municipal Reports cumulative table)","H"),
 ("1899-11-07","Municipal","Mayor (Phelan) — 1st under 1898 charter","H"),
 ("1899-12-27","Special","Park-bond special (Municipal Reports cumulative table)","H"),
 ("1899-12-29","Special","Sewer-bond special (the DOE turnout table dates it 1899-12-02; see doe-data-discrepancies.md)","H"),
 ("1902-12-02","Special","Geary Street Railroad bond special (DOE turnout table; Municipal Reports confirm)","H"),
 ("1902-12-04","Special","Charter-amendments special (Municipal Reports cumulative table)","H"),
 ("1903-09-29","Special","Sewer and other bonds special (DOE turnout table; Municipal Reports confirm)","H"),
 ("1903-10-08","Special","Street-railroad bonds special (DOE turnout table; Municipal Reports confirm)","H"),
 ("1901-11-05","Municipal","Mayor (Schmitz)","H"),("1903-11-03","Municipal","Mayor (Schmitz re-elected)","H"),
 ("1905-11-07","Municipal","Mayor (Schmitz, 3rd) + Supervisors","H"),
 ("1907-11-05","Municipal","Mayor (Taylor) — post-graft-trial","H"),
]

# --- merge ----------------------------------------------------------------------
rows = {}  # date -> dict
def add(date, kind, desc, level, conf, src):
    r = rows.get(date)
    if not r:
        rows[date] = {"date": date, "kinds": {kind}, "descs": [desc] if desc else [],
                      "levels": {level}, "conf": conf, "src": {src}}
    else:
        r["kinds"].add(kind)
        if desc and desc not in r["descs"]:
            r["descs"].append(desc)
        r["levels"].add(level)
        r["src"].add(src)
        if conf == "H":
            r["conf"] = "H"

for d, k in P1:
    add(d, k, "", "city", "H", "SFPL/DataSF/DOE")
for d, k, office in P2A:
    add(d, k, office, "statewide", "H", "Blue Book/SOV/Wikipedia")
for d, k, what, conf in P2B:
    add(d, k, what, "municipal", conf, "Municipal Reports/CDNC/Wikipedia")

# --- recovered? cross-reference the live dataset --------------------------------
el = json.loads((ROOT / "packages" / "data" / "elections.json").read_text())
night = {e["id"]: e.get("nightPct") for e in el}
# an election is "missing" if we hold no election-night count; among the
# missing, distinguish those whose FINAL count we do hold (a certified or
# registrar total from any source) from those with no recovered data at all
finals = set(night)  # every canvass/modern election carries a certified final
for fn in ("sf_turnout_pre1899.csv", "sf_turnout_1891_1907.csv"):
    with open(ROOT / "data" / fn, newline="") as f:
        for r in csv.DictReader(f):
            if r["ballots_cast"]:
                finals.add(r["election_date"])
DOE_TABLE_DATE_FIXES = {"2001-12-10": "2001-12-11", "1899-12-02": "1899-12-29"}
with open(ROOT / "data" / "sf_turnout_history_doe_1899_2019.csv", newline="") as f:
    for r in csv.DictReader(f):
        if r["ballots_cast"] and r["ballots_cast"] not in ("n/a",):
            finals.add(DOE_TABLE_DATE_FIXES.get(r["election_date"], r["election_date"]))
def recovered(date):
    p = night.get(date)
    if p is not None:
        return "night", p
    return ("final-only", "") if date in finals else ("no", "")

# --- write ----------------------------------------------------------------------
out = ROOT / "data" / "elections_master.csv"
KIND_ORDER = ["Presidential","Gubernatorial","General","Primary","Municipal",
              "Charter","Special","Recall","Runoff"]
def kind_str(ks):
    return " + ".join(sorted(ks, key=lambda k: KIND_ORDER.index(k) if k in KIND_ORDER else 99))
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["election_date","year","level","kind","description",
                "recovered","night_pct","date_confidence","sources"])
    n_night = n_final = n_nothing = 0
    for date in sorted(rows):
        r = rows[date]
        rec, pct = recovered(date)
        if rec == "night": n_night += 1
        elif rec == "final-only": n_final += 1
        else: n_nothing += 1
        lvl = ("both" if {"statewide"} <= r["levels"] and
               ({"municipal"} <= r["levels"] or "city" in r["levels"])
               else ("statewide" if "statewide" in r["levels"]
                     else "municipal" if "municipal" in r["levels"] else "city"))
        conf = {"H":"exact","A":"approx","U":"date-unknown"}[r["conf"]]
        w.writerow([date, date[:4], lvl, kind_str(r["kinds"]),
                    "; ".join(r["descs"]), rec, pct, conf, "; ".join(sorted(r["src"]))])
    total = len(rows)
print(f"{total} distinct election dates -> {out}")
print(f"  recovered (night count):     {n_night}")
print(f"  missing, final count known:  {n_final}")
print(f"  missing, no data at all:     {n_nothing}")
