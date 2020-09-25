"""
Say you need to make ten requests to an API that will return temperature data.
You only want to return results that are greater than 100 degrees Fahrenheit.
Assume that each request will return different data. In this case, there’s no way to use a list comprehension in Python to solve the problem.

The walrus operator solves this problem.
It allows you to run an expression while simultaneously assigning the output value to a variable.
The following example shows how this is possible, using get_weather_data() to generate fake weather data:
"""

import random
def get_weather_data():
    return random.randrange(90, 110)
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)

#O/P: [107, 102, 109, 104, 107, 109, 108, 101, 104]