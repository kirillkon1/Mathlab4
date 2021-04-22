import numpy as np

from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import toFixed


class LogarithmicFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'LogarithmicFunction'

    def find(self, x: float) -> float:
        return self.a * np.log(x) + self.b

    def getStringFunction(self) -> str:
        return f'{toFixed(self.a)}*ln(x) + {toFixed(self.b)}'
