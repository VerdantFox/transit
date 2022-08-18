# Transit

Example project for using the Boston public transit system API.

## Environment

The app has utility scripts written in bash. You will need a shell environment to run those scripts. The standard terminal should work for Mac or Linux. For Windows, I recommend running the scripts in a [Git bash shell](https://www.atlassian.com/git/tutorials/git-bash) or similar.

The app is python. It was written for python 3.10, though it should work for python 3.9 as well. To get started, install python 3.10. Then create and activate a python 3.10 [virtual environment](https://docs.python.org/3/library/venv.html). With an activated python 3.10 virtual environment, pip install the project requirments.

```bash
pip install -r requirements.txt
```

## Running tests

To run tests, you'll need to have an activated python 3.10 virtual environment with the app requirements.txt files pip installed. See [environment](#environment) above for details. With the virtual environment in place, run the script `./utils/pytest.sh` or simply run `pytest .`. To see test coverage run `./utils/pytest-with-coverage.sh`. This will list file coverage to stdout. It will also generate an HTML version of the coverage in `htmlcov` directory. Open `htmlcov/index.html` for a detailed view of test coverage. Note that the app is 100% covered by tests.

## Running the App in development

To run the app in development, you'll need to have an activated python 3.10 virtual environment with the app requirements.txt files pip installed. See [environment](#environment) above for details. To run the app in development mode run `./utils/run-dev.sh` or simply `flask --app main.py --debug run`. Then open a web browser to `http://127.0.0.1:5000` or `localhost:5000`.

## Running static

Transit app files are statically checked for style, bugs, and common security flaws with the `pre-commit` package. You can run those static checkers with `./utils/pre-commit.sh` or by running `pre-commit install` followed by `pre-commit run --all-files`.

## App description

The app is very rudimentary at this point. There are two pages: a "routes" page and a "stops" page. The "routes" page lists all routes in the Boston mass transit API. The "stops" page lists all stops in the the API. You can click any route from the "routes" page to get a list of stops that touch that route. This is achieved with a "route" query parameter against the "stops" page. You can click any stop in the "stops" page to get a list of routes that stop at that stop. This is achieved with a "stop" query parameter against the "routes" page.

## TODOs

I stopped this app short of its potential due to time constraints. With more time I would like to make at least the following changes:

- Add sort and search capabilities to the tables in the existing pages
- Add a "schedules" page where the user can get schedule information for a given route
- Add Google Maps interface where the user could see route and stop information visually
