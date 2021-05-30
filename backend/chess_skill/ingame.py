from .root import app
from .util import get_game, frontend_update


@app.handle(intent='castle')
def castle(request, responder):
    game = get_game(request, responder)

    castle_move = None

    if game.is_move_valid(castle_move):
        responder.reply('castling...')
    else:
        responder.reply('Cannot castle...')

    frontend_update(request, responder)


@app.handle(intent='forfeit')
def forfeit(request, responder):
    get_game(request, responder).forfeit()

    responder.reply('forfeiting...')

    frontend_update(request, responder)


@app.handle(intent='move')
def move(request, responder):
    game = get_game(request, responder)

    move = None  # TODO: get move string from request

    if game.is_move_valid(move):
        responder.reply('moving...')
    else:
        responder.reply('invalid move...')

    frontend_update(request, responder)


@app.handle(intent='pawn_promote')
def pawn_promote(request, responder):
    game = get_game(request, responder)

    pawn_promotion = None

    if game.is_move_valid(pawn_promotion):
        responder.reply('promoting pawn...')
    else:
        responder.reply('cannot promote pawn...')

    frontend_update(request, responder)


@app.handle(intent='undo')
def undo(request, responder):
    game = get_game(request, responder)

    if game.is_undo_valid():
        responder.reply('undoing...')
    else:
        responder.reply('cannot undo right now...')

    frontend_update(request, responder)
