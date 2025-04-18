from gdo.base.WithSerialization import WithSerialization


class Pos(WithSerialization):

    _x: int
    _y: int

    _taking: bool

    COLS = { 0: 'X', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H' }

    def __init__(self):
        self._x = 0
        self._y = 0
        self._taking = False

    def get_x(self):
        return self._x - 1

    def get_y(self):
        return self._y - 1

    def render(self):
        return f"{self.COLS[self._x]}{self._y}"
