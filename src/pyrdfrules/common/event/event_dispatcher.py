class EventDispatcher():
    """
    The EventDispatcher class manages event listeners and dispatches events to them.
    """
    def __init__(self):
        self._listeners = []
        
    def add_listener(self, callback: callable):
        """Adds a listener to the event dispatcher."""
        self._listeners.append(callback)
        
    def remove_listener(self, callback: callable):
        """Removes a listener from the event dispatcher."""
        self._listeners.remove(callback)
        
    def dispatch(self, *args, **kwargs):
        """Dispatches an event to all listeners."""
        for listener in self._listeners:
            listener(*args, **kwargs)

    def __iadd__(self, other: callable):
        self.add_listener(other)
        return self
        
    def __isub__(self, other : callable):
        self.remove_listener(other)
        return self