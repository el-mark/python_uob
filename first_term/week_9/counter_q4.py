class Counter:

    def __init__(self, wrapAround):
        self.theCount = 0
        self.wrapAround = wrapAround

    def inc(self):
        if self.theCount < self.wrapAround:
            self.theCount = self.theCount + 1
        else:
            self.theCount = 0

    def dec(self):
        if self.theCount > 0:
            self.theCount = self.theCount - 1
        else:
            self.theCount = self.wrapAround

    def getCount(self):
        return self.theCount

    def setCount(self, newCount):
        self.theCount = newCount

    def equals(self, other):
        return self.theCount == other.theCount
    
    def update(self, qty):
        if qty > 0:
            for i in range(qty):
                self.inc()
        else:
            for i in range(abs(qty)):
                self.dec()
        


X = "aabbcc"

A = Counter (40)
B = Counter (9999)
C = Counter (10)
D = C
E = B

A.inc()

for char in X :
    A.inc()

B.dec()
B.dec()

B.dec()
B.inc()

C.inc()
C.setCount(7)

# AFTER RUNNING ALL OF THE CODE ABOVE

# How many times was the body of the for loop above executed ?
# print(A.getCount() - 1)
print(len(X))
# 6 times

# What is the value of char ?
# What is the value of A.getCount() ?
print(A.getCount())
# 7

A.update(10)
print(f'A: {A.getCount()}')
# 17


A.update(-65)
print(f'A: {A.getCount()}')
# 34

A.update(+18)
print(f'A: {A.getCount()}')
# 11
