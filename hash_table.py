from state import State


class HashTable:

    def __init__(self):
        self.dict = {}

    def push(self, s):
        self.dict[s.puzzle] = s

    def get(self, s):
        if s.puzzle in self.dict:
            return (self.dict[s.puzzle])
        return None

    def contain(self, s):
        if s.puzzle in self.dict:
            return (True)
        return (False)
