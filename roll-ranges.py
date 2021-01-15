from random import random
#example: [[2,20],[1,10]] means 2 d20, 1 d10
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

#chunk is percent of domain range
def rollstat(dice,passes,chunk=10,debug=False):
    l=list()
    for x in range(0,passes):
        l.append(roll(dice,debug=debug))
    chunksize=(max(l)-min(l))*(chunk/100)
    #print(chunksize)
    nums=list()
    score=0
    for x in l:
        if [x,score] not in nums: nums.append([x,score])
    for x in nums:
        x[1]=100*(l.count(x[0])/len(l))
    nums.sort(key=lambda x: x[0])
    copy=nums.copy()
    newlist=list()
    counter=0
    blockscore=0
    mn=0
    mx=0
    while copy:
        x=copy.pop()
        if counter==0:
            mx=x[0]
            blockscore=0
        blockscore += x[1]
        counter += 1
        if mx-x[0] >=chunksize or len(copy) ==0:
            mn=x[0]
            counter=0
            newlist.append([str(mn)+'-'+str(mx),blockscore])
    newlist.sort(key=lambda x: x[1],reverse=True)
    return newlist


#example: [[2,20],[1,10]] means 2 d20, 1 d10
#chunk is percent of domain range
import time
t=time.time()

#-------MAIN INPUTS HERE---------

for x in rollstat([[18,20]],500000,chunk=39,debug=False):
    print(x[0],'=',str(round(x[1],3))+'%')





print('took',round(time.time()-t,2),'seconds')
