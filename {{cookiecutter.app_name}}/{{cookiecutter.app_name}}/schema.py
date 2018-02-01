from apistar import typesystem


class ExampleCreate(typesystem.Object):
    properties = {
        'name': typesystem.String
    }
    required = ['name']


class ExampleList(typesystem.Object):
    properties = {
        'name': typesystem.String,
        'id': typesystem.Integer
    }
