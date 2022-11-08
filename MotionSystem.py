"""This is the MotionSystem Demo Class"""

class MotionSystem:
    def __init__(self, armJoints, wheels, radioChip, manipulator, legs) -> None:
        self.armJoints = armJoints
        self.wheels = wheels
        self.radiochip = radioChip
        self.manipulator = manipulator
        self.legs = legs
    def receiveInput(self):
        print("Receiving motion input from RadioController")
    def forward(self):
        print("Move forward")
    def backward(self):
        print("Move backward")
    def left(self):
        print("Shift Left")
    def right(self):
        print("Shift Right")
    def turnClockwise(self):
        print("Turning Clockwise")
    def turnCounterClockwise(self):
        print("Turning CounterClockwise")
    def pickUp(self):
        print("Pick up object")
    def release(self):
        print("Release object")
    def drop(self):
        print("Drop Object")