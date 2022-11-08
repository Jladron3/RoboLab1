"""This is the Camera Demo Class"""

class Camera:
    def __init__(self, lens, flash) -> None:
        self.lens = lens
        self.flash = flash
    def capture(self):
        print("Capture Photo")
    def openLens(self):
        print("Open camera lens")
    def closeLens(self):
        print("Close camera lens")