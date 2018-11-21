#to do list
#figure out if lines 47 - 41

import random
import time

i = 1
learn = 10
max = 10
min = 1
x = max/2
x_2 = max/2
rand = random.randrange(min, max)
counter = 0

def cost(b):
  return(b - rand)

while(learn > 1):
    counter = 0
    rand = random.randrange(min, max)
    while(cost(x) != 0):

        prevX = x
        counter = counter + 1
        learn = counter

        if abs(x_2) > rand:
            x = x-1
            print('cost: ')
            print(cost(x))
            print('x:')
            print(x)
            counter = counter + 1
            learn = counter
            print('counter: ')
            print(counter)
        elif abs(x_2) < rand:
            x = x+1
            print('cost: ')
            print(cost(x))
            print('x:')
            print(x)
            counter = counter + 1
            learn = counter
            print('counter:')
            print(counter)

    print('target: ')
    print(rand)
    #x = (x+prevX)/2   #this is another idea to train the neural networkish thing
    if((x_2 - rand) > 0):
        x_2 = x_2 + 1
    elif((x_2 - rand) < 0):
        x_2 = x_2 -1


    print("ajusted x:")
    print(x)
    print('i: ')
    print(i)
    i = i+1
    print('distance from perfect guess')
    print(learn)

print('Neural network successful with x reaching 1 first try')
print('trained x (assigned as x_2 ): ')
print(x_2)
