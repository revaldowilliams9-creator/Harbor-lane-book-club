# 📚 Harbor Lane Book Club Tracker

A lightweight **Python** utility designed to automate weekly reading statistics, timestamped report generation, and persistent data serialization.

## 💡 Why I Built This
I built this tracker to automate repetitive statistical summaries and preserve application state across sessions without setting up a full database server. Combining `datetime` audit logging with `pickle` object serialization allowed me to generate both human-readable reports and reloadable binary snapshots.

## ✨ Key Features
* 📊 **Statistical Summary:** Calculates weekly average page counts across member reading logs.
* 📝 **Automated Reporting:** Generates timestamped human-readable summaries in `minutes.txt` using Python's `datetime` module.
* 💾 **State Persistence:** Serializes session metrics into `club_stats.pkl` via `pickle` for fast reload and retrieval.

## 📂 Project Structure
* 🐍 `book_club_tracker.py` — Core script that computes reading averages, formats timestamps, and writes output artifacts.
* 📄 `minutes.txt` — Generated plain-text summary report with audit timestamps.
* 🗄️ `club_stats.pkl` — Serialized binary snapshot of session metrics.

## 🚀 Quick Start & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/revaldowilliams9-creator/Harbor-lane-book-club.git
   cd Harbor-lane-book-club
   ```

2. **Run the reading tracker:**
   ```bash
   python book_club_tracker.py
   ```
## 📸 Live Preview
<img width="404" height="300" alt="image" src="https://github.com/user-attachments/assets/528ce44e-3f8a-4e9c-b03e-7fbabd0cc2be" />

