from typing import Type


class Point:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = coordinate_x
        self.y = coordinate_y

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"


class PointCollection(list):

    def append(self, __object: Point) -> None:
        super().append(__object)
