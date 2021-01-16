#example: [[2,20],[1,10]] means 2 d20, 1 d10
from random import random
import sys
def roll(dice=[[2,20],[1,10]],debug=False):
    #----syntax checker----
    if type(dice) != list:
        raise ValueError('input to roll must be 2d array')
    else:
        for x in dice:
            if type(x) != list:
                raise ValueError('input to roll must be 2d array')
    #------print block-----
    if debug:
        print('rolling ',end='')
        for x in dice:
            comma=not dice[len(dice)-1] == x
            print(x[0],'d'+str(x[1])+comma*', ',end='')
        print('')
    #--------math block-----
    total=0
    for block in dice:
        for num in range(0,block[0]):
           total+= 1+int(random()*block[1])
    return(total)


def rollstat(dice,passes,pretty=False):
    l=list()
    for x in range(0,passes):
        l.append(roll(dice))
    nums=list()
    score=0
    for x in l:
        if [x,score] not in nums: nums.append([x,score])
    for x in nums:
        x[1]=100*(l.count(x[0])/len(l))
    nums.sort(key=lambda x: x[1],reverse=True)
    if pretty:
        for x in nums:
            print(x)
    return nums

if __name__=='__main__':
    import time
    t=time.time()
    
    argv=sys.argv
    argv.pop(0)
    unpackedargs=[ x.split('d') for x in argv ]
    for c,x in enumerate(unpackedargs):
        for i,y in enumerate(x):
            unpackedargs[c][i] = int(y)
    print(argv)
    print(unpackedargs)

    dice=[[18,20]]
    if len(unpackedargs) > 0:
        dice=unpackedargs
    

    #example: [[2,20],[1,10]] means 2 d20, 1 d10
    #-------MAIN INPUTS HERE---------
    for x in rollstat([[18,20]],100000,pretty=False):
        print(str(x[0])+' = '+str(x[1])+'%')






    print('took',round(time.time()-t,2),'seconds')
