# Go Study

Herein lies the code for the backend of a Django demo application that allows users
to create and view flashcard decks for studying.

The main goal is a quick 'n' easy project to display Django skillz.

## GraphQL

This application exposes a single URL `http://<base-domain>/graphQL/` that allows consumers
to perform a number of queries and mutations.

### Authentication

All authentication is handled with JWT. See https://django-graphql-jwt.domake.io/index.html
for the available queries and mutations.

Additionally, we allow you to query for the current logged-in user with the following:

```text
query {
    currentUser {
        email
    }
}
```

### Flashcards and Decks

We have two available queries, both require the user to be authenticated.

To query for a list of all available flashcard decks, use the following.

```text
query {
    decks {
        title
        description
    }
}
```

To query for a specific deck and get a list of its flashcards, use the following. Make sure
to use the deck's real ID.

```text
query {
    deck(id: <int>) {
        title
        description
        flashcards {
            answer
            question
        }
    }
}
```

## Running Locally

### Installation

Download `conda` (or use an equivalent virtual environment and package installer
combo in place of any conda commands below). Open a Terminal window and run the following:

```commandline
git clone git@github.com:timmycron/go-study.git
cd go-study
conda create --name go-study python=3.10.4
conda activate go-study
pip install -r requirements.txt
python manage.py migrate
```

### Running

Open a Terminal window, change directory into the base project directory
that contains `manage.py`, and run the following:

```commandline
conda activate go-study
python manage.py runserver
```

### Manual Testing

Before executing the `runserver` command above, run `python manage.py loaddata flashcards`.

Open a browser window to http://127.0.0.1:8000/graphql/ and run the queries listed in the 
Flashcards and Decks section.

### Unit Testing

Open a Terminal window, change directory into the base project directory
that contains `manage.py`, and run the following:

```commandline
conda activate go-study
pytest
```

## Development

The `master` branch is our production branch. The `develop` branch is our development branch.
Both of these are protected and should never be pushed to directly.

### Features

To develop a new feature, follow this git flow:

- Create a new feature branch with `git checkout -b f-<some-feature-name>` (e.g. `f-adding-flashcard-model`).
- Implement the feature by making the necessary code changes.
- Push the branch to `github` with `git push --set-upstream f-<same-feature-name>`.
- Use the Github web interface to create a merge request from `f-<same-feature-name>` into `develop`.
- Ensure all tests pass and the code is reviewed and approved by someone supa chill.

### Production

After all features for a release are completed and merged into `develop`, follow this git flow:

- Create a new release branch using the web interface. Name it `r-<date>-<version>` (e.g. `r-20220512-v1.5.3`).
- Perform QA using release branch. Make updates to branch as needed.
- Use the Github web interface to create a merge request from `r-<date>-<version>` into `develop` and
from `r-<date>-<version>` into `master`.
- Ensure all tests pass and the code is reviewed and approved by someone supa chill.
- Merge and ensure the auto deployment is successful.