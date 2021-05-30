from .root import app
from .util import get_game


@app.handle(intent='castle')
def castle(request, responder):
    responder.reply('castling...')


@app.handle(intent='forfeit')
def forfeit(request, responder):
    responder.reply('forfeiting...')


@app.handle(intent='move')
def move(request, responder):
    move = None  # TODO: get move string from request

    game = get_game(request, responder)

    if game.is_move_valid(move):
        responder.reply('moving...')
    else:
        responder.reply('invalid move...')


@app.handle(intent='pawn_promote')
def pawn_promote(request, responder):
    responder.reply('promoting pawn...')


@app.handle(intent='undo')
def undo(request, responder):
    game = get_game(request, responder)

    if game.is_undo_valid():
        responder.reply('undoing...')
    else:
        responder.reply('cannot undo right now...')
