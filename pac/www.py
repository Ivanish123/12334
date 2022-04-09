class Windows():

    def __init__(self, x, y):
        self.s1 = x * y


class S():

    def __init__(self, x, y, z):
        self.s = 2 * z * (x + y)
        self.list = []

    def Apennd(self, h, w):
        self.list.append(Windows(h, w))

    def gotovo(self,):
         a =self.s
         for i in self.list:
             a -= i.s1
             return(a)