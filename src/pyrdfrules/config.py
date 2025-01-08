import logging
from pathlib import Path
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
    
    workspace_path: Path|None = None
    """Path to the workspace directory.
    Applicable only to local instances of RDFRules.
    
    If empty, will default to the install directory of RDFRules/workspace.
    """