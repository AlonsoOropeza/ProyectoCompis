#####################
# Alonso Oropeza
# parsing table and string analyzer
# Compiladores
# 20/11/2021
####################

import firstFollows as fF
import pandas as pd

# creates parsing table
def parsingTable(nonTerms, terms, firsts, dic, follows):
    cols = list(terms)
    if ' ' in cols: cols.remove(' ')
    cols.append('$')
    df  = pd.DataFrame(columns = cols, index=nonTerms, data='')
    #aqui empieza lo chido
    #print(dic, firsts, follows)
    for nonTerm in nonTerms:
        for prod in dic[nonTerm]:
            #terminals
            if prod[0] in terms:
                if prod[0] != ' ': #first rule
                    df[prod[0]][nonTerm] = nonTerm+" -> "+" ".join(prod)
                else:
                    df = addFollowsIfEpsilon(follows, df, nonTerm) 
            #non terminals
            elif prod[0] in nonTerms:
                for first in firsts[prod[0]]: #first rule
                    if first != ' ':
                        df[first][nonTerm] = nonTerm+" -> "+" ".join(prod)
                if ' ' in firsts[prod[0]]: # second and third rule
                    df = addFollowsIfEpsilon(follows, df, nonTerm) 
    return df

#second and third rule
def addFollowsIfEpsilon(follows, df, nonTerm):
    for follow in follows[nonTerm]:
        if follow != ' ': #sanity check
            df[follow][nonTerm] = nonTerm+" -> ' '"
    return df

def parseStrings(strings,df,nonTerm):
    results = list()
    for string in strings:
        string = string.replace('\n','')
        string = string.split()
        results.append(parseString(string,df,nonTerm))
        print('\n')
    return results

def saveToStack(string, cols, df, nonTerm, pringles):
    if string[0] not in cols:
        return []
    #fill the stack with S rule
    rule = df[string[0]][nonTerm].split(' -> ')[1]
    rule = rule.split()
    for i in range(len(rule)-1,-1,-1):
        pringles.insert(0,rule[i]) #save to stack
    return pringles

def parseString(string,df,nonTerm):
    cols = list(df.columns)
    pringles = []
    pringles = saveToStack(string, cols, df, nonTerm, pringles)
    while (pringles != [] and string != []):
        print(pringles, string)
        if pringles[0] == string[0]:
            pringles.pop(0)
            string.pop(0)
        else:
            if pringles[0] in cols: #a terminal that doesnt unify
                return 'No'
            else:
                nonTerm = pringles[0]
                pringles.pop(0)
                pringles = saveToStack(string, cols, df, nonTerm, pringles)
    if (pringles == [] and string == []):
        return 'Yes'
    else:
        return 'No'

# main function of parser.py, calls other functions
def parser(firsts, follows, LL1, terms, nonTerms, strings, dic):
    df = parsingTable(nonTerms, terms, firsts, dic, follows)
    msg=parseStrings(strings, df, nonTerms[0])
    toHTML(df, msg)

def listMaker(ls):
    msg = ""
    for i in range(len(ls)):
        msg += """<b>""" + str(i) + """: </b>""" + ls[i] + """</br>"""
    return  msg

def toHTML(df,ls):
    f = open('parser.html','w')
    message = """<html>
    <head></head>
    <body>"""+df.to_html()+listMaker(ls)+"""</body>
    </html>"""
    f.write(message)
    f.close()