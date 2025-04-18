from gdo.chess.Board import Board
from gdo.chess.Pos import Pos
from gdo.chess.pieces.Piece import Piece


class Pawn(Piece):

    def possible_moves(self, board: Board) -> list[Pos]:
        board.can_move
