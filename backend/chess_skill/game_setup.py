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

    difficulty = None  # TODO: add difficulty entity
    starting_side = None  # TODO: add starting side (black/white)

    responder.reply('new game...')

    frontend_update(request, responder, command='new', difficulty=difficulty)


@app.handle(intent='resume')
def resume_game(request, responder):
    """
    Resume an existing game.

    Options:
        - Last played game (based on user_id)
    """
    # TODO: this needs to take the user_id and get the last game_id

    responder.reply('resuming game...')

    frontend_update(request, responder, game_id='{OLD GAME_ID}', command='resume')
