# Harbor Lane Book Club Tracker

A Python utility designed to automate weekly reading statistics, report generation, and persistent data storage.

## Features
- **Statistical Summary:** Calculates weekly average page counts across member logs.
- **Automated Reporting:** Generates timestamped human-readable summaries in `minutes.txt` using `datetime`.
- **State Persistence:** Serializes session metrics into `club_stats.pkl` via `pickle` for future retrieval.

## Usage
```bash
python book_club_tracker.py
```
