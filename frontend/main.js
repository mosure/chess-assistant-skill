function saveBoard(fen) {
    localStorage.setItem('board-1', fen);
    console.log('board-1 saved: ' + fen);
}

function loadBoard() {
    return localStorage.getItem('board-1');
}

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    console.log('Query variable %s not found', variable);
}

function parseHash() {
    hash = window.location.hash;
    //history.pushState(null, null,'#undefined');

    if (hash) {
        hash = hash.substring(1); // Remove #

        if (hash.includes('/') || hash === 'start') {
            return {
                type: 'board',
                fen: hash,
            };
        } else {
            return {
                type: 'move',
                move: hash,
            };
        }
    }

    return undefined;
}

function handleCommand(board, cmd, command_webhook_url, game_id) {
    if (!cmd) {
        return;
    }

    if (cmd.type === 'board') {
        board.position(cmd.fen);
    } else if (cmd.type === 'move') {
        board.move(cmd.move);

        if (command_webhook_url) {
            var request = $.post(command_webhook_url, {
                game_id: game_id,
                move: cmd.move,
            }, (response) => {
                if (response) {
                    console.log('received update from webhook');
                    console.log(response);

                    // TODO: parse webhook response for opponent move
                    //       consider win states

                    if (response.move) {
                        board.move(response.move);
                    }
                }
            }, 'json');

            request.done(() => {
                console.log('sent move to webhook');
            }).fail(() => {
                console.log('failed to communicate with webhook');
            });
        }
    }

    saveBoard(board.fen());
};


var command_webhook_url = getQueryVariable('command_webhook_url');
if (command_webhook_url) {
    console.log('Command Webhook URL: ' + command_webhook_url);
}

var game_id = getQueryVariable('game_id');
if (game_id) {
    console.log('Game ID: ' + game_id);
}

var action = parseHash();
var position = action?.fen ?? loadBoard() ?? 'start';

var board = Chessboard('board-1', {
    position: position,
    orientation: 'white',
    moveSpeed: 'slow',
});

window.addEventListener('hashchange', () => {
    handleCommand(board, parseHash(), command_webhook_url, game_id);
}, false);
