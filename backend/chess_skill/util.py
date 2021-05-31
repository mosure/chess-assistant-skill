from backend.chess_service import ChessGame, get_game

from .constants import GAME_ID_KEY


def _get_game(request) -> ChessGame:
    if GAME_ID_KEY not in request.frame:
        return None

    return get_game(request.frame[GAME_ID_KEY])


def add_commands(request, responder):
    pass


def frontend_update(request, responder, refresh_web_view=True):
    add_commands(request, responder)

    if refresh_web_view:
        responder.act('display-web-view')
