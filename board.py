# -*- coding: UTF-8 -*-
from collections import Counter
from functools import reduce
from operator import add
from random import randint


class ReversiException(Exception):
    """Breaking the rules of reversi"""
    pass


class ImmutableError(ReversiException):
    """Trying to change the properties of a ReversiBoard after it's been
    initialized.
    """


_range = range(8)  # cache this range
_coords = [(x, y) for x in _range for y in _range]
_directions = [
    (0, -1), (1, 0), (0, 1), (-1, 0), # up, right, down, left
    (-1, -1), (1, -1), (1, 1), (-1, 1) # nw, ne, se, sw
]


class ReversiBoard:
    """Represents the board of the game.
    None of the methods are destructive, i.e. the board is 'immutable'."""

    def __init__(self, board=None, current=None):
        if board is None:
            # official opening state
            board = [[0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,1,2,0,0,0],
                     [0,0,0,2,1,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0]]

        if current is None:
            current = 1  # white starts

        self.board = board
        self._set_current(current)

    def _set_current(self, current):
        if hasattr(self, '_current'):
            raise ImmutableError("The board already has a current player.")
        self._current = current
        self._not_current = self._invert(current)

    def current(self):
        return self._current  # read only

    def score(self):
        """Return a list with score for white vs black"""
        raise NotImplementedError("This method needs to be implemented")

    def _inside(self, pos):
        """Is a position within the boundaries of the board?"""
        x, y = pos
        return x in _range and y in _range

    def _item(self, pos):
        """Gets the item at a position"""
        x, y = pos
        return self.board[y][x]

    def _search_direction(self, start, direction, look_for):
        """Count how many pieces would be captured in a given direction"""
        raise NotImplementedError("This method needs to be implemented")

    def _invert(self, color):
        """Turns black into white and vice versa"""
        raise NotImplementedError("This method needs to be implemented")

    def valid_move(self, pos):
        """Check if a move is valid or not"""
        raise NotImplementedError("This method needs to be implemented")

    def valid_moves(self):
        """Return a list of valid moves for a player"""
        return [pos for pos in _coords
                if self.valid_move(pos)]

    def _clone_board(self):
        """Returns an exact copy of the board."""
        clone = []
        for y in _range:
            clone.append(list(self.board[y]))
        return clone

    def make_move(self, pos):
        """Makes a move, and returns an updated game."""
        if not self.valid_move(pos):
            raise ReversiException("Invalid move %s" % str(pos))

        # update board
        # turn pieces
        # figure out new player
        raise NotImplementedError("This method needs to be implemented")


    def game_over(self):
        """Check if game is over or not"""
        if len(self.valid_moves()) > 0:
            return False
        # Otherwise, shift to next player
        next_player_board = ReversiBoard(
            self._clone_board(),
            self._not_current)
        if len(next_player_board.valid_moves()) == 0:
            return True
        return False

    def render(self):
        """Creates a beautiful (?) ascii art rendition of the board"""
        pieces = [". ", "\xe2\x97\x8f ", "\xe2\x97\xaf "]
        return "\n".join(
            ["".join(
                [pieces[pos] for pos in row]
            ) for row in self.board]
        )
