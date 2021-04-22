from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import toFixed


class PowerFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'PowerFunction'

    def find(self, x: float) -> float:
        return self.a * pow(x, self.b)

    def getStringFunction(self) -> str:
        return f'{toFixed(self.a)} * x^{toFixed(self.b)}'
