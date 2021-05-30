

class ChessGame:
    def __init__(self):
        self.id = None  # TODO: populate the ID with lichess ID

    def is_move_valid(self, algebraic_notation):
        pass

    def move(self, algebraic_notation):
        pass

    def is_undo_valid(self):
        pass

    def undo(self):
        pass


class ChessService:
    def start_ai_game(difficulty) -> ChessGame:
        return None

    def get_game(game_id) -> ChessGame:
        return None
