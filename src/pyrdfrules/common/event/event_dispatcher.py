class EventDispatcher():
    def __init__(self):
        self._listeners = []
        
    def add_listener(self, callback: callable):
        self._listeners.append(callback)
        
    def remove_listener(self, callback: callable):
        self._listeners.remove(callback)
        
    def dispatch(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)

    def __iadd__(self, other: callable):
        self.add_listener(other)
        return self
        
    def __isub__(self, other : callable):
        self.remove_listener(other)
        return self