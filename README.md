# Go Study

Herein lies the code for the backend of a Django demo application that allows users
to create and view flashcard decks for studying.

The main goal is a quick 'n' easy project to display Django skillz.

## Setup

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

## Running

Open a Terminal window, change directory into the base project directory
that contains `manage.py`, and run the following:

```commandline
conda activate go-study
python manage.py runserver
```

## Manual Testing

Before executing the `runserver` command above, run `python manage.py loaddata flashcards`.

Open a browser window to http://127.0.0.1:8000/graphql/ and run some queries. Here's an example:

```
query {
  allFlashcards {
    id
    question
    answer
  }
}
```
