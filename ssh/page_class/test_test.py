class Rectagle:
    def __init__(self, wid, hei):
        self.wid = wid
        self.hei = hei

    def area(self):
        return self.wid * self.hei

    def paragic(self):
        return 2 *((self.wid + self.hei))

    def grafics(self):
        for i in range(0,self.wid):
            #for j in range(0, self.hei):
            print(i * "*")
            


rec = Rectagle(10,6)
print(dir(rec))
#print(rec.grafics())




