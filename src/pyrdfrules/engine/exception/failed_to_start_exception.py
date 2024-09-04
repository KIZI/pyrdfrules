from pyrdfrules.common.exception.pyrdfrules_exception import PyRDFRulesException


class FailedToStartException(PyRDFRulesException):
    """Raised when the engine fails to start."""

    def __init__(self, message: str = "Failed to start engine."):
        super().__init__(message)