POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'title': {'type': 'string'}  # , 'enum': ['POST']}
    },
    'required': ['id']
}
