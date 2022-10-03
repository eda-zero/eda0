
class Counter(Chip):
    def __init__(self, n):
        super(Chip, self).__init__(f"counter{n}")
        self.counter = 0
        self.n = n
        self.max = 2**n
    def O(self):
        C = "{0:b}".format(self.counter)
        C = '0'*(self.n-len(C))+C
        return [0 if c=='0' else 1 for c in C]
    def inc(self):
        self.counter = (self.counter+1) % self.max

if __name__ == '__main__':
    C = Counter(2)
    for i in range(20):
        print("C.O()=", C.O())
        C.inc()