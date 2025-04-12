class ReversedList:
    def __init__(self, lst):
        self.lst = lst[::-1]

    def __len__(self):
        return len(self.lst)

    def __str__(self):
        return '{}'.format(self.lst)

    def __getitem__(self, index: int):
        return self.lst[index]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
