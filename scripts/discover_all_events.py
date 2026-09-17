name: Discover All Events

on:
  workflow_dispatch:

jobs:
  discover:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Libraries
        run: |
          pip install requests beautifulsoup4

      - name: Discover Events
        run: |
          python scripts/discover_all_events.py

      - name: Show Hobbs Events
        run: |
          cat hobbs_events.json
