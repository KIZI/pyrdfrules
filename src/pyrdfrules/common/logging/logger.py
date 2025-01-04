import logging

from pyrdfrules.config import Config

pyrdfrules_logger : logging.Logger = None
"""Global instance of the logger.
Empty by default.
Obtain the logger by calling the `log` function from this package.
"""

class Logger():
    """
    The Logger class provides methods to configure and retrieve the logger for the application.
    """
    
    logger: logging.Logger = None
    
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        pass
    
    def set_config(self, config: Config) -> None:
        """Sets the configuration.
        
        Args:
            config (Config): Configuration.
        """
    
        self.set_logging_level(config.log_level)
    
    def set_logging_level(self, level: int) -> None:
        """Sets the logging level.
        
        Args:
            level (int): Logging level.
        """
        
        self.logger.setLevel(level)
    
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

def configure_logging(config: Config) -> None:
    """Configures logging.
    
    Args:
        config (Config): Configuration.
    """
    
    global pyrdfrules_logger
    
    if pyrdfrules_logger is None:
        pyrdfrules_logger = Logger()
    
    pyrdfrules_logger.set_config(config)