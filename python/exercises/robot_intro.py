class Robot:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def move(self, speed):
        self.speed = speed
        print(f"{self.name} is moving at {self.speed} mph")

    def stop(self):
        self.speed = 0
        print(f"{self.name} has stopped.")



robot = Robot("Rover")

robot.move(2)

print(f"{robot.name} speed: {robot.speed}")