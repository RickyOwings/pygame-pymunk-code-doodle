from typing import Callable


class GameObject:
    def __init__(self):
        instances.append(self)

    def update(self, time: float):
        """INSERT WHATEVER"""

    def draw(self):
        """INSERT WHATEVER"""

instances: list[GameObject] = []

def drawAllGO():
    for obj in instances:
        obj.draw()

def updateAllGO(time: float):
    for obj in instances:
        obj.update(time)