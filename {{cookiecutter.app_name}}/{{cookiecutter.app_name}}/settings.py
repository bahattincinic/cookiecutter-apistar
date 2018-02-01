from apistar import environment, typesystem
from apistar.parsers import JSONParser

from .models import Base


class Env(environment.Environment):
    properties = {
        'DEBUG': typesystem.boolean(default=False),
        'DATABASE_URL': typesystem.string(),
    }
    required = ['DEBUG']


env = Env()
settings = {
    'DEBUG': env['DEBUG'],
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata
    },
    'PARSERS': [JSONParser()],
    'SCHEMA': {
        'TITLE': '{{ cookiecutter.project_name }}',
        'DESCRIPTION': '{{ cookiecutter.project_short_description}}'
    }
}
