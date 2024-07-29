import time
import sys

'''
Z-line fan controller

Inputs
--------------------------
Power button
1 button
2 button
3 button
Timer button
Light button

Outputs
------------------------------------
Seven segement display (1 character) (does it have a dot?)
Fan speed 1
Fan speed 2
Fan speed 3
Light

States
-----------------------------------
Fan speed (0 / 1 / 2 / 3)
Light (on/off)
timer (don't care, setting, counting down)
'''

class Light:
    def __init__(self):
        self.state = False

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def toggle_state(self):
        self.state = not self.state

class Fan:
    def __init__(self):
        self.speed = 0

    def set_speed_0(self):
        self.speed = 0

    def set_speed_1(self):
        self.speed = 1

    def set_speed_2(self):
        self.speed = 2

    def set_speed_3(self):
        self.speed = 3

class Timer:
    ''' Creates a timer with an initial duration in minutes.
        When running, the timer counts down. When it reaches the duration, the timer stops.

        The time remaining is made available to, for example, update a display.
    '''
    def __init__(self, duration):
        self.initial_duration = duration * 60  # Duration in seconds
        self.remaining_time = self.initial_duration
        self.start_time = time.time()

    def update_timer(self):
        ''' Updates the time remaining and performs actions based on remaining time '''
        elapsed_time = time.time() - self.start_time
        self.remaining_time = self.initial_duration - elapsed_time

        if self.remaining_time <= 0:
            self.remaining_time = 0

        return self.remaining_time


def display(remaining_time):
    remaining_seconds = int(remaining_time)
    remaining_minutes = remaining_seconds // 60
    
    if remaining_seconds < 60 and remaining_seconds >= 30:
        display_value = "0."
    elif remaining_seconds < 30:
        display_value = "0"
    else:
        display_value = f"{remaining_minutes}"

    return display_value

def main():
    timer_duration = 2  # Example duration in minutes
    timer = Timer(timer_duration)

    while timer.update_timer() > 0:
        sys.stdout.write(f"\rDisplay: {display(timer.update_timer())}")
        sys.stdout.flush()
        time.sleep(1)

    print("\nTimer has finished.")

if __name__ == "__main__":
    main()
