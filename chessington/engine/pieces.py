"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square
from abc import ABC, abstractmethod

BOARD_MAX = 7
BOARD_MIN = 0

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):

            chessPiece = []
            white = self.player == Player.WHITE
            currentP = board.find_piece(self)

            if white:
                if currentP.row == BOARD_MAX:
                    return []

                squareone = Square.at(currentP.row + 1, currentP.col)
                if board.get_piece(squareone) is None:
                    chessPiece.append(Square.at(currentP.row + 1, currentP.col))

                    if currentP.row == 1 and board.get_piece(Square.at(currentP.row+2, currentP.col)) is None:
                        chessPiece.append(Square.at(currentP.row+2, currentP.col))

                if currentP.col + 1 <= BOARD_MAX:
                    capturedPiece = board.get_piece(Square.at(currentP.row + 1, currentP.col + 1))
                    if capturedPiece and capturedPiece.player == Player.BLACK:
                        chessPiece.append(Square.at(currentP.row + 1, currentP.col + 1))
                if currentP.col - 1 >= BOARD_MIN:
                    capturedPiece = board.get_piece(Square.at(currentP.row + 1, currentP.col - 1))
                    if capturedPiece and capturedPiece.player == Player.BLACK:
                        chessPiece.append(Square.at(currentP.row + 1, currentP.col - 1))

            else:
                if currentP.row == BOARD_MIN:
                    return []

                squareone = Square.at(currentP.row - 1, currentP.col)
                if board.get_piece(squareone) is None:
                    chessPiece.append(Square.at(currentP.row - 1, currentP.col))

                    if currentP.row == 6 and board.get_piece(Square.at(currentP.row - 2, currentP.col)) is None:
                        chessPiece.append(Square.at(currentP.row - 2, currentP.col))

                if currentP.col + 1 <= BOARD_MAX:
                    capturedPiece = board.get_piece(Square.at(currentP.row - 1, currentP.col + 1))
                    if capturedPiece and capturedPiece.player == Player.WHITE:
                        chessPiece.append(Square.at(currentP.row - 1, currentP.col + 1))
                if currentP.col - 1 >= BOARD_MIN:
                    capturedPiece = board.get_piece(Square.at(currentP.row - 1, currentP.col - 1))
                    if capturedPiece and capturedPiece.player == Player.WHITE:
                        chessPiece.append(Square.at(currentP.row - 1, currentP.col - 1))

            return chessPiece


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        castleUp = []
        castleDown = []

        white = self.player == Player.WHITE
        currentP = board.find_piece(self)

        if white:
            #squareone = Square.at(currentP.row + 1 and currentP.row+6, currentP.col)
            #if board.get_piece(squareone) is None:

            castleUp.append(Square.at(currentP.row+1, currentP.col))
            castleDown.append(Square.at(currentP.row, currentP.col+1))
            castleUp.append(Square.at(currentP.row+2, currentP.row))
            castleDown.append(Square.at(currentP.row, currentP.col + 2))
            castleUp.append(Square.at(currentP.row+3, currentP.row))
            castleDown.append(Square.at(currentP.row, currentP.col + 3))
            castleUp.append(Square.at(currentP.row+4, currentP.col))
            castleDown.append(Square.at(currentP.row, currentP.col + 4))
            castleUp.append(Square.at(currentP.row+5, currentP.col))
            castleDown.append(Square.at(currentP.row, currentP.col + 5))
            castleUp.append(Square.at(currentP.row+6, currentP.col))
            castleDown.append(Square.at(currentP.row, currentP.col + 6))


        else:
            castleUp.append(Square.at(currentP.row-1, currentP.col))
            castleUp.append(Square.at(currentP.row-2, currentP.col))
            castleUp.append(Square.at(currentP.row-3, currentP.col))
            castleUp.append(Square.at(currentP.row-4, currentP.col))
            castleUp.append(Square.at(currentP.row-5, currentP.col))
            castleUp.append(Square.at(currentP.row-6, currentP.col))

        castle = castleUp + castleDown

        return castle


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []