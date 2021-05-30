from backend.chess_service import ChessGame, ChessService


def get_game(request, responder) -> ChessGame:
    game_id = None  # TODO: get game_id from request context

    return ChessService.get_game(game_id)


def add_commands(request, responder):
    pass


def frontend_update(request, responder, game=None):
    add_commands(request, responder)

    responder.act('display-web-view')

    responder.listen()
