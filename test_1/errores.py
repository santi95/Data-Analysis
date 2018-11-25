class BadRequest(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, "No estás haciendo bien la consulta")

class NotFound(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class NotAcceptable(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class GenomeError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

#raise GenomeError('cosas')
