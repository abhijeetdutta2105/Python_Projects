import random

#this initializes the random number generator
random.seed(1)
oldstate = random.getstate()

# print(oldstate)
print('some radom numbers generated')
for i in range(3):
  print(random.randint(1,100))

random.setstate(oldstate)

print('same set of random numbers generated')
for i in range(3):
  print(random.randint(1,100))
 

# for generating random floating point number

print(random.random()) # this will generate the number b/w 0.0 and 1.0
print(random.uniform(10,20)) #and this will generate the numbers b/w the given numbers