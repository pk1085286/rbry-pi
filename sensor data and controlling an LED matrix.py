from sense_hat import SenseHat
import time
import random

sense = SenseHat()

# Define some colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
teal = (0, 255, 255)
orange = (255, 165, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Define some patterns
pattern1 = [
    black, black, black, black, black, black, black, black,
    black, black, black, red, red, black, black, black,
    black, black, red, black, black, red, black, black,
    black, red, black, black, black, black, red, black,
    black, red, black, black, black, black, red, black,
    black, black, red, black, black, red, black, black,
    black, black, black, red, red, black, black, black,
    black, black, black, black, black, black, black, black,
]

pattern2 = [
    black, black, black, black, black, black, black, black,
    black, black, black, yellow, yellow, black, black, black,
    black, black, yellow, black, black, yellow, black, black,
    black, yellow, black, black, black, black, yellow, black,
    black, yellow, black, black, black, black, yellow, black,
    black, black, yellow, black, black, yellow, black, black,
    black, black, black, yellow, yellow, black, black, black,
    black, black, black, black, black, black, black, black,
]

# Set up the LED matrix
sense.clear()

# Define a function to generate random patterns
def random_pattern():
    return [random.choice([black, white]) for i in range(64)]

# Define a function to display a pattern on the LED matrix
def display_pattern(pattern, duration):
    sense.set_pixels(pattern)
    time.sleep(duration)
    sense.clear()

# Define a function to read the temperature and humidity from the Sense HAT sensors
def read_sensors():
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    return round(humidity, 2), round(temp, 2)

# Define a function to display the temperature and humidity on the LED matrix
def display_sensors():
    humidity, temp = read_sensors()
    sense.show_message("Temp: {}C, Humidity: {}%".format(temp, humidity), text_colour=white, back_colour=blue, scroll_speed=0.1)

# Define a main function that runs the project
def main():
    # Display the temperature and humidity
    display_sensors()

    # Display a random pattern for 5 seconds
    display_pattern(random_pattern(), 5)

    # Display pattern 1 for 3 seconds
    display_pattern(pattern1, 3)

    # Display pattern 2 for 3 seconds
    display_pattern(pattern2, 3)

    # Display the temperature and humidity again
    display_sensors()

if __name__ == "__main__":
    main()
