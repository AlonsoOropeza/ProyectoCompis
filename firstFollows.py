#####################
# Alonso Oropeza
# generador first follows
# Compiladores
# 15/10/2021
####################

# En esta segunda entrega, deberás desarrollar, de forma individual,
# una herramienta que, dada una gramática en EBNF, imprime el conjunto
# FIRST y FOLLOW para cada no terminal de la gramática. 
# También deberá imprimir si la gramática es LL(1) o no.

# creates a dictionary of keys to empty list
def dictList(keys):
  dic = dict()
  for key in keys:
    dic[key] = list()
  return dic

# transforms the grammar to dictionary list form
def grammarToDic(grammar, nonTerms):
  dic = dictList(nonTerms)
  for prod in grammar:
    head, body = prod.split('->')
    head = head.replace(' ', '')
    tmp = list()
    counter = 0
    for ele in body.split(): 
      if ele == "'": 
        counter += 1 
        if counter == 2:
          tmp.append(' ')
      else:
        tmp.append(ele)
    dic[head].append(tmp)
  return dic

# calls firsts and follows
def output(nonTerms, terms, dic):
  firsts = getFirst(nonTerms[0], nonTerms, terms, dic, dictList(nonTerms))
  follows = getFollow(nonTerms, terms, dic, dictList(nonTerms), firsts)
  for nonTerm in nonTerms:
    print(nonTerm, '-> FIRST =', firsts[nonTerm], ', FOLLOW =', follows[nonTerm])
  print('LL(1)?', LL1(firsts, follows, dic, nonTerms, terms))

# copy content of one list into another, no repetitions
def mergeNoRep(copy, paste):
  for newEle in copy:
    if newEle not in paste:
      paste.append(newEle)
  return paste

# get all the firsts in a dictionary
def getFirst(nonTerm, nonTerms, terms, dic, firsts):
  firsts = recursiveFirst(nonTerm, nonTerms, terms, dic, firsts)
  firsts = epsiWin(firsts, dic, nonTerms)
  return firsts

# recursive function for get first
def recursiveFirst(nonTerm, nonTerms, terms, dic, firsts):
  for prod in dic[nonTerm]:
    for ele in prod:
      if ele in nonTerms: # if there is a non terminal
        if len(firsts[ele]) == 0: 
          firsts.update(getFirst(ele, nonTerms, terms, dic, firsts))
        firsts[nonTerm] = mergeNoRep(firsts[ele], firsts[nonTerm]) # append terminals
      else: # there is a terminal
        if ' ' in firsts[nonTerm]:
          firsts[nonTerm].remove(' ') # shift epsilon 
        if ele not in firsts[nonTerm]:  
          firsts[nonTerm].append(ele) # add terminal
        break 
  return firsts

# final utility function that checks for A -> B C D
# if all of them have epsilon, we add epsilon to first(A)
def epsiWin(firsts, dic, nonTerms):
  for nonTerm in dic:
    for prod in dic[nonTerm]:
      epsiWins = 0
      for ele in prod:
        if ele in nonTerms and ' ' in firsts[ele]:
          epsiWins += 1
      if  epsiWins == len(prod) and ' ' not in firsts[nonTerm]:
        firsts[nonTerm].append(' ')
  return firsts

# get all the follows in a dictionary
def getFollow(nonTerms, terms, dic, follows, firsts):
  follows = dictList(nonTerms)
  follows[nonTerms[0]].append('$')
  follows = recursiveFollow(nonTerms, terms, dic, follows, firsts)
  #print(follows)
  return follows

#recursive function of follows
def recursiveFollow(nonTerms, terms, dic, follows, firsts):
  for nonTerm in nonTerms:
    for key in dic:
      for prod in dic[key]:
        if nonTerm in prod: # if match
          follows[nonTerm] = mergeNoRep(follows[key], follows[nonTerm]) # add follows
          idx = prod.index(nonTerm) # the index of where it was found
          if len(prod) - idx != 1:
            for i in range(idx+1, len(prod)):
              if prod[i] in terms:
                follows[nonTerm].append(prod[i]) # add ele
              else:
                firstFoes = firsts[prod[i]]
                if ' ' in firstFoes:
                  follows[nonTerm] = mergeNoRep(follows[key], follows[nonTerm]) # add follows
                  firstFoes.remove(' ')
                follows[nonTerm] = mergeNoRep(firstFoes, follows[nonTerm]) # add firsts
  return follows

# get double productions for each nonTerm
def getDoubleProd(nonTerms, dic):
  doubles = list()
  for nonTerm in nonTerms:
    if len(dic[nonTerm]) == 2:
      doubles.append(nonTerm)
  return doubles

# get the firsts of both α and β productions
def getFirstsOfBothProd(dic, double, nonTerms, terms):
  halfDic = dic.copy()
  tmp = halfDic[double][1]
  del halfDic[double][1]
  preFirsts = dict() 
  preFirsts.update(getFirst(double, nonTerms, terms, halfDic, dictList(nonTerms)))
  halfDic[double].append(tmp)
  del halfDic[double][0]
  posFirsts = dict()
  posFirsts.update(getFirst(double, nonTerms, terms, halfDic, dictList(nonTerms)))
  return preFirsts, posFirsts


# if A -> α | β
# FIRST(α) ∩ FIRST(β) = Ø
def firstLL1Rule(preFirsts, posFirsts, double):
  for ele in preFirsts[double]:
    if ele in posFirsts[double]:
      return False # exists in the other firsts(double)
  return True

# if A -> α | β
# if ɛ ϵ FIRST(α), then FIRST(α) ∩ FIRST(A) = Ø
def secondLL1Rule(double, firsts, follows):
  if ' ' in firsts[double]:
    for ele in firsts[double]:
      if ele in follows[double]:
        return False
  return True

# return true if LL1 or false if not
def LL1(firsts, follows, dic, nonTerms, terms):
  doubles = getDoubleProd(nonTerms, dic)
  if doubles == list():
    return False # there isn't any nonTerm of two productions
  else:
    for double in doubles: 
      preFirsts, posFirsts = getFirstsOfBothProd(dic, double, nonTerms, terms)
      if not firstLL1Rule(preFirsts, posFirsts, double): return False
      if not secondLL1Rule(double, preFirsts, follows): return False
      if not secondLL1Rule(double, posFirsts, follows): return False
    return True

def firfoll1(nonTerms, terms, dic):
  firsts = getFirst(nonTerms[0], nonTerms, terms, dic, dictList(nonTerms))
  follows = getFollow(nonTerms, terms, dic, dictList(nonTerms), firsts)
  boliche = LL1(firsts, follows, dic, nonTerms, terms)
  return firsts, follows, boliche

    

'''
5
goal -> A
A -> ( A )
A -> two
two -> a 
two -> b

6
S -> A a
A -> B D
B -> b
B -> ' '
D -> d
D -> ' '

5
X -> Y z
X -> a
Y -> b Z
Y -> ' '
Z -> ' '
'''