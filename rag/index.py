class VectorIndex:
    def __init__(self):
        self.vectors = []
        self.meta = []

    def add(self, vector, meta):
        self.vectors.append(vector)
        self.meta.append(meta)
