from pyrdfrules.api.rdfrules_api_context import RDFRulesApiContext


class TaskApi():
    
    context: RDFRulesApiContext
    
    def __init__(self, context: RDFRulesApiContext) -> None:
        self.context = context
        pass
    
    async def create_task(self):
        """Create a task.
        """
        pass
    
    async def get_task_status(self, task_id: str):
        """Get the status of a task.
        """
        pass
    
    async def interrupt_task(self, task_id: str):
        """Interrupt a task.
        """
        pass