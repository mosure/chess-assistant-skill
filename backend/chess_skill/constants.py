import os


FRONTEND_URL = os.environ.get('FRONTEND_URL')
def frontend_url_with_hash(hash):
    return f'{FRONTEND_URL}#{hash}'
