"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start = start
        self.count = 0
    
    def __repr__(self):
        return f'Current number is {self.start}. Current count is {self.count}'

    def reset(self):
        """Reset the number to the initial start"""
        self.start = self.start-self.count
        self.count = 0

    def generate(self):
        """Increment the number

        Count how many times it has incremented
        """
        self.start += 1
        self.count += 1
        return self.start-1
