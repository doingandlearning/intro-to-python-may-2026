queue = [
    "Fleetwood Mac - The Chain (Live)",
    "Dua Lipa - Training Season",
    "Khruangbin - Time (You and I)",
    "The Smile - Wall of Eyes",
    "Olivia Dean - Dive",
    "LCD Soundsystem - tonite",
    "Jungle - Back On 74",
    "Arlo Parks - Softly (Acoustic)",
    "Bonobo - Kerala",
    "Little Simz - Gorilla",
    "Eminem - 8 Mile"
]

count = len(queue)
total_words = 0
for item in queue:
    artist, title = item.split(" - ")
    total_words += len(title.split())
average_words = total_words / count

print(f"You have {count} tracks in the queue.")
print(f"Average words per title: {average_words:.2f}")

import re
user_word = input("Give me term: ").strip()

pattern = re.compile(r'\b' + re.escape(user_word) + r'\b', re.IGNORECASE)

matches = []
for value in queue:

  if pattern.search(value):
    matches.append(value)
  
print(matches)