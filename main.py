import lexicAnalizyer as lA
import firstFollows as fF
import parser as pr

#####################
# Alonso Oropeza
# Script general
# Compiladores
# 08/09/2021
####################

print('Welcome to first-follows generator')
print('Making grammar from what it is inside the grammar.txt file')
grammar, strings = lA.readFile()
terminals, nonTerminals = lA.lexicAnalyzer(grammar) # 1. get terminals and non terminals
terminals.sort()
dic = fF.grammarToDic(grammar, nonTerminals) # transforms the grammar
firsts, follows, LL1 = fF.firfoll1(nonTerminals, terminals, dic) # 2. get first, follows
dic = fF.grammarToDic(grammar, nonTerminals) # porQueNoEsInmutableAlParecer :'v
if not LL1:
    print('not LL1') 
else:
    pr.parser(firsts, follows, LL1, terminals, nonTerminals,strings, dic) # 3. parse the grammar
#fF.output(nonTerminals, terminals, dic)