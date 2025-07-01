class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.index = 0
        self.full = False

    def append(self, value):
        self.data[self.index] = value
        self.index = (self.index + 1) % self.size
        if self.index == 0:
            self.full = True

    def get(self):
        if self.full:
            return self.data[self.index:] + self.data[:self.index]
        else:
            return self.data[:self.index]