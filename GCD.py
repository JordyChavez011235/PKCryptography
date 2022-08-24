##### part (a)
def divides(a,b):
#We use that b%a == 0 if and only if a divides b
    return b%a==0

##### part (b)
def getDivisors(a):
#first give an empty list of divisors
    listOfDivisors = []
#Check each integer and if it is a divisor add it to the list
    for i in range(1,a+1):
     if divides(i,a):
      listOfDivisors.append(i)
    return listOfDivisors

def getDivisorsFaster(a):
  listOfDivisors = []
  for i in range(1,int(math.sqrt(a)+1)):
   if divides(i,a):
    listOfDivisors.append(i)
    listOfDivisors.append(a/i)
   return listOfDivisors

##### part (c)
def getCommonDivisors(a,b):
#you could call getDivisors and compare lists, but it's a bit more␣ ,→efficient I think to just populate a new list at once.
  listOfCommonDivisors = []
  for i in range(1,min(a,b)+1):
    if divides(i,a) and divides(i,b):
     listOfCommonDivisors.append(i)
  return listOfCommonDivisors

##### part (d)
#because getCommonDivisors returns a sorted list, we just need the top (or -1st) 
#element of the list. If it were not sorted, you would have to sort 
#the list or at least go through it looking for the top element.
def findGCDSlow(a,b):
  return getCommonDivisors(a,b)[-1]

def divisionWithRemainder(a,b):
#The trick here is to find the remainder first. Then it becomes a simple division problem.
  r = a%b
#then solve a = bq+r for r
  q = (a-r)//b #Try to use // for integer division to avoid float errors
  return [q,r]

##### part(b)
def findGCDFast(a,b):
  while(b>0): #If the remainder hasn't yet become 0
   qr = divisionWithRemainder(a,b)
#replace (a,b) with (b,r)
   a = b
   b = qr[1]
#once we break out our remainder b=0, so the one before it is in position a.
  return a

def extendedGCD(a,b):
#Each remainder can be computed in terms of a and b. These placeholders 
#save the coefficients in the previous 2 remainders
 u0 = 1
 v0 = 0
 u1 = 0
 v1 = 1
 while(b>0): #If the remainder hasn't yet become 0
#then do division with remainder
  qr = divisionWithRemainder(a,b)
#replace (a,b) with (b,r)
  a = b
  b = qr[1]
#compute the new cofficients
  u = u0 - qr[0]*u1
  v = v0 - qr[0]*v1
#and shift them coefficients:
  u0 = u1
  u1 = u
  v0 = v1
  v1 = v
#once we break out our remainder b=0, so the one before it is in position a. 
#Therefore we want the coefficients associated to a as well, which are u0 and v0
  return [a,u0,v0]
  
