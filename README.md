# Keenan's Flask Blog

This Flask blog was my first experimentation with web design and deployment. I originally built this webapp in December 2020, but made significant updates in the fall of 2021. The core components of the app consist of:
* Flask web server
* Dynamic HTML templates with Jinja
* Bootstrap CSS
* SQLite database with SQLAlchemy 
* Password Authentication with BCrypt hashing
* Linux deployment on a Linode server
* My first experience with Git :)

I took a lot of inspiration from [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo) and [Tech with Tim](https://www.youtube.com/@TechWithTim) who both helped me learn web design. I've used some of their code snippets but have tried to make the website my own as much as possible.

## Installation

The app should support all versions of python. It is productionalized on Python 3.9.

```bash
pip install -r requirements.txt
```
```bash
python run.py
```
Once launched, Flask will run on local port 5000 by default.


## License

[MIT](https://choosealicense.com/licenses/mit/)