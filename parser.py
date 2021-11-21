
#####################
# Alonso Oropeza
# parsing table and string analyzer
# Compiladores
# 20/11/2021
####################

from numpy import string_
import firstFollows as fF
import pandas as pd

ls = ['yes','no','no']


# creates parsing table
def parsingTable(nonTerms, terms):
    df  = pd.DataFrame(columns = terms, index=nonTerms)
    return df

# main function of parser.py, calls other functions
def parser(firsts, follows, LL1, terms, nonTerms, strings):
    df = parsingTable(nonTerms, terms)
    print(df)
    toHTML(df, ls)

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