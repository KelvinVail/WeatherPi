import microdotphat

class Micro:
    def __init__(self):
        pass

    def display(self, value):
        microdotphat.clear()
        microdotphat.write_string(value, kerning=False)
        microdotphat.show()
