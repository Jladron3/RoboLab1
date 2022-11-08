"""This is the LED Demo class"""

class LED:
    def __init__(self, color, pin) -> None:
        self.color = color #makes color an attrubte 
        self.pin = pin #makes pin an attribute
    def turnOn(self):
        print("Turn the LED on")
    def turnOff(self):
        print("Turn the LED off")