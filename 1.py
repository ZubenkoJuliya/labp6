class BigBell:
    def __init__(self):
        self.ding = 'ding'

    def sound(self):
        print(self.ding)
        if self.ding == 'ding':
            self.ding = 'dong'
        else:
            self.ding = 'ding'


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
