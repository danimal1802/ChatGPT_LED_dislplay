# ChatGPT created script to emulate a Star Trek computer panel Original Series
# Runs on a Raspberry Pi with a SenseHat 8x8 multicolor LED panel
# April 2023


import time
import random
from sense_hat import SenseHat

# Create a SenseHat instance
sense = SenseHat()

# Set the rotation of the LED matrix display to 180 degrees
sense.set_rotation(180)

# Function to generate a random color
def random_color():
    return (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

# Function to set each pixel to a random color in a random pattern
def set_random_colors():
    for _ in range(64):  # There are 64 pixels on the LED matrix
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        sense.set_pixel(x, y, random_color())
        time.sleep(0.2)

# Main loop
while True:
    set_random_colors()
