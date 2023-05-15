# Define TV class
class TV:
    # constructor attributes of an TV object
    def __init__(self):
        self.channel = 1        # sets initial channel to 1
        self.volumeLevel = 1    # sets initial volume to 1
        self.on = False         # sets initial on to False if TV is initially turned off
    

    # a method that returns True when TV is on
    def turnOn(self):
        self.on = True

    # a method that returns False when TV is off
    def turnOff(self):
        self.on = False
    
    # a method that returns the current channel
    def getChannel(self):
        return self.channel
    
    # a method that sets new channel
    def setChannel(self, channel):
        pass

    # a method that returns the current volume
    def getVolume(self):
        pass
    
    # a method that sets new volume level
    def setVolume(self):
        pass

    # a method that increments channel number by 1
    def channelUp(self):
        pass

    # a method the decrements channel number by 1
    def channelDown(self):
        pass

    # a method that increments volume level by 1
    def volumeUp(self):
        pass

    # a method the decrements volume level by 1
    def volumeDown(self):
        pass