from gdo.base.WithSerialization import WithSerialization
from gdo.chess.Board import Board
from gdo.chess.Pos import Pos


class Piece(WithSerialization):

    BLACK = 1
    WHITE = 2

    _pos: Pos
    _color: int

    __slots__ = ('_pos', '_color')

    def __init__(self):
        self._pos = Pos()
        self._color = 0

    def pos(self, x: int, y: int):
        self._pos._x = x
        self._pos._y = y
        return self

    def black(self):
        self._color = self.BLACK
        return self

    def white(self):
        self._color = self.WHITE
        return self

    ##########
    # Engine #
    ##########
    def possible_moves(self, board: Board) -> list[Pos]:
        return []
