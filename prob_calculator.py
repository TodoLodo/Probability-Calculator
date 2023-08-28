import copy
import random
from typing import Any
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.__balls: dict = kwargs

    @property
    def balls(self) -> dict:
        return self.__balls
    
    @property
    def contents(self) -> list[str]:
        re = []
        for key in self.balls:
            if self.balls[key]:
                l = [key]*self.balls[key]
                re.extend(l)
        return re
    
    def __remove(self, color) -> str:
        self.__balls[color] -= 1
        return color
    
    def draw(self, count: int) -> list[str]:
        re = []
        for _ in range(count):
            try:
                re.append(self.__remove(random.choice(self.contents)))
            except IndexError:
                pass
        return re

def tester(f):
    print(f)
    return f

def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments
