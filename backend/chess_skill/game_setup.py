from .root import app


@app.handle(intent='new')
def new_game(request, responder):
    responder.reply('new game...')


@app.handle(intent='resume')
def resume_game(request, responder):
    responder.reply('resuming game...')
