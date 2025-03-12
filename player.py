from die import Die  # Assuming Die class is in a separate file named die.py

class Player:
    """Represents a player with three dice and a scoring system."""

    def __init__(self):
        """Initialize a player with three dice and 0 points."""
        self._dice = sorted([Die(), Die(), Die()])  # Create and sort dice
        self._points = 0  # Start with 0 points

    @property
    def points(self):
        """Return the player's points."""
        return self._points

    def roll_dice(self):
        """Roll all dice and sort them."""
        for die in self._dice:
            die.roll()  # Roll each die
        self._dice.sort()  # Sort them again

    def has_pair(self):
        """Check if there is a pair. Increase points if true."""
        if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False

    def has_three_of_a_kind(self):
        """Check if all three dice have the same value. Increase points if true."""
        if self._dice[0] == self._dice[1] == self._dice[2]:  # All three match
            self._points += 3
            return True
        return False

    def has_series(self):
        """Check if the dice form a sequence. Increase points if true."""
        if (self._dice[1] - self._dice[0] == 1) and (self._dice[2] - self._dice[1] == 1):
            self._points += 2
            return True
        return False

    def __str__(self):
        """Return a string representation of the dice."""
        return f"D1={self._dice[0]}, D2={self._dice[1]}, D3={self._dice[2]}"