from src.Functions.AbstractFunction import AbstractFunction


class LinearFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'LinearFunction'

    def find(self, x: float) -> float:
        return self.a * x + self.b

    def getStringFunction(self) -> str:
        return f'{self.a}*x^{self.b}'
