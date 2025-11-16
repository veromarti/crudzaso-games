import time
import os

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print((f"{minutes:02}:{seconds:02}".center(50, "➖")))
    time.sleep(1)
    os.system("cls")

print("TIME'S UP!")