var default_game_difficulty = 4;
var lichess_api_url = 'https://lichess.org/api';
var token = '';

var current_game_id = localStorage.getItem('game_id');
var game = new Chess();

var game_subscription;
var last_move;
var turn_count = 0;

var board = Chessboard('board-1', {
    position: 'start',
    orientation: 'white',
    moveSpeed: 'slow',
});

var $board = $('#board-1');
var squareClass = 'square-55d63';


function postMoveUpdate(from_square, to_square) {
    $board.find('.' + squareClass).removeClass('highlight-check');
    $board.find('.' + squareClass).removeClass('highlight-last-move');

    if (game.game_over()) {
        // handle game over
    } else if (game.in_check()) {
        var turn = game.turn();

        for (var file of 'abcdefgh') {
            for (var rank of '12345678') {
                var square = file + rank;
                var piece = game.get(square);

                if (piece && piece.type === game.KING && piece.color === turn) {
                    $board.find('.square-' + square).addClass('highlight-check');
                }
            }
        }
    }

    if (from_square && to_square) {
        $board.find('.square-' + from_square).addClass('highlight-last-move');
        $board.find('.square-' + to_square).addClass('highlight-last-move');
    }
}

function subscribeToGame() {
    if (game_subscription) {
        clearInterval(game_subscription);
    }

    game_subscription = setInterval(() => {
        api('/board/game/stream/' + current_game_id, 'get', undefined, (res) => {
            var game_moves = res.state.moves.split(' ');

            if (turn_count === game_moves.length) {
                return;
            }
            turn_count = game_moves.length;

            var incoming_move = game_moves.slice(-1)[0];

            if (incoming_move && incoming_move !== last_move) {
                last_move = incoming_move

                console.log('incoming move: ' + incoming_move);

                var move = game.move(incoming_move, { sloppy: true });
                if (!move) {
                    console.log('incoming move is invalid');
                    return;
                }

                console.log(move);

                board.position(game.fen());
                postMoveUpdate(move.from, move.to);
            }
        });
    }, 1000);
}

function setBoardPosition(fen) {
    board.position(fen);
    game.load(fen);
}

function setGameId(game_id) {
    current_game_id = game_id;
    localStorage.setItem('game_id', current_game_id);
}

function api(path, type, data, success) {
    $.ajax({
        url: lichess_api_url + path,
        type: type,
        data: data,
        headers: {
            'authorization': 'Bearer ' + token,
        },
        dataType: 'json',
        success: success,
    });
}

function newGame(difficulty = default_game_difficulty) {
    api('/challenge/ai', 'post', {
        level: difficulty,
        days: 14,
        color: "white",
        //fen: '2k2B1n/2NN3P/1R1p4/p5K1/5P2/4p3/3r1pRp/8 w - - 0 1',
    }, (res) => {
        console.log(res);

        setGameId(res.id);

        setBoardPosition(res.fen);

        subscribeToGame();
    });

    return 'start';
}

function loadGame() {
    // TODO: load game and return initial state (or start a new game if bad game_id)

    return 'start';
}

function doMove(move) {
    var uci = frontend_move(move);
    last_move = uci;

    api('/board/game/' + current_game_id + '/move/' + uci, 'post', undefined, (res) => {
        console.log(res);
    });
}

function parseHash() {
    hash = window.location.hash;
    history.pushState(null, null,'#');

    if (hash) {
        try {
            hash = hash.substring(1); // Remove #
            hash_json = atob(hash)
            return JSON.parse(hash_json)
        } catch {
            return undefined;
        }
    }

    return undefined;
}

function frontendMove(move) {
    var move_res = game.move(move, { sloppy: true });

    if (!move_res) {
        console.log('invalid move');
        return;
    }
    board.position(game.fen());
    postMoveUpdate(move_res.from, move_res.to);

    console.log(move_res);

    var uci = move_res.from + move_res.to;
    return uci;
}

function handleCommand(board, payload) {
    if (!payload) {
        return;
    }

    console.log(payload);

    if (payload.frontend_mode) {
        if (payload.move) {
            frontendMove(payload.move);
        } else if (payload.fen) {
            setBoardPosition(payload.fen);
        }

        return;
    }

    // handle command over move
    if (payload.command) {
        var difficulty = payload.difficulty || default_game_difficulty;

        if (payload.command === 'new') {
            newGame(difficulty);
        }
    } else if (payload.move) {
        doMove(payload.move);
    }
};

newGame();

window.addEventListener('hashchange', () => {
    handleCommand(board, parseHash());
}, false);
