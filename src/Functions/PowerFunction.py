from src.Functions.AbstractFunction import AbstractFunction


class PowerFunction(AbstractFunction):

    def getTitle(self) -> str:
        return 'PowerFunction'

    def find(self, x: float) -> float:
        return self.a * pow(x, self.b)

    def getStringFunction(self) -> str:
        return f'{self.a} * x^{self.b}'
