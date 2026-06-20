Movie recommendation system — final project
Small CLI demo that uses ideas from Sections 1–6 of the bootcamp: comments, print / input, conditions, lists and loops, functions and main(), files (JSON), try / except on bad input, __str__ on a class, classes/OOP, and composition.

Python 3.10+ (uses | in type hints, e.g. str | None).

**Author**: Zaydalli
**Github Link**: [https://github.com/Zaydalli/movie_recommendation_system]

Run
cd movie_recommendation_system
python main.py

What's where
| Path | Purpose |
|------|---------|
| `main.py` | Menu and entry point |
| `auth.py` | User authentication (Login/Registration) |
| `data_manager.py` | JSON read/write handlers |
| `models.py` | User and Movie OOP classes |
| `movie_manager.py` | CRUD operations, History, Favorites |
| `recommendation.py` | Rating system and Recommendation Engine |
| `utils.py` | Helpers for colored UI and input validation |
| `data/*.json` | Saved application data (users, movies, ratings, favorites, history) |

Menu
Register, Login, Exit.
Once logged in: View All Movies, Search Movies, Get Recommendations, Rate a Movie, My Favorites, Watch History, Admin: Manage Movies, Reports & Statistics, Logout.

Data file
UTF-8 text. JSON formatted files inside the data/ folder for storing users, movies, ratings, favorites, and history. Automatically generated if they don't exist.
