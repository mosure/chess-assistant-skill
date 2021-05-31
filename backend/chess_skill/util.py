import base64
import json

from .constants import frontend_url_with_hash


def add_commands(request, responder):
    pass


def frontend_update(request, responder, move=None, game_id=None, difficulty=None, command=None):
    """
    Update the frontend with different actions based on params...

    move - specifies ingame moves (e.g. Ke5, undo, forfeit, ...)
    difficulty - AI difficulty 1-8
    command - 'new' if a new game
    """

    add_commands(request, responder)

    hash_payload = {
        'command': command,
        'difficulty': difficulty,
        'move': move,
    }

    hash_payload_str = json.dumps({k: v for k, v in hash_payload.items() if v is not None})
    hash_payload_base64 = base64.b64encode(hash_payload_str.encode('ascii')).decode('ascii')

    responder.act('display-web-view', {
        'url': frontend_url_with_hash(hash_payload_base64),
    })
    print(frontend_url_with_hash(hash_payload_base64))
