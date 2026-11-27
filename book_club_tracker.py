import pickle
from datetime import date


def calculate_average_pages(pages_list):
    """Return the average of a list of page counts, or 0 if empty."""
    if not pages_list:
        return 0.0
    return sum(pages_list) / len(pages_list)


def get_member_pages():
    """Prompt the user to enter comma-separated page counts."""
    raw_input = input("Enter pages read by each member (comma-separated, e.g. 120, 85, 200): ")
    pages = []
    for item in raw_input.split(","):
        cleaned = item.strip()
        if cleaned.isdigit():
            pages.append(int(cleaned))
        elif cleaned:
            print(f"Skipping invalid entry: '{cleaned}'")
    return pages


def main():
    pages = get_member_pages()
    if not pages:
        print("No valid page numbers entered. Exiting.")
        return

    average_pages = round(calculate_average_pages(pages), 2)
    today_text = date.today().strftime("%d %B %Y")

    print(f"\nAverage pages read this week: {average_pages}")
    print(f"Date: {today_text}")

    # Append to minutes.txt so past weeks are preserved
    with open("minutes.txt", "a", encoding="utf-8") as f:
        f.write(f"[{today_text}] Members: {len(pages)} | Average Pages: {average_pages}\n")

    # Save structured session stats using pickle
    club_stats = {
        "date": today_text,
        "member_count": len(pages),
        "pages": pages,
        "average_pages": average_pages,
    }

    with open("club_stats.pkl", "wb") as f:
        pickle.dump(club_stats, f)

    with open("club_stats.pkl", "rb") as f:
        loaded_stats = pickle.load(f)

    print("Verified saved stats:", loaded_stats)


if __name__ == "__main__":
    main()
