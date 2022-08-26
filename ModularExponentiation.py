
########## Problem 1
def slowPower(g,A,N):
 x = 1
 for i in range(0,A):
   x = x*g % N
 return x

########## Problem 2
def getBinary(A):
  binaryList = []
  while A>0:
   if A%2 == 0:
    binaryList.append(0)
   else:
    binaryList.append(1)
  A = A//2 
#This does the same operation as math.floor(A/2), but without
#ever converting to a float, and therefore avoiding the lack of precision for values of A that are larger than 64 bits.
  return binaryList

def fastPower(g,A,N):
  binaryList = getBinary(A)
  powersOfG = [g % N] #initiate a list of the powers of g with g^1
  for i in range(0,len(binaryList)):
     newPower = powersOfG[-1]**2 % N #square the last element of the list and add it
     powersOfG.append(newPower)
     output = 1
  for i in range(0,len(binaryList)):
   if binaryList[i]==1:
     output = output * powersOfG[i] % N #multiply all the ones corresponding to nonzero binary coefficients
  return output

########## Problem 3(b)
def fastPowerSmall(g,A,N):
   a = g
   b = 1
   while A>0:
     if A % 2 == 1:
       b = b * a % N
     A = A//2
     a = a*a % N
   return b
