from __future__ import annotations
from typing import NewType, List
from abc import ABC, abstractmethod


Move = NewType('Move', int)

class Piece:
    @property
    def opposite(self) -> Piece:
        raise NotImplementedError("Should be implemented by subclasses.")

class Board(ABC):
    @property
    @abstractmethod
    def turn(self) -> Piece:
        pass

    @abstractmethod
    def move(self, location: Move) -> Board:
        pass

    @property
    @abstractmethod
    def legal_moves(self) -> List[Move]:
        pass

    @property
    @abstractmethod
    def is_win(self) -> bool:
        pass

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    @abstractmethod
    def evaluate(self, player: Piece) -> float:
        pass