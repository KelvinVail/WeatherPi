import scrollphathd
from scrollphathd.fonts import font5x5

class Scroll:
    def __init__(self):
        pass

    def display(self, value):
        scrollphathd.clear()
        scrollphathd.write_string(
            value,
            x=0, # Align to the left of the buffer
            y=0, # Align to the top of the buffer
            font=font5x5, # Use the font5x5 font we imported above
            brightness=0.3
        )
        scrollphathd.show()
