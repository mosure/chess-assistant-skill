# assistant-skill-chess
webex assistant chess skill

![Image of Chess](docs/start.png)

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
