from pyrdfrules.common.exception.pyrdfrules_exception import PyRDFRulesException

class TaskNotFoundException(PyRDFRulesException):
    """
    Thrown when a task is not found in the RDFRules instance.
    """
    
    def __init__(self, task_id: str):
        super(TaskNotFoundException, self).__init__(f'Task with id {task_id} not found')