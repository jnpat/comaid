import random

def rand(popSize,target): #Random password
  pop = []
  inv = []
  for i in range(popSize):
    for j in range(len(target)):
      inv.append(random.randint(0,9))
    pop.append(inv)
    inv = []
  return pop

def findFit(target,pop): #Find fitness check by population and target 
  pop1 = []
  for i in range(len(pop)):
    fitNess = 0
    for j in range(len(pop[0])):
      if target[j] == pop[i][j]:
        fitNess += 1
    pop1.append((pop[i],fitNess)) #Array[pop,fitness]
  return pop1

def sort(pop1): #Sort fitness to find best fitness on the top 
  pop1.sort(key = lambda x: x[1],reverse=True)
  return pop1

def parentSelect(pop1): #Random two individual to Compare the best 
  x = random.randint(0,popSize-1)
  y = random.randint(0,popSize-1)
  if pop1[x][1] >= pop1[y][1]:
    return pop1[x]
  else:
    return pop1[y]

def xOver(p1,p2):
  x = random.randint(0,popSize-1)
  first1 = []
  first2 = []
  second1 = []
  second2 = []
  for i in range(len(p1)):
    if i <= x:
      first1.append(p1[i])
      second1.append(p2[i])
    else: 
      first2.append(p1[i])
      second2.append(p2[i])
  #swap
  o1 = first1+second2
  o2 = second1+first2
  return o1,o2

def mutation(o1,o2):
  mR = 0.05*100 #Rate to change bit
  for i in range(len(o1)):
    prob1 = random.randint(1,100)
    prob2 = random.randint(1,100)
    if prob1 <= mR:
      o1[i] = random.randint(0,9) #Random 0-9 to change
    elif prob2 <= mR:
      o2[i] = random.randint(0,9) #Random 0-9 to change
  return o1,o2

def elite(population,offSpring): #Choose best individual in population to offSpring
  x = (popSize*0.01)*20
  for i in range(len(population)):
    if i < x:
      offSpring.append(population[i][0])
  return offSpring


# --------------------------- main --------------------------- #
popSize = input('Enter population size: ')
target = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

population = sort(findFit(target,rand(popSize,target))) #first population
i = 1
while(population[0][1] < 20): #check by fitness = 20 to stop
  offSpring = []
  i += 1
  elite(population,offSpring)
  while(len(offSpring)<len(population)): #fill in offSpring to size = population size
    p1 = parentSelect(population)
    p2 = parentSelect(population)

    child = xOver(p1[0],p2[0])
    child = mutation(child[0],child[1])

    offSpring.append(child[0])
    offSpring.append(child[1])
    

  population = offSpring
  population = sort(findFit(target,population))
  print("Generation" + str(i) + ", Best fitness" + str(population[0][1]) + ", Best individual: " + str(population[0][0]))