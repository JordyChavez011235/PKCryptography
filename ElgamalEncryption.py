
########## Problem 1

##### Part (a)
print('\n',"Part (a)",'\n')
x = "Hello World"
for i in x:
print(i)

##### Part (b)
print('\n',"Part (b)",'\n')
x = "Hello"
y = x + '!'
print(y)

##### Part (c)
print('\n',"Part (c)",'\n')
print(ord('a'))
print(ord('A'))
print(ord(' '))
print(ord(','))
#print(ord(a)) Ord needs input of a char which needs ' '
#print(ord("hello")) Ord needs input of a char not a string.

##### Part (d)
print('\n',"Part (d)",'\n')
print(chr(98))
print(chr(40))
print(chr(ord('F')))
print(ord(chr(201)))

#Output
Part (a)
H
e
l
l
o
W
o
r
l
d

Part (b)
Hello!

Part (c)
97
65
32
44

Part (d)
b
(
F
201

########## Problem 2
##### Part (a)
def textToInt(words):
   number = 0
   i = 0
   for letter in words:
     number += ord(letter)*(256**i)
     i+=1
   return number

##### Part (b)
def intToText(number):
   words = ""
   while number>0:
     nextLetter = number % 256
     words += chr(nextLetter)
     number = (number-nextLetter)/256
   return words

  ########## Problem 3
#We save a prime as a variable which we may vary:
p = 370141817103067776979133
##### Part (a)
def encrypt(m,k):
   return m*k % p

def decrypt(c,k):
  kinv = findInverse(k,p)
  return c*kinv % p

##### Part (b)
print('\n',"Part (b)",'\n')

key = 147955927473629958316
cipher = 85449848686775252245536

message = decrypt(cipher,key)
print(intToText(message))

##### Part (c)
print('\n',"Part (c)",'\n')


message = textToInt("Hello!")
print("Mesage as integer:",message)
myKey = 1213141516171819
cipher = encrypt(message,myKey)
print("Encrypted integer:",cipher)
newMessage = decrypt(cipher,myKey)
print("Decrypted integer:",newMessage)
print("Decoded to text:",intToText(newMessage))

##### Part (d)
print('\n',"Part (d)",'\n')
#First we update the prime:
p = 23169331
print("My new prime is",p)
#We'll then run the same code:

message = textToInt("Hello!")
print("Mesage as integer:",message)
myKey = 1213141516171819
cipher = encrypt(message,myKey)
print("Encrypted integer:",cipher)
newMessage = decrypt(cipher,myKey)
print("Decrypted integer:",newMessage)
print("Decoded to text:",intToText(newMessage))
print("We got the wrong answer because the message doesnt fit in F_p^*")

#Output

#Part (b)
##Testing…

#Part (c)
##Mesage as integer: 36762444129608
##Encrypted integer: 29808642902613194360915
##Decrypted integer: 36762444129608
##Decoded to text: Hello!

#Part (d)
##My new prime is 23169331
##Mesage as integer: 36762444129608
##Encrypted integer: 16329898
##Decrypted integer: 14171873
##Decoded to text: á>Ø
##We got the wrong answer because the message doesnt fit in F_p^*
  
########## Problem 4

#We can put this all in one function:
def doDiffieHellman(prime,generator,aliceSecret,bobSecret):
#they compute public numbers to swap
   alicePublic = fastPowerSmall(generator,aliceSecret,prime)
   bobPublic = fastPowerSmall(generator,bobSecret,prime)
   print("Alice's public number is",alicePublic)
   print("Bob's public number is",bobPublic)
#they both compute the shared secret
   aliceSharedSecret = fastPowerSmall(bobPublic,aliceSecret,prime)
   bobSharedSecret = fastPowerSmall(alicePublic,bobSecret,prime)
   print("Alice computed",aliceSharedSecret)
   print("Bob computed",bobSharedSecret)

##### Part (a)
print('\n',"Part (a)",'\n')
#We first choose a prime and generator
p = 17
g = 3
#Alice and bob have secret numbers
a = 5
b = 3

doDiffieHellman(p,g,a,b)

##### Part (b)
print('\n',"Part (b)",'\n')
#We first choose a prime and generator
p = 56509
g = 2
#Alice and bob have secret numbers
a = 3482
b = 20487
doDiffieHellman(p,g,a,b)
##### Part (c)
print('\n',"Part (c)",'\n')
#We first choose a prime and generator
p = 370141817103067776979133
g = 31415926535
#Alice and bob have secret numbers
a = 112233445566778899
b = 998877665544332211

doDiffieHellman(p,g,a,b)

#Output

#Part (a)
##Alice's public number is 5
##Bob's public number is 10
##Alice computed 6
##Bob computed 6

#Part (b)
##Alice's public number is 49892
##Bob's public number is 18602
##Alice computed 31046
##Bob computed 31046

#Part (c)
##Alice's public number is 234986677042258789314441
##Bob's public number is 357420017376256037149781
##Alice computed 221206967657463523352818
##Bob computed 221206967657463523352818  

 ########## Problem #5
 

##### Parts (a) and (b)
def generatePublicKey(a):
  return fastPowerSmall(g,a,p)

def elgamalEncrypt(m,A):
   k = ZZ.random_element(2,p-2)
   c1 = fastPowerSmall(g,k,p)
   B = fastPowerSmall(A,k,p)
   c2 = m*B % p
   return [c1,c2]

def elgamalDecrypt(c1,c2,a):
   x = findInverse(fastPowerSmall(c1,a,p),p)
   return x*c2 % p

##### Part (c)
p = 787
g = 34

#secret key:
a = 99

#generate the public key
A = generatePublicKey(a)

#what's bob's message?
m = 314

#encrypt it using the public key A
cipherText = elgamalEncrypt(m,A)

#Then decrypt it:
decodedM = elgamalDecrypt(cipherText[0],cipherText[1],a)

#did it work?
print("Bob's message was",m,"and Alice decoded",decodedM,'\n')

###### Part (d)
#Here's the input

p= 753022235974397591242683563886842009117
g = 47393028462819284673
aliceSecret = 314159265358979323846
c1 = 449164960684688587557185888310931655332
c2 = 608713686463403616105013668689979824341

#let's decrypt it
decodedM = elgamalDecrypt(c1,c2,aliceSecret)

#and turn it into text:
decodedMText = intToText(decodedM)

#print it:
print("Decoded message from Gabriel in part (d):")
print(decodedMText,'\n')

##### Part (e)

#Here's the public key:
A = 418194837551245918495968754919547251501

messageAsText = "Secret Message!"

#turn it into a number
message = textToInt(messageAsText)

#then encode it
c = elgamalEncrypt(message,A)
print("Cipher text for Gabriel in part (e):")
print(c)

#Output
  
##Bob's message was 314 and Alice decoded 314
##Decoded message from Gabriel in part (d):
##Can you hear me?
##Cipher text for Gabriel in part (e):
##[110289188331938815234884147529065440837,
##666581497017700795250063878827648284718]
