from apistar import Response
from apistar.backends.sqlalchemy_backend import Session

from .models import Example
from .schema import ExampleCreate, ExampleList


def list_view(session: Session) -> Response:
    return Response(content=[
        ExampleList(item)
        for item in session.query(Example).all()
    ])


def create_view(session: Session, data: ExampleCreate) -> Response:
    instance = Example(name=data.name)
    session.add(instance)
    session.flush()

    return Response(status=201, content=ExampleList(instance))
