from pyrdfrules.common.exception.pyrdfrules_exception import PyRDFRulesException

class TaskNotFoundException(PyRDFRulesException):
    def __init__(self, task_id):
        super(TaskNotFoundException, self).__init__(f'Task with id {task_id} not found')