import json
import subprocess

#
# Run scrapers first
#

try:
    subprocess.run(
        ["python", "scripts/scrape_hbtownhall.py"],
        check=True
    )
except Exception as e:
    print(
        f"HB Town Hall scraper failed: {e}"
    )

try:
    subprocess.run(
        ["python", "scripts/scrape_ncbrunswick.py"],
        check=True
    )
except Exception as e:
    print(
        f"NC Brunswick scraper failed: {e}"
    )

all_events = []
seen = set()


def add_events(filename, source):

    try:

        with open(
            filename,
            "r"
        ) as f:

            events = json.load(f)

        for event in events:

            key = (
                event.get(
                    "title",
                    ""
                )
                .lower()
                .strip()
            )

            if key not in seen:

                seen.add(key)

                event["source"] = source

                all_events.append(event)

        print(
            f"Loaded {len(events)} events from {filename}"
        )

    except FileNotFoundError:

        print(
            f"{filename} not found"
        )

    except Exception as e:

        print(
            f"Error reading {filename}: {e}"
        )


#
# Existing sources
#

add_events(
    "concerts.json",
    "concerts"
)

add_events(
    "hobbs_events.json",
    "hobbs"
)

add_events(
    "coastal_events.json",
    "coastal"
)

#
# New sources
#

add_events(
    "hbtownhall.json",
    "hbtownhall"
)

add_events(
    "ncbrunswick.json",
    "ncbrunswick"
)

#
# Save combined file
#

with open(
    "all_events.json",
    "w"
) as f:

    json.dump(
        all_events,
        f,
        indent=2
    )

print()

print(
    f"Created all_events.json with {len(all_events)} events"
)

print()
