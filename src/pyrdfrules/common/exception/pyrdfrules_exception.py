
class PyRDFRulesException(Exception):
    """Base class for all exceptions in PyRDFRules."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self