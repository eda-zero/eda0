class TruthTable:
    def __init__(self, table, nIn, names):
        self.nIn = nIn
        self.nOut = len(table[0])-nIn
        self.inputs = []
        self.outputs = []
        self.iNames = names[:nIn]
        self.oNames = names[nIn:]
        for row in table:
            self.inputs.append(row[:nIn])
            self.outputs.append(row[nIn:])

    def rows(self):
        return len(self.inputs)
