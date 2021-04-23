from src.Functions.AbstractFunction import AbstractFunction
from src.Utils.Utils import toFixed

"""Класс, который сожержит в себе ответ для вывода в консоль"""
class Answer:
    def __init__(self, function: AbstractFunction, measure_of_deviation, standard_deviation) -> None:
        super().__init__()
        self.fun = function
        self.sum = measure_of_deviation
        self.delta = standard_deviation

    def __str__(self) -> str:
        return f'{self.fun.getStringFunction()} | {toFixed(self.fun.a)} | {toFixed(self.fun.b)} | {toFixed(self.fun.c)} | {toFixed(self.sum)} | {toFixed(self.delta)}'
