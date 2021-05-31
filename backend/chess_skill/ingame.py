from .root import app
from .util import _get_game, frontend_update


@app.handle(intent='castle')
def castle(request, responder):
    if not _is_game_active(request, responder):
        return

    game = _get_game(request, responder)

    castle_move = None

    if game.is_move_valid(castle_move):
        responder.reply('castling...')
    else:
        responder.reply('cannot castle...')

    frontend_update(request, responder)


@app.handle(intent='forfeit')
def forfeit(request, responder):
    if not _is_game_active(request, responder):
        return

    _get_game(request, responder).forfeit()

    responder.reply('forfeiting...')

    frontend_update(request, responder)


@app.handle(intent='move')
def move(request, responder):
    if not _is_game_active(request, responder):
        return

    responder.frame['desired_action'] = 'move'

    locations = _get_locations(request)
    pieces = _get_pieces(request)

    successful = False
    if len(locations) == 2:
        successful = _move_location_to_location(request, responder, from_pos=locations[0], to_pos=locations[1])
    elif len(pieces) == 2:
        successful = _move_piece_to_piece(request, responder, from_piece=pieces[0], to_piece=pieces[1])
    elif len(pieces) == 1 and len(locations) == 1:
        successful = _move_piece_and_location(request, responder, piece=pieces[0], location=locations[0])
    elif len(pieces) == 1 and len(locations) == 0:
        responder.reply('specify a target location.')
    elif len(pieces) == 0 and len(locations) == 1:
        responder.reply('specify a target location.')
    else:
        responder.reply('specify a piece to move.')

    if not successful:
        responder.listen()


@app.handle(intent='pawn_promote')
def pawn_promote(request, responder):
    if not _is_game_active(request, responder):
        return

    game = _get_game(request, responder)

    pawn_promotion = None

    if game.is_move_valid(pawn_promotion):
        responder.reply('promoting pawn...')
    else:
        responder.reply('cannot promote pawn...')

    frontend_update(request, responder)


@app.handle(intent='undo')
def undo(request, responder):
    if not _is_game_active(request, responder):
        return

    game = _get_game(request, responder)

    if game.is_undo_valid():
        responder.reply('undoing...')
    else:
        responder.reply('cannot undo right now...')

    frontend_update(request, responder)


def _get_locations(request):
    """
    Get's the user desired location from the query

    Args:
        request (Request): contains info about the conversation up to this point
        (e.g. domain, intent, entities, etc)

    Returns:
        list(string): resolved locations entity
    """
    return [e for e in request.entities if e['type'] == 'location']

def _get_pieces(request):
    """
    Get's the user desired pieces from the query

    Args:
        request (Request): contains info about the conversation up to this point
        (e.g. domain, intent, entities, etc)

    Returns:
        list(string): resolved pieces entity
    """
    return [e for e in request.entities if e['type'] == 'piece']

def _get_files(request):
    """
    Get's the user desired files from the query

    Args:
        request (Request): contains info about the conversation up to this point
        (e.g. domain, intent, entities, etc)

    Returns:
        list(string): resolved files entity
    """
    return [e for e in request.entities if e['type'] == 'file']

def _get_ranks(request):
    """
    Get's the user desired ranks from the query

    Args:
        request (Request): contains info about the conversation up to this point
        (e.g. domain, intent, entities, etc)

    Returns:
        list(string): resolved ranks entity
    """
    return [e for e in request.entities if e['type'] == 'rank']


def _is_game_active(request, responder):
    game = _get_game(request)

    if game is None:
        return responder.reply('there is no active game.')

    return True


def _move(request, responder, algebraic_notation):
    """
    Handle a dirty move.
    """

    game = _get_game(request)

    (good_from, good_to) = game.is_move_well_defined(move)
    if not good_from or not good_to:
        responder.reply('non-specific move.')
        return False

    if not game.is_move_valid(algebraic_notation=algebraic_notation):
        responder.reply('move is invalid.')
        return False

    responder.reply('move is valid.')
    frontend_update(request, responder)

    return True

def _move_location_to_location(request, responder, from_pos, to_pos):
    move = f'{from_pos}{to_pos}'

    return _move(request, responder, move)

def _move_piece_to_piece(request, responder, from_piece, to_piece):
    # TODO: support this
    # TODO: check for file/rank identifiers

    responder.reply('piece to piece moves are currently not supported.')
    return False

def _move_piece_and_location(request, responder, piece, location):
    piece_letter = piece['text'].upper()[0]
    location_text = location['text'].lower()

    files = _get_files(request)
    ranks = _get_ranks(request)

    if len(files) == 1 and len(ranks) == 1:
        file = files[0]['text']
        rank = ranks[0]['text']
        move = f'{piece_letter}{file}{rank}{location_text}'
    elif len(files) == 1:
        file = files[0]['text']
        move = f'{piece_letter}{file}{location_text}'
    elif len(ranks) == 1:
        rank = ranks[0]['text']
        move = f'{piece_letter}{rank}{location_text}'
    else:
        move = f'{piece_letter}{location_text}'

    return _move(request, responder, move)
