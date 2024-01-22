class Counter:

    def __init__(self):
        self.theCount = 0

    def inc(self):
        if self.theCount < 999:
            self.theCount = self.theCount + 1
        else:
            self.theCount = 0

    def dec(self):
        if self.theCount > 0:
            self.theCount = self.theCount - 1
        else:
            self.theCount = 999

    def getCount(self):
        return self.theCount

    def setCount(self, newCount):
        self.theCount = newCount

    def equals(self, other):
        return self.theCount == other.theCount


X = "aabbcc"

A = Counter ()
B = Counter ()
C = Counter ()
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

# What is the value of B.getCount() ?
print(B.getCount())
# 998

# What is the value of E.getCount() ?
print(E.getCount())
# 998

# What is the value of C.getCount() ?
print(C.getCount())
# 7

# What is the value of C == D ?
print(C.equals(D))
# True

# What is the value of A == C ?
print(f'A: {A.getCount()}')
print(f'C: {C.getCount()}')
print(A.equals(C))
# True

# What is the value of A.equals(C) ?
print(A.equals(C))
# True

D.dec()
print(f'D: {D.getCount()}')
print(f'C: {C.getCount()}')
