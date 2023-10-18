import random

f = open('test.txt', 'w')
f.write('code:\n')
for i in range(1, 100):
    random_number = random.randint(1, 100)
    f.write(f'{random_number} ')
f.close()
