import random
import string

from backend.chess_service import ChessGame, get_game

from .constants import GAME_ID_KEY, GAME_ID_LENGTH
from .root import app
from .util import frontend_update


@app.handle(intent='new')
def new_game(request, responder):
    """
    Start a new game.

    Options:
        - CPU difficulty

    Future:
        - Allow PVP games
    """

    difficulty = None
    game_id = None

    game = _new_game(request, responder)

    responder.reply('new game...')

    frontend_update(request, responder)


@app.handle(intent='resume')
def resume_game(request, responder):
    """
    Resume an existing game.

    Options:
        - Last played game (based on user_id)
    """
    # TODO: this needs to take the user_id and get the last game_id

    responder.reply('resuming game...')

    frontend_update(request, responder)


def _new_game(request, responder) -> ChessGame:
    game_id = ''.join(random.choices(string.ascii_uppercase, k=GAME_ID_LENGTH))
    responder.frame[GAME_ID_KEY] = game_id

    return get_game(game_id)
