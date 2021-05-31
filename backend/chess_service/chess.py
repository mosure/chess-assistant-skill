class ChessGame:
    def __init__(self, game_id):
        self.game_id = game_id
        self.state = None

    def is_move_valid(self, algebraic_notation):
        """
        Whether or not a move is valid given the current game state.
        """
        return False

    def is_move_well_defined(self, algebraic_notation):
        """
        Whether or not a move is well defined.

        Returns tuple:
            (is_well_defined_from, is_well_defined_to)
        """
        return (False, False)

    def is_undo_valid(self):
        """
        Whether or not the game supports an undo action.
        """
        return False

    def update_board(self, positions):
        """
        Update the board's state.

        positions: can be either JSON or FENe
        """
        pass


games = {}
def get_game(game_id) -> ChessGame:
    global games

    if game_id in games:
        return games[game_id]

    games[game_id] = ChessGame(game_id)
    return games[game_id]
