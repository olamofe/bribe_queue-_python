#bribe queue solution
######
def minimumBribes(q):
    bribe = 0
    lenlist = len(q)
    for index in range(lenlist):
        if(q[index] > (index+1)):
            jump = q[index]-(index+1)
            if(jump > 2):
                print("Too chaotic")
                return "Too chaotic"
            bribe += jump
        else:
            if(index+1 <= lenlist-1 and q[index] > q[index+1]):
                bribe += 1
    print(bribe)
    return bribe