x = 'global'

def func(x):
    x = 'not global'
    print(x)

func(x)
print(x)
