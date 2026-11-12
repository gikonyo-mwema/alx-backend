# 0x02. i18n

This project progressively adds Flask-Babel internationalization, locale
selection, translated templates, and user-aware settings.

## Tasks

| Task | Flask app | Template |
| --- | --- | --- |
| 0. Basic Flask app | [0-app.py](./0-app.py) | [0-index.html](./templates/0-index.html) |
| 1. Basic Babel setup | [1-app.py](./1-app.py) | [1-index.html](./templates/1-index.html) |
| 2. Get locale from the request | [2-app.py](./2-app.py) | [2-index.html](./templates/2-index.html) |
| 3. Parametrize templates | [3-app.py](./3-app.py) | [3-index.html](./templates/3-index.html) |
| 4. Force a locale with URL parameters | [4-app.py](./4-app.py) | [4-index.html](./templates/4-index.html) |
| 5. Mock logging in | [5-app.py](./5-app.py) | [5-index.html](./templates/5-index.html) |
| 7. Infer a user’s locale | [7-app.py](./7-app.py) | [7-index.html](./templates/7-index.html) |
| Final app | [app.py](./app.py) | [index.html](./templates/index.html) |

The repository does not contain task 6 files. Shared Babel settings are in
[babel.cfg](./babel.cfg).
