'''find all the symmetric pairs in an array of pairs'''
def findpairs(pairs):
    #create an empty set of strings
    s=set()
    #do for each pair
    for (x,y) in pairs:
        #insert the curret pair'(x,y)' into theset
        s.add((x,y))
        #if mirror pair'(y,x)' is seen before,print the pairs
        if (y,x) in s:
            print((x,y),"|",(y,x))
pairs=[(3,4),(1,2),(5,2),(7,10),(4,3),(2,5)]
findpairs(pairs)