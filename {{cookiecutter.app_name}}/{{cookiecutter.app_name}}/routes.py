from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from {{ cookiecutter.app_name}}.views import (
    list_view, create_view
)


routes = [
    Route('/example', 'GET', list_view),
    Route('/example', 'POST', create_view),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
