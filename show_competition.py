#!/usr/bin/env python3
"""
show_competition.py — Display a competition edition from crosscountry.aero by ID.

Usage:
    python show_competition.py <id>

Example:
    python show_competition.py 91
"""

import sys
import json
import urllib.request
from datetime import datetime

API_URL = "https://data.crosscountry.aero/public/get/events"

STATUS_MAP = {
    10: "Upcoming / Active",
    20: "Finished",
}

COUNTRY_FLAG = {
    "IT": "🇮🇹", "GB": "🇬🇧", "FR": "🇫🇷", "PL": "🇵🇱", "NL": "🇳🇱",
    "US": "🇺🇸", "AU": "🇦🇺", "ES": "🇪🇸", "DE": "🇩🇪", "NO": "🇳🇴",
    "SI": "🇸🇮", "ZA": "🇿🇦", "CL": "🇨🇱", "SK": "🇸🇰", "BA": "🇧🇦",
    "AT": "🇦🇹", "RU": "🇷🇺", "LT": "🇱🇹", "SE": "🇸🇪", "AE": "🇦🇪",
}


def fetch_events() -> list[dict]:
    """Fetch all competition editions from the API."""
    req = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; crosscountry-viewer/1.0)"},
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())


def find_by_id(events: list[dict], competition_id: int) -> dict | None:
    """Return the event matching the given id, or None."""
    return next((e for e in events if e.get("id") == competition_id), None)


def format_date(date_str: str | None) -> str:
    """Pretty-print an ISO date string, e.g. '2026-05-23' → '23 May 2026'."""
    if not date_str:
        return "—"
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%-d %b %Y")
    except ValueError:
        return date_str


def print_competition(event: dict) -> None:
    """Display competition details in a readable format."""
    country = event.get("country", "")
    flag = COUNTRY_FLAG.get(country, "🌍")
    status_label = STATUS_MAP.get(event.get("status"), f"Unknown ({event.get('status')})")
    is_final = "🏆 Yes" if event.get("final") else "No"

    first_date      = format_date(event.get("firstDate"))
    first_race_date = format_date(event.get("firstRacingDate"))
    last_date       = format_date(event.get("lastDate"))
    reg_close       = format_date(event.get("registrationCloseDate"))

    width = 52
    divider = "─" * width

    print()
    print(f"╔{'═' * width}╗")
    print(f"║  {event.get('fullEditionTitle', 'N/A'):<{width - 2}}║")
    print(f"╚{'═' * width}╝")
    print()

    rows = [
        ("ID",                    str(event.get("id", "—"))),
        ("Edition title",         event.get("editionTitle", "—")),
        ("Venue",                 event.get("venue") or "—"),
        ("Country",               f"{flag}  {country}" if country else "—"),
        ("Status",                status_label),
        ("World Final",           is_final),
        (divider,                 ""),
        ("Opening date",          first_date),
        ("First racing day",      first_race_date),
        ("Closing date",          last_date),
        ("Registration closes",   reg_close),
        (divider,                 ""),
        ("Competition ID",        str(event.get("competitionId", "—"))),
        ("Edition number",        str(event.get("edition", "—"))),
        ("Series",                str(event.get("series", "—"))),
        ("Rule space ID",         str(event.get("ruleSpaceId", "—"))),
        ("Score version",         str(event.get("scoreVersion", "—"))),
        ("Handicap list ID",      str(event.get("handicapListId", "—"))),
    ]

    for label, value in rows:
        if label == divider:
            print(f"  {divider}")
        else:
            print(f"  {label:<22}  {value}")

    print()


def list_competitions(events: list[dict]) -> None:
    """Print a compact table of all available competitions."""
    print(f"\n  {'ID':>5}  {'Country':^7}  {'Dates':<24}  Title")
    print(f"  {'─'*5}  {'─'*7}  {'─'*24}  {'─'*40}")
    for e in events:
        cid     = e.get("id", "?")
        country = e.get("country", "??")
        flag    = COUNTRY_FLAG.get(country, "  ")
        first   = (e.get("firstDate") or "")[:10]
        last    = (e.get("lastDate")  or "")[:10]
        dates   = f"{first} → {last}" if first else "—"
        title   = e.get("fullEditionTitle", "N/A")
        print(f"  {cid:>5}  {flag} {country:<4}  {dates:<24}  {title}")
    print()


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    arg = sys.argv[1]

    # Special flag: list all
    if arg in ("-l", "--list"):
        print("\nFetching competition list …")
        events = fetch_events()
        list_competitions(events)
        sys.exit(0)

    # Parse the ID
    try:
        competition_id = int(arg)
    except ValueError:
        print(f"Error: '{arg}' is not a valid integer ID.")
        print("Usage: python show_competition.py <id>")
        print("       python show_competition.py --list   # show all competitions")
        sys.exit(1)

    print(f"\nFetching competition #{competition_id} …")
    try:
        events = fetch_events()
    except Exception as exc:
        print(f"Error fetching data: {exc}")
        sys.exit(1)

    event = find_by_id(events, competition_id)
    if event is None:
        print(f"\nNo competition found with ID {competition_id}.")
        print("Use --list to see all available IDs.")
        sys.exit(1)

    print_competition(event)


if __name__ == "__main__":
    main()
