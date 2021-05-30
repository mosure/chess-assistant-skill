

class ChessGame:
    def __init__(self):
        self.id = None

    def is_move_valid(self, algebraic_notation):
        return False

    def move(self, algebraic_notation):
        pass

    def is_undo_valid(self):
        return False

    def undo(self):
        pass

    def forfeit(self):
        pass


class ChessService:
    def start_ai_game(difficulty) -> ChessGame:
        return None

    def get_game(game_id) -> ChessGame:
        return ChessGame()
