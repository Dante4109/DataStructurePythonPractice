# You have a music player that should be playing a 900 song list randomly.
# You notice that you keep hearing a song being repeated during your drive and
# you are curious if its truly random.

from collections import Counter
import random

r             = random.Random() 
songs         = range(1,900)
unplayed      = set(songs)

# You also keep hitting skip in the hopes a particular song comes up. 
# Write a piece of code that simulates this.  You should tell me three things;
# 1) the number of songs played before a repeat occurs
# 2) how many songs needed to be played before you played them all
# 3) after you succeed in playing them all, how many times has the most common song been played.

counter         = Counter()
firstrepeat     = None
totalplays      = 0

while unplayed:
    song = r.choice(songs)
    unplayed -= set([song])
    if firstrepeat is None and song in counter:
        firstrepeat = len(counter)
    counter[song] += 1
    totalplays += 1

print(f"""
Number of songs played before a repeat:             {firstrepeat}
Total number songs played:                          {totalplays}
Most common song:                                   {counter.most_common()[0][0]}
How many times has the most common song was played: {counter.most_common()[0][1]}
""")

# Sample run
# 
# $ python3 foo.py
# 
# Number of songs played before a repeat:             50
# Total number songs played:                          7263
# Most common song:                                   375
# How many times has the most common song was played: 17