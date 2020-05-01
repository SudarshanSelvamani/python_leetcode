class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        summed_value = self.value + other.value
        return Number(summed_value)

    def __repr__(self):
        """Create a decent representation for the output."""
        return "{!s}({!r})".format(self.__class__.__name__, self.value)

a = Number(1)
b = Number(2)

# This line will look for `a.__add__(b)` to do the work:
c = a + b
print(c)