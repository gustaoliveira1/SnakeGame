from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, position: list[int]) -> None:
        self.position = position

    @abstractmethod
    def render(self) -> None:
        pass