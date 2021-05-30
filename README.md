# assistant-skill-chess

[![GitHub License](https://img.shields.io/github/license/mosure/assistant-skill-chess)](https://raw.githubusercontent.com/mosure/assistant-skill-chess/main/LICENSE)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/mosure/assistant-skill-chess)](https://github.com/mosure/assistant-skill-chess)
[![GitHub Issues](https://img.shields.io/github/issues/mosure/assistant-skill-chess)](https://github.com/mosure/assistant-skill-chess/issues)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/mosure/assistant-skill-chess.svg)](http://isitmaintained.com/project/mosure/assistant-skill-chess "Average time to resolve an issue")

webex assistant chess skill

![Image of Chess](docs/start.png)

## Flows
In these flows, `UI-SDK` is the client.
### Normal Flow
![Normal Flow](docs/flows-Normal%20Flow.svg)

### Command Flow
![Command Flow](docs/flows-Command%20Flow.svg)

## TODO
These are future tasks slated for v2 of the experience.

### PVP Games
Requires websocket skill <-> frontend to receive async player moves (or similar).

### Skill session timeout

When the assistant goes off the screen, the current session/`dialogue_id` is lost. The skill service needs to automatically resume sessions (based on `user_id` if available) or the assistant needs to keep `dialogue_id` while a web view is visible.

### Create a better frontend communication library
Create a library around passing data into skill UI's.

## Sources
[Algebraic Notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) as a way of representing moves.

[chessboard.js](https://chessboardjs.com/) as a chessboard UI framework.

[chess.js](https://github.com/jhlywa/chess.js) as a chess logic library.

[Forsyth-Edwards Notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) as a way of representing game state.

[lichess.org API](https://lichess.org/api) as a chess backend.
