#####################
# Alonso Oropeza
# Analizador lexico
# Compiladores
# 08/09/2021
####################

# En esta primera entrega, deberás desarrollar, de forma individual, 
# una herramienta que, dada una gramática en EBNF, 
# imprimir el listado de terminales y no terminales de la gramática.

# to read n lines and make the grammar
# INPUT:
# n (int) --> number of lines
# followed by n lines of the gramar
def grammarMaker():
    grammar = list()
    for x in range (int(input())):
        grammar.append(input())
    return grammar

# to parse the grammar into terminals & non terminals
def lexicAnalyzer(grammar):
  terminals = set()
  nonTerminals = list()
  for x in grammar: # iterate each production
    head, body = x.split('->')
    head = head.replace(' ', '')
    if head not in nonTerminals:
      nonTerminals.append(head) # add non terminals
    counter = 0
    for ele in body.split(): 
      if ele == "'": 
        counter += 1 
        if counter == 2:
          terminals.add(' ') # add epsilon
      else:
        terminals.add(ele) # add  terminals
  for nonTerm in nonTerminals:
    if nonTerm in terminals:
      terminals.remove(nonTerm) # remove nonTerms
  return list(terminals), nonTerminals
'''
6
S -> A a
A -> B D
B -> b
B -> ' '
D -> d
D -> ' '
'''
# print('Terminals: ')
# print(*terminals, sep = ', ')
# print('Non Terminals: ')
# print(*nonTerminals, sep = ', ')

def readFile():
  f = open("grammar.txt", "r")
  grammar = f.readlines()
  f.close()
  N = int(grammar[0][0])
  M = int(grammar[0][2])
  strings = grammar[-M:]
  grammar = grammar[1:N+1]
  return grammar, strings