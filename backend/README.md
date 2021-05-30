# Backend

## Assistant Skill
The backend NLP is powered by [mindmeld](https://www.mindmeld.com/).

### Building
Run `python -m backend.chess_skill build` to build the models.

### Converse
Run `python -m backend.chess_skill converse` to interact with the skill.

## Chess Service
Abstraction around chess logic. Dialogue handlers expect methods defined in `chess.py` to be implemented.
