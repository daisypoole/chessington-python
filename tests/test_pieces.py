from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn
from chessington.engine.pieces import Rook
from chessington.engine.pieces import Bishop

class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(6, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves

    @staticmethod
    def test_white_rook_can_move_up_board():

        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(0, 0)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(4, 0) in moves

    @staticmethod
    def test_white_rook_cannot_move_if_white_piece_in_front():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(0, 0)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(1, 0)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(1, 0) not in moves

    @staticmethod
    def test_white_rook_cannot_move_if_white_piece_4_spaces_in_front():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(0, 0)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(4, 0)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(1, 0) in moves
        assert Square.at(2, 0) in moves
        assert Square.at(3, 0) in moves
        assert Square.at(4, 0) not in moves
        assert Square.at(5, 0) not in moves

    @staticmethod
    def test_white_rook_can_take_piece_if_black_piece_in_front():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(0, 0)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(1, 0)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(1, 0) in moves
        assert Square.at(2, 0) not in moves



    @staticmethod
    def test_rook_can_move_laterally():

        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(2, 5)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        expected_moves = [
            Square.at(2, 0), Square.at(2, 1), Square.at(2, 2), Square.at(2, 3), Square.at(2, 4), Square.at(2, 6), Square.at(2, 7),
            Square.at(0, 5), Square.at(1, 5), Square.at(3, 5), Square.at(4, 5), Square.at(5, 5), Square.at(6, 5), Square.at(7, 5)
        ]
        assert len(moves) == len(expected_moves)
        assert set(moves) == set(expected_moves)

    @staticmethod
    def test_bishop_can_move_diagonally():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(3, 5)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        expected_moves = [
            Square.at(0, 2), Square.at(1, 3), Square.at(2, 4), Square.at(4, 6), Square.at(5, 7),
            Square.at(1, 7), Square.at(2, 6), Square.at(4, 4), Square.at(5, 3), Square.at(6, 2), Square.at(7, 1)
        ]
        assert len(moves) == len(expected_moves)
        assert set(moves) == set(expected_moves)

    @staticmethod
    def test_bishop_can_capture_enemy_pieces():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(3, 5)
        board.set_piece(square, bishop)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(5, 7)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert enemy_square in moves

    @staticmethod
    def test_bishop_is_blocked_by_enemy_pieces():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(3, 5)
        board.set_piece(square, bishop)

        enemy = Pawn(Player.BLACK)
        enemy_square = Square.at(5, 3)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(6, 2) not in moves

    @staticmethod
    def test_bishop_cannot_capture_friendly_pieces():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(3, 5)
        board.set_piece(square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(5, 3)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert friendly_square not in moves

    @staticmethod
    def test_bishop_is_blocked_by_friendly_pieces():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(3, 5)
        board.set_piece(square, bishop)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(5, 3)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(6, 2) not in moves
        assert Square.at(7, 7) not in moves



