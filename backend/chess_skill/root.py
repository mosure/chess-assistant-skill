from webex_assistant_sdk import SkillApplication, crypto
import os


secret = 'my-secret-chess-skill_asdfasdf'
path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'chess_skill.id_rsa'))
print(path)

key = crypto.load_private_key_from_file(path)


app = SkillApplication(__name__, secret=secret, private_key=key)


@app.middleware
def add_sleep(request, responder, handler):
    handler(request, responder)
    # ensure response ends with `listen` or `sleep`
    if responder.directives[-1]['name'] not in {'listen', 'sleep'}:
        responder.sleep()

__all__ = ['app']
