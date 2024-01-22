class Turn:
    number = 0
    def add(self):
        self.number += 1

def changeX():
    turn.add()

turn = Turn()
changeX()
changeX()
changeX()
print(turn.number)



# turn = 0
# def changeX():
#     turn += 1

# changeX()
# print(turn)
