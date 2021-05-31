from .root import app
from .util import frontend_update


@app.handle(intent='castle')
def castle(request, responder):
    castle_move = None

    responder.reply('castling...')

    frontend_update(request, responder)


@app.handle(intent='forfeit')
def forfeit(request, responder):
    responder.reply('forfeiting...')

    frontend_update(request, responder)


@app.handle(intent='move')
def move(request, responder):
    locations = _get_locations(request)
    pieces = _get_pieces(request)

    if len(locations) == 2:
        _move_location_to_location(request, responder, from_pos=locations[0], to_pos=locations[1])
    elif len(pieces) == 2:
        _move_piece_to_piece(request, responder, from_piece=pieces[0], to_piece=pieces[1])
    elif len(pieces) == 1 and len(locations) == 1:
        _move_piece_and_location(request, responder, piece=pieces[0], location=locations[0])
    elif len(pieces) == 1 and len(locations) == 0:
        responder.reply('specify a target location.')
    elif len(pieces) == 0 and len(locations) == 1:
        responder.reply('specify a target location.')
    else:
        responder.reply('specify a piece to move.')

    responder.listen()


@app.handle(intent='pawn_promote')
def pawn_promote(request, responder):
    pawn_promotion = None

    responder.reply('promoting pawn...')

    frontend_update(request, responder)


@app.handle(intent='undo')
def undo(request, responder):
    _move(request, responder, 'undo')


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



def _move(request, responder, algebraic_notation):
    """
    Handle a dirty move.
    """

    responder.reply(f'move: {algebraic_notation}')
    frontend_update(request, responder, algebraic_notation)

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

    if piece['text'].upper() == 'KNIGHT':
        # K is taken by king
        piece_letter = 'N'

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
