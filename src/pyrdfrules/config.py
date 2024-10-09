from pydantic import BaseModel, PositiveInt


class Config(BaseModel):
    """Configuration class for the instance.
    """
    
    task_update_interval_ms: PositiveInt = 1000
    """Update interval for the task status in milliseconds.
    
    This affects how often the task status is updated.
    """
    
    log_output: bool = True
    """Logs output to the console.
    """