{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}

### Requirements

* Python 3.6+
* Postgres Postgres 9.4+

### Installation

#### OSX

Install Homebrew

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install Required Packages:

    $ brew install python3
    $ brew install postgresql

#### Ubuntu/Debian

Install Required Packages:
(python3 is already installed as default on 16.04)

    $ sudo apt-get install python3-dev postgresql

Set postgres password:

    $ sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"

Add postgres as default user: (write this in your .bashrc or .zshrc to make it persistent)

    $ export PGUSER=postgres
    $ export PGPASSWORD=postgres

### Building the Project

Create Virtual Environment (3.5+)

    $ mkvirtualenv --python=$(which python3) {{cookiecutter.app_name}}

Setup PostgreSQL Database

    $ initdb /usr/local/var/postgres
    $ postgres -D /usr/local/var/postgres/ #in another terminal
    $ createuser --superuser postgres
    $ createdb -U postgres {{cookiecutter.app_name}}

Clone the repository and:

    $ git clone git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    $ cd {{cookiecutter.app_name}}/

install requirements

    $ workon {{cookiecutter.app_name}}
    $ pip install -r requirements/dev.txt

To run the project, Follow the following commands:

    $ export DEBUG=TRUE
    $ export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/{{cookiecutter.app_name}}"
    $ apistar create_tables
    $ apistar run
