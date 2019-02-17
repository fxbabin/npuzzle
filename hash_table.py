from state import State

class HashTable:

    def __init__(self):
        self.dict = {}

    def push(self, s):
        t = tuple(s.puzzle)
        self.dict[t] = s
    
    def get(self, s):
        t = tuple(s.puzzle)
        if t in self.dict:
            return (self.dict[t])
        return None

    def contain(self, s):
        t = tuple(s.puzzle)
        if t in self.dict:
            return (True)
        return (False)
