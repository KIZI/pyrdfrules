import logging
from pydantic import BaseModel, PositiveInt


class Config(BaseModel):
    """
    Configuration class for the instance.
    """
    
    task_update_interval_ms: PositiveInt = 1000
    """Update interval for the task status in milliseconds.
    
    This affects how often the task status is updated.
    """
    
    task_timeout_ms: int = 0
    """Timeout for the task in milliseconds. Zero means no timeout.
    """
    
    log_output: bool = True
    """Logs output to the console.
    """
    
    log_level: int = logging.INFO
    """Logging level.
    """