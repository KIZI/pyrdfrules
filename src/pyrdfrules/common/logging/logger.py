import logging

pyrdfrules_logger = None

class Logger():
    
    logger: logging.Logger = None
    
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        pass
    
    def get_logger(self) -> logging.Logger:
        """Gets the logger.
        
        Returns:
            logging.Logger: Logger.
        """
        
        return self.logger
    
    
def log() -> logging.Logger:
    """Gets the logger.
    
    Returns:
        logging.Logger: Logger.
    """
    
    global pyrdfrules_logger
    
    if pyrdfrules_logger is None:
        pyrdfrules_logger = Logger()
    
    return pyrdfrules_logger.get_logger()