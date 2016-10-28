path = []

fromSrc = 0
fromDest = 0

path.append(1)
path.append(11)

#from src
path.insert(fromSrc+1,2)
fromSrc+=1

#from dest
path.insert(-(fromDest+1),10)
fromDest+=1

#from src
path.insert(fromSrc+1,3)
fromSrc+=1

#from dest
path.insert(-(fromDest+1),9)
fromDest+=1

#from dest
path.insert(-(fromDest+1),8)
fromDest+=1

#from src
path.insert(fromSrc+1,4)
fromSrc+=1

#say I reached the length
#add the simple path [5,6,7]

path[fromSrc+1:fromSrc+1] = [5,6,7]


print path
print path[1:len(path)-1]