from backend.chess_service import ChessGame, ChessService

from .root import app
from .util import frontend_update


@app.handle(intent='new')
def new_game(request, responder):
    difficulty = None

    game = ChessService.start_ai_game(difficulty=difficulty)

    responder.reply('new game...')

    frontend_update(request, responder)


@app.handle(intent='resume')
def resume_game(request, responder):
    to_load = None


    responder.reply('resuming game...')

    frontend_update(request, responder)
