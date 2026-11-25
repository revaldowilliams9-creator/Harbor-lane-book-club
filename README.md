# Harbor Lane Book Club Tracker

A Python utility designed to automate weekly reading statistics, report generation, and persistent data storage.

## 💡 Why I Built This 
I built this tracker to automate repetitive statistical summaries and preserve application state across sessions without setting up a full database server. Combining datetime audit logging with pickle object serialization allowed me to generate both human-readable reports and reloadable binary snapshots.

## Features
- **Statistical Summary:** Calculates weekly average page counts across member logs.
- **Automated Reporting:** Generates timestamped human-readable summaries in `minutes.txt` using `datetime`.
- **State Persistence:** Serializes session metrics into `club_stats.pkl` via `pickle` for future retrieval.

## Usage
```bash
python book_club_tracker.py
```
