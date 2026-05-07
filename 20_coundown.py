# import os #for alarm sound! for its alternative
import subprocess

import time
# Inside this time module, there is a useful function called sleep().
# The parameter is in seconds: time.sleep(seconds)
# time.sleep(seconds) pauses the program for the given number of seconds.
# time.sleep(3)  # Waits 3 seconds before executing the code below.

# for i in range (1, 6): # 1 2 3 4 5 
# for i in reversed(range (1, 6)):
for i in range (5, 0, -1): # as this time i am usign step to reverse so i set stat = 5, end = 0, step = -1 , so backward
    time.sleep(1)
    print(f"{i}", end=" ")
print()
print("Time's up!")
# 5 4 3 2 1  
# Time's up!

print("\nlets Make a clock!")
t = int(input("Enter time in seconds: "))
for i in range(t, -1, -1):
    seconds = i % 60 # finding after a full minutes how many seconds left
    # minutes = int(i/60) % 60 # i/60 = how many minutes(converts seconds to minute), then % 60 for below 1hour how many minutes
    # hour = int(i / 3600) #converts seconds to hours, 1hour = 3600sec
    # better methods: using floor division // insted of int()
    minutes = (i // 60) % 60
    hours = i // 3600    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Alarm Sound!")
subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

# if we use os then,
# os.system("afplay /System/Library/Sounds/Glass.aiff") # ✅
# Some built-in Mac sounds:  # Glass
    # os.system("afplay /System/Library/Sounds/Ping.aiff") # Ping
    # os.system("afplay /System/Library/Sounds/Pop.aiff")  # Pop
    # os.system("afplay /System/Library/Sounds/Hero.aiff") # Hero
    # os.system("afplay /System/Library/Sounds/Funk.aiff") # Funk
    # os.system("afplay /System/Library/Sounds/Tink.aiff") # Tink

# 20.wav should be inside same folder where this code is
# os.system("afplay 20.wav") # this full audio will play after that the next line will execute
#lets play a sound!