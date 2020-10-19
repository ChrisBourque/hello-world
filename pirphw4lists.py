''' This is a function which adds elements to a list and rejects it to a different list if it is a repeat.'''

myUniqueList = []
myLeftOvers = []

#notUnique = False
#unique = True
#for thing in myUniqueList 

def isUnique(thing):
# 
      if thing in (myUniqueList):
        myLeftOvers.append (thing)
#		return False
#addorNot = False
      else:
        myUniqueList.append (thing)
        return(thing)
#		return True
#addorNot = True
#myLeftOvers.append


isUnique(1)
print(myUniqueList)
print(myLeftOvers)
isUnique(3)
print(myUniqueList)
print(myLeftOvers)
isUnique(1)
print(myUniqueList)
print(myLeftOvers)
isUnique(33)
print(myUniqueList)
print(myLeftOvers)
isUnique(76)
print(myUniqueList)
print(myLeftOvers)
isUnique(1)
print(myUniqueList)
print(myLeftOvers)
isUnique(33)
print(myUniqueList)
print(myLeftOvers)
isUnique('dog')
print(myUniqueList)
print(myLeftOvers)
isUnique('cat')
print(myUniqueList)
print(myLeftOvers)
isUnique('dog')


print(myUniqueList)

print(myLeftOvers)

