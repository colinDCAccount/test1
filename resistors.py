"""
Colin Innes (100834391)
resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 202x Test 1
"""

class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)


### DEFINE class VariableResistor HERE ###
class VariableResistor(Resistor):
    """Model a variable resistor that can be set as a percentage of its max value."""

    def __init__(self, max_resistance):
        """Constructor sets the maximum resistance in ohms."""
        super().__init__(max_resistance)
        self.max_resistance = max_resistance

    def set_resistance(self, percent):
        """Set the resistance as a percent (0–100%) of max resistance."""
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.resistance = self.max_resistance * (percent / 100.0)

    def __str__(self):
        """Return a string showing both current and max resistance."""
        return f"R={self.resistance:.1f} (max={self.max_resistance:.1f})"


if __name__ == "__main__":
    r1 = Resistor(1000.0)
    print("R1:", r1)
    print("R1: voltage=12.0, current=", r1.current(12.0))

    ## UNCOMMENT THIS BLOCK TO TEST VariableResistor
    r2 = VariableResistor(1000.0)
    print("R2:", r2)
    print("R2 100%: voltage=12.0, current=", r2.current(12.0))
    r2.set_resistance(50.0)
    print("R2 50%: voltage=12.0, current=", r2.current(12.0))

