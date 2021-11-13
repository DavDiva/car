from config import car_sizes, car_color, car_frame
from math import sin, cos, pi, sqrt, atan2

class Car:
    def __init__(self, position, angle = 0) -> None:
        super().__init__()
        self.position = position
        self.angle = angle

    def update(self):
        self.angle += 0.01

    def draw(self, draw_tool, display):
        gipotenuse = sqrt(self.position[0] * self.position[0] + self.position[1] * self.position[1])
        angle_between = atan2(car_sizes[1], car_sizes[0])
        draw_tool.lines(display, car_color, True,
                        [[self.position[0] + gipotenuse*cos(angle_between + self.angle),
                            self.position[1] + gipotenuse*sin(angle_between + self.angle)],
                         [self.position[0] + gipotenuse * cos(pi - angle_between + self.angle),
                            self.position[1] + gipotenuse * sin(pi - angle_between + self.angle)],
                         [self.position[0] + gipotenuse * cos(angle_between + self.angle + pi),
                            self.position[1] + gipotenuse * sin(angle_between + self.angle + pi)],
                         [self.position[0] + gipotenuse * cos(-angle_between + self.angle),
                            self.position[1] + gipotenuse * sin(-angle_between + self.angle)]],
                        car_frame)