import random

# Define the Die class
class Die:

    # Initialize the Die with a given number of sides (default is 6)
    def __init__(self, sides=6):
        self._sides = sides  # Set the number of sides of the die
        self._value = self.roll()  # Roll the die when it is initialized

    # Method to roll the die and return the result
    def roll(self):
        self._value = random.randint(1, self._sides)  # Randomly generate a value between 1 and the number of sides
        return self._value

    # String representation of the Die, returns the current value as a string
    def __str__(self):
        return str(self._value)

    # Less than comparison, used to compare the value of this die with another
    def __lt__(self, other):
        return self._value < other._value

    # Equality comparison, checks if the value of this die is equal to another
    def __eq__(self, other):
        return self._value == other._value

    # Subtraction operator, returns the difference in value between this die and another
    def __sub__(self, other):
        return self._value - other._value





