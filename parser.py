
#####################
# Alonso Oropeza
# parsing table and string analyzer
# Compiladores
# 20/11/2021
####################

import firstFollows as fF

#creates a dictionary to map a string to idx
def mapMaker(ls):
    idx=0
    dic = dict()
    for ele in ls:
        dic[ele] = idx
        idx += 1
    return dic

#creates a table of len(nonTerms) rows and len(term) cols
def parsingTableGen(nonTerms, terms):
    pTable = []
    for x in range (len(nonTerms)): 
        pTable.append([])
        for y in range(len(terms)):
            pTable[x].append('')
    return pTable

def parser(firsts, follows, LL1, terms, nonTerms):
    nonTermsMap = mapMaker(nonTerms)
    termsMap = mapMaker(terms)
    print(nonTermsMap, termsMap)
    pTable = parsingTableGen(nonTerms, terms)
    pTable[0][0]='goal->A'
    print(pTable)
    print(pTable[nonTermsMap['goal']][termsMap['a']])




f = open('parser.html','w')

ls = [
    ['nonTerm', '(', 'a'],
    ['goal', '', 'asdad'],
    ['A', 'asdad', '']
]

ls2 = [
    ['input 1', 'yes'],
    ['input 2', 'no'],
    ['input 3', 'no']
]

def tableMaker(ls):
    str = """<style>th, td {border: 1px solid black;}td{text-align:center;}</style><table>"""
    for row in ls:
        str += "<tr>"
        for ele in row:
            col = "<td>" + ele + "</td>"
            str += col
        str += "</tr>"
    str += "</table></br>"
    return str

def listMaker(ls):
    str = ""
    for row in ls:
        col = """<b>""" + row[0] + """: </b>"""
        str += col
        col = row[1] + """</br>"""
        str += col
    return  str
message = """<html>
<head></head>
<body>"""+tableMaker(ls)+listMaker(ls2)+"""</body>
</html>"""

f.write(message)
f.close()