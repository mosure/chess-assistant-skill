from .root import app


@app.handle(intent='greet')
def greet(request, responder):
    responder.reply('Hello! This is the assistant chess skill.')


@app.handle(intent='exit')
def exit(request, responder):
    responder.reply('Closing assistant chess...')
    responder.act('clear-web-view')
    responder.sleep('')
