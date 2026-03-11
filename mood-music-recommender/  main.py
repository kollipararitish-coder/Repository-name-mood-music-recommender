from mood_detector import detect_mood
from songs import songs

print("Mood Based Music Recommender")

user_input = input("How are you feeling today? ")

mood = detect_mood(user_input)

print("\nDetected mood:", mood)
print("\nRecommended songs:")

for song in songs[mood]:
    print("-", song)