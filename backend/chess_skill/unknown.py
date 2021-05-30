from .root import app


@app.handle(intent='unknown')
def unknown(request, responder):
    replies = ["Sorry, not sure what you meant there."]
    responder.reply(replies)
