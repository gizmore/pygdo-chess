from gdo.base.WithSerialization import WithSerialization
from gdo.chess.Pos import Pos
from gdo.chess.pieces.Piece import Piece


class Board(WithSerialization):

    _board: list[list[Piece|None]]

    def __init__(self):
        super().__init__()
        self._board = []
        self.reset()

    def reset(self):
        self._board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

    def is_empty(self, pos: Pos) -> bool:
        x = pos.get_x()
        y = pos.get_y()
        if x < 0 or x > 7:
            return False
        if y < 0 or y > 7:
            return False
        return self._board[y][x] is None
