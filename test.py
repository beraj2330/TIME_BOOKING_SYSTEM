
def func(test):

    a = {}

    for x in test:
        if x not in a:
            a[x]=1
        else:
            a[x] = a[x] + 1

    return a

test = ['yellow', 'blue', 'yellow', 'brown', 'brown', 'yellow', 'blue']
print(func(test))