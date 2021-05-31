def add_commands(request, responder):
    pass


def frontend_update(request, responder, refresh_web_view=True):
    add_commands(request, responder)

    if refresh_web_view:
        responder.act('display-web-view')
