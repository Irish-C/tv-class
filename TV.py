# Define TV class
class TV:
    # constructor init method for properties of an TV object
    def __init__(self):
        self.channel = 1        # sets initial channel to 1
        self.volumeLevel = 1    # sets initial volume to 1
        self.on = False         # sets initial on to False if TV is initially turned off
    

    # function that returns True when TV is on
    def turnOn(self):
        self.on = True

    # function that return False when TV is off
    def turnOff(self):
        self.on = False
    
    # function that returns the channel
    def getChannel(self):
        return self.channel