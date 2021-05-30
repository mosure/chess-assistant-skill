from ..chess_service import ChessGame, ChessService


def get_game(request, responder) -> ChessGame:
    game_id = None  # TODO: get game_id from request context

    return ChessService.get_game(game_id)
