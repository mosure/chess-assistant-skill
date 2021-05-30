# assistant-skill-chess
webex assistant chess skill

![Image of Chess](docs/start.png)

## Backend
### Assistant Skill
The backend NLP is powered by [mindmeld](https://www.mindmeld.com/).

### Chess Service
Abstraction around chess logic. Dialogue handlers expect methods defined in `chess.py` to be implemented.

## Frontend
Frontend code runs on the edge device to display the game state.

## Flows
In these flows, `UI-SDK` is assistant edge client code.
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
