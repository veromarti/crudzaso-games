import time
import os
import threading
from playsound3 import playsound

my_time = 0
running = False
paused_display = False
last_displayed_time = -1

def start_timer(seconds):
    global my_time, running, last_displayed_time
    my_time = seconds
    running = True
    last_displayed_time = -1
    
    sound_thread = threading.Thread(target=lambda: playsound('unused/Audio4.wav'))
    sound_thread.start()
    count_thread = threading.Thread(target=count)
    count_thread.start()
    
    display_thread = threading.Thread(target=auto_display)
    display_thread.start()
    
    return count_thread, display_thread

def count():
    global my_time, running
    while running and my_time > 0:
        time.sleep(1)
        my_time -= 1

def auto_display():
    """Automatically update display every second"""
    global running, last_displayed_time
    while running and my_time > 0:
        if my_time != last_displayed_time:
            last_displayed_time = my_time
        time.sleep(1)

def display_time():
    """Continuously display time using while loop"""
    global running, paused_display
    while running and my_time > 0:
        if not paused_display:
            print_time()
        time.sleep(0.5)

def pause_display():
    global paused_display
    paused_display = True
    print() 

def resume_display():
    global paused_display
    paused_display = False

def stop_timer():
    global running
    running = False

def show_time():
    seconds = my_time % 60
    minutes = int(my_time / 60) % 60
    return f"{minutes:02}:{seconds:02}"

def print_time():
    print(f"⏱️  Time: {show_time()}".center(30, "➖"))


if __name__ == "__main__":
    my_time = int(input("Enter the time in seconds: "))

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        print((f"{minutes:02}:{seconds:02}".center(50, "➖")))
        time.sleep(1)
        os.system("cls")

    print("TIME'S UP!")