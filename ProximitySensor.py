"""This is the ProximitySensor Demo class"""

class ProximitySensor: 
    def __init__(self, detection, rotator) -> None:
        self.detection = detection
        self.rotator = rotator
    def scan(self):
        print("Scanning area to detect obstacles")
    def halt(self):
        print("Halt movement obstacle detected")
    def alert(self):
        print("Warning: approaching obstacle")