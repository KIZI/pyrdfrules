"""
Logging module exposing logging functionality.

Configurable logging is provided by the `Config` class. The `Logger` class provides the logging functionality. The `log` function provides a global logger instance. The `configure_logging` function configures the logging, and is called automatically upon application startup.

By default, the logging level is set to `logging.INFO`. This can be changed by setting the `log_level` attribute of the `Config` class.
"""