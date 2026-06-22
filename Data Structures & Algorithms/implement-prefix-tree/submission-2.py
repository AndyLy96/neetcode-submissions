class PrefixTree:

    def __init__(self):
        self.hash = {}

    def insert(self, word: str) -> None:
        self.hash[len(self.hash)] = word

    def search(self, word: str) -> bool:
        if word in self.hash.values():
            return True
        return False    

    def startsWith(self, prefix: str) -> bool:
        for w in self.hash.values():
            if w.startswith(prefix):
                return True
        return False
        