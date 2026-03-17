# memory.py

_memory = {}
_history = []

def update_memory(key, value):
    _memory[key] = value

def get_memory(key):
    return _memory.get(key)

def add_to_history(message):
    _history.append(message)
    if len(_history) > 10:
        _history.pop(0)

def get_history():
    return _history