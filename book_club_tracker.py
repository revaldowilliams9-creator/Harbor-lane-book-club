# This program works out the average pages read, shows today's date,
# saves a summary to a text file, and saves the stats with pickle.
# (Oliver, 2023, Chapters 5-8)

import pickle
from datetime import date

# This function works out the average of a list of numbers
def calculate_average_pages(pages_list):
    total = sum(pages_list)           # add all the numbers together
    average = total / len(pages_list) # divide by how many there are
    return average

# ---- Main program ----

# Pages read by each member this week
pages = [120, 85, 200, 60, 150]

# Work out the average pages
average_pages = calculate_average_pages(pages)

# Get today's date and format it nicely e.g. "14 October 2026"
today = date.today()
today_text = today.strftime("%d %B %Y")

# ---- Print the summary ----
print("Average pages read this week:", average_pages)
print("Today's date:", today_text)

# ---- Save the summary to a text file ----
with open("minutes.txt", "w") as f:
    f.write("Average pages read this week: " + str(average_pages) + "\n")
    f.write("Today's date: " + today_text + "\n")

# ---- Save the club stats using pickle ----

# Put the data into a dictionary
club_stats = {
    "average_pages": average_pages,
    "date": today_text
}

# Save the dictionary to a pickle file
with open("club_stats.pkl", "wb") as f:
    pickle.dump(club_stats, f)

# ---- Load and verify the pickle file ----
with open("club_stats.pkl", "rb") as f:
    loaded_stats = pickle.load(f)

print("Loaded stats:", loaded_stats)
print("Summary saved to minutes.txt and club_stats.pkl")