
class Sat:
    def __init__(self):
        self.map = {} # 滿足該真值表的字典查表
        self.array = [] # 滿足該真值表的所有列

    def load(self, table, oi):
        for ti in range(table.rows()):
            input = table.inputs[ti]
            out = table.outputs[ti][oi]
            if out!='0':
                self.array.append(input) 
                self.map[input]=out
