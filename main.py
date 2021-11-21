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
terminals, nonTerminals = lA.lexicAnalyzer(grammar)
dic = fF.grammarToDic(grammar, nonTerminals) # transforms the grammar
firsts, follows, LL1 = fF.firfoll1(nonTerminals, terminals, dic)
pr.parser(firsts, follows, LL1, terminals, nonTerminals,strings)





#fF.output(nonTerminals, terminals, dic)
