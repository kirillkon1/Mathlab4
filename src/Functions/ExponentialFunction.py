import math

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import toFixed


class ExponentialFunction(AbstractFunction):

    def __init__(self) -> None:
        super().__init__()

    def getTitle(self) -> str:
        return 'ExponentialFunction'

    def find(self, x: float) -> float:
        return self.a * pow(math.e, self.b * x)

    def getStringFunction(self) -> str:
        return f'{toFixed(self.a)}*e^{toFixed(self.b)}x'
