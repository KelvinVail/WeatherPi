class Stack:
    def __init__(self, displays):
        self.displays = displays

    def display(self, value):
        for display in self.displays:
            display.display(value)
